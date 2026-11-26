"""
split_chapters.py
=================
Egyptian Ministry of Education — Textbook Chapter Splitter (v3)
--------------------------------------------------------------
Enhanced with support for:
1. Standard Arabic/English/French units: الوحدة, المحور, الفصل, الباب, Unit, Chapter, Thème, Unité
2. Chinese units: 第一单元, 第二单元, 第三单元, 第四单元...
3. Numbered unit sections without keyword: "1 أساسيات ...", "2 أساسيات ..."
4. Multi-line TOC layouts where titles and numbers are on adjacent lines
5. Assessment periods: الفترة الأولى, الفترة الثانية, الفترة الثالثة
6. Safe page processing (skips corrupt font tables without hanging)
"""

import argparse
import logging
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF (fitz) is required. Install with: pip install pymupdf")

AR_DIGIT_MAP = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

# Arabic/English/French/Chinese chapter keywords
CHAPTER_KEYWORDS_RE = re.compile(
    r'(?:الوحدة|المحور|الفصل|الموضوع|الباب|الفترة|Unit|Chapter|Theme|Module|Part|Unité|Chapitre|Thème|Partie|第[一二三四五六七八九十]+单元)\s*([^\n\.\:]{1,70})?',
    re.IGNORECASE
)

# Numbered section header at start of line in TOC (e.g. "1والتمويل النقود أساسيات", "2و القتصاد")
NUMBERED_TOC_RE = re.compile(r'^[1-9١-٩]\s*[\u0600-\u06FF]{2,}', re.UNICODE)

EXCLUDE_KEYWORDS = [
    'تدريب', 'تقييم', 'مراجعة', 'امتحان', 'أسئلة', 'حلول', 'إجابات', 'اختبار',
    'Review', 'Exercises', 'Exercise', 'Test', 'Exam', 'Summary', 'Index', 'Glossary'
]

def clean_arabic(text: str) -> str:
    """Normalize NFKC, strip diacritics, tatweel, and invisible control characters while preserving newlines."""
    if not text:
        return ""
    text = unicodedata.normalize('NFKC', text)
    # Normalize \r\n and \r to \n
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # Remove control characters EXCEPT \n and \t
    text = re.sub(r'[\x00-\x08\x0b-\x1f\x7f-\x9f\u200c-\u200f\ufeff]', '', text)
    # Remove diacritics (tashkeel) and tatweel
    text = re.sub(r'[\u064B-\u065F\u0670\u0640]', '', text)
    return text

def sanitize_title(title: str, max_len: int = 70) -> str:
    """Make title safe for Windows file paths."""
    title = re.sub(r'[\\/:*?"<>|]', '-', title)
    title = re.sub(r'\s+', ' ', title).strip(' -')
    return title[:max_len] if title else "chapter"

def parse_page_num(num_str: str, total_pages: int, prev_page: int = 0) -> int:
    """Parse Arabic or Western page number, handling reversed RTL digits."""
    is_ar_digit = any(c in '٠١٢٣٤٥٦٧٨٩' for c in num_str)
    num_ascii = num_str.translate(AR_DIGIT_MAP)
    try:
        val = int(num_ascii)
        rev_val = int(num_ascii[::-1]) if len(num_ascii) > 1 else val
        
        # If extracted from Arabic RTL text, multi-digit numbers are extracted backwards
        if is_ar_digit and len(num_ascii) > 1:
            if 1 <= rev_val <= total_pages:
                return rev_val
            if 1 <= val <= total_pages:
                return val
        else:
            if 1 <= val <= total_pages and val >= prev_page:
                return val
            if 1 <= rev_val <= total_pages and rev_val >= prev_page:
                return rev_val
            if 1 <= val <= total_pages:
                return val
    except ValueError:
        pass
    return -1

def detect_chapters_from_pdf_toc(doc: fitz.Document) -> List[Dict[str, Any]]:
    """Strategy 1: PDF embedded bookmarks / outline."""
    total_pages = len(doc)
    toc = doc.get_toc(simple=True)
    if not toc:
        return []
    
    entries = []
    for lvl, title, p_1based in toc:
        t = title.strip()
        if not re.search(r'wizara|Book_|[_\-]{2,}|^Page\s*\d+$', t, re.I) and len(t) > 2:
            p_idx = max(0, min(total_pages - 1, p_1based - 1))
            entries.append((p_idx, sanitize_title(t)))
            
    if len(entries) >= 2:
        seen = set()
        res = []
        for p, t in entries:
            if p not in seen:
                seen.add(p)
                res.append({'page': p, 'title': t, 'source': 'pdf-toc'})
        if len(res) >= 2:
            return sorted(res, key=lambda x: x['page'])
    return []

def detect_chapters_from_printed_toc(doc: fitz.Document) -> List[Dict[str, Any]]:
    """Strategy 2: Printed Table of Contents page (in first 14 pages)."""
    total_pages = len(doc)
    for toc_idx in range(min(14, total_pages)):
        try:
            raw_text = doc[toc_idx].get_text()
        except Exception:
            continue
            
        page_txt = clean_arabic(raw_text)
        if any(k in page_txt for k in ['الفهرس', 'المحتويات', 'المحتوى', 'Contents', 'CONTENTS', 'Table of Contents', 'Sommaire', 'Table des matières', '目录']):
            lines = [l.strip() for l in page_txt.split('\n') if l.strip()]
            entries = []
            prev_p = 0
            
            for idx, line in enumerate(lines):
                m_chap = CHAPTER_KEYWORDS_RE.search(line)
                m_num_sec = NUMBERED_TOC_RE.search(line)
                m_nums = re.findall(r'(\d+|[٠١٢٣٤٥٦٧٨٩]+)', line)
                
                matched_str = None
                if m_chap:
                    matched_str = m_chap.group(0).strip(' -:\t')
                elif m_num_sec:
                    matched_str = line[:50].strip(' -:\t')
                    
                if matched_str:
                    if any(ex in line for ex in EXCLUDE_KEYWORDS):
                        continue
                        
                    pg = -1
                    if m_nums:
                        cand_num = m_nums[0] if line.startswith(m_nums[0]) else m_nums[-1]
                        pg = parse_page_num(cand_num, total_pages, prev_p)
                    else:
                        # Lookahead 1-2 lines for page number
                        lookahead = lines[idx+1:min(len(lines), idx+3)]
                        for nxt in lookahead:
                            nxt_nums = re.findall(r'(\d+|[٠١٢٣٤٥٦٧٨٩]+)', nxt)
                            if nxt_nums:
                                pg = parse_page_num(nxt_nums[0], total_pages, prev_p)
                                if pg > 0:
                                    break
                                    
                    if pg > 0 and pg >= prev_p:
                        prev_p = pg
                        entries.append((pg - 1, sanitize_title(matched_str)))

            # Block inspection if line scanning yielded < 2
            if len(entries) < 2:
                try:
                    blocks = doc[toc_idx].get_text('blocks')
                except Exception:
                    blocks = []
                curr_title = None
                for b in blocks:
                    btxt = clean_arabic(b[4].strip())
                    m_kw = CHAPTER_KEYWORDS_RE.search(btxt) or NUMBERED_TOC_RE.search(btxt)
                    if m_kw and not any(ex in btxt for ex in EXCLUDE_KEYWORDS):
                        curr_title = sanitize_title(m_kw.group(0) if hasattr(m_kw, 'group') else btxt[:50])
                    elif curr_title:
                        m_nums = re.findall(r'(\d+|[٠١٢٣٤٥٦٧٨٩]+)', btxt)
                        if m_nums:
                            pg = parse_page_num(m_nums[0], total_pages, prev_p)
                            if pg > 0 and pg >= prev_p:
                                prev_p = pg
                                entries.append((pg - 1, curr_title))
                                curr_title = None

            if len(entries) >= 2:
                entries = sorted(entries, key=lambda x: x[0])
                dedup = []
                for p, t in entries:
                    if not dedup or p - dedup[-1]['page'] >= 3:
                        dedup.append({'page': p, 'title': t, 'source': 'printed-toc'})
                if len(dedup) >= 2:
                    return dedup
    return []

def detect_chapters_from_page_headings(doc: fitz.Document) -> List[Dict[str, Any]]:
    """Strategy 3: Scan initial pages for unit / chapter banner headings."""
    total_pages = len(doc)
    candidates = []
    start = 3 if total_pages > 15 else 0
    max_scan = min(total_pages, 50)
    
    for p in range(start, max_scan):
        try:
            txt = clean_arabic(doc[p].get_text())
        except Exception:
            continue
            
        if not txt:
            continue
        
        lines = [l.strip() for l in txt.split('\n') if l.strip()][:3]
        top_text = ' '.join(lines)
        
        m = CHAPTER_KEYWORDS_RE.search(top_text)
        if m:
            heading = m.group(0).strip()
            # Filter out non-chapter sections based on heading only
            if not any(ex in heading for ex in EXCLUDE_KEYWORDS):
                title = sanitize_title(heading)
                candidates.append((p, title))
                
    if candidates:
        dedup = []
        for p, t in candidates:
            if not dedup or p - dedup[-1]['page'] >= 4:
                dedup.append({'page': p, 'title': t, 'source': 'text-heading'})
        if len(dedup) >= 2:
            return dedup
    return []

def detect_chapters(doc: fitz.Document) -> List[Dict[str, Any]]:
    """Unified detector: tries Strategies 1 -> 2 -> 3 -> Fallback."""
    total_pages = len(doc)
    if total_pages == 0:
        return []
        
    res = detect_chapters_from_pdf_toc(doc)
    if res:
        return res
        
    res = detect_chapters_from_printed_toc(doc)
    if res:
        return res
        
    res = detect_chapters_from_page_headings(doc)
    if res:
        return res
        
    return [{'page': 0, 'title': 'كامل الكتاب - Full Book', 'source': 'fallback'}]

def split_pdf_book(
    pdf_path: Path,
    out_dir: Path,
    verbose: bool = False
) -> int:
    """Split a single PDF textbook into chapters inside out_dir."""
    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        logging.error(f"Failed to open {pdf_path}: {e}")
        return 0
        
    total_pages = len(doc)
    if total_pages == 0:
        doc.close()
        return 0
        
    chapters = detect_chapters(doc)
    if not chapters:
        chapters = [{'page': 0, 'title': 'كامل الكتاب - Full Book', 'source': 'fallback'}]
        
    if chapters[0]['page'] > 0:
        chapters.insert(0, {'page': 0, 'title': 'المقدمة والتهيئة - Introduction', 'source': 'preface'})
        
    out_dir.mkdir(parents=True, exist_ok=True)
    num_written = 0
    
    for idx, chap in enumerate(chapters):
        start_p = chap['page']
        end_p = chapters[idx + 1]['page'] if idx + 1 < len(chapters) else total_pages
        if end_p <= start_p:
            continue
            
        safe_title = sanitize_title(chap['title'])
        filename = f"chapter-{idx+1:02d}-{safe_title}.pdf"
        dest_file = out_dir / filename
        
        if dest_file.exists():
            num_written += 1
            continue
            
        try:
            out_doc = fitz.open()
            out_doc.insert_pdf(doc, from_page=start_p, to_page=end_p - 1)
            out_doc.save(str(dest_file))
            out_doc.close()
            num_written += 1
            if verbose:
                logging.info(f"  Wrote: {filename} (pages {start_p+1}-{end_p})")
        except Exception as e:
            logging.error(f"  Error writing {filename}: {e}")
            
    doc.close()
    return num_written

def process_directory(
    source_dir: Path,
    out_root: Path,
    books_root: Path,
    verbose: bool = False
) -> Tuple[int, int]:
    """Process all PDF files under source_dir recursively."""
    pdfs = sorted(source_dir.rglob("*.pdf"))
    logging.info(f"Found {len(pdfs)} PDF textbooks under {source_dir}")
    
    total_books = 0
    total_chapters = 0
    
    for pdf in pdfs:
        try:
            rel = pdf.parent.relative_to(books_root)
        except ValueError:
            rel = pdf.parent.relative_to(source_dir)
            
        book_folder = out_root / rel / pdf.stem
        n = split_pdf_book(pdf, book_folder, verbose=verbose)
        total_chapters += n
        total_books += 1
        logging.info(f"[{total_books}/{len(pdfs)}] {pdf.name} -> {n} chapter(s)")
        
    return total_books, total_chapters

def main():
    parser = argparse.ArgumentParser(description="Split MoE textbook PDFs into chapters.")
    parser.add_argument("--source", required=True, type=Path, help="Source directory containing PDFs.")
    parser.add_argument("--out-root", type=Path, default=None, help="Root output directory.")
    parser.add_argument("--books-root", type=Path, default=None, help="Root books directory.")
    parser.add_argument("--verbose", action="store_true", help="Print detailed page ranges.")
    args = parser.parse_args()
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )
    
    source = args.source.resolve()
    if not source.exists():
        sys.exit(f"Directory not found: {source}")
        
    books_root = args.books_root.resolve() if args.books_root else Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books")
    out_root = args.out_root.resolve() if args.out_root else Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books-by-chapter")
    
    b_count, c_count = process_directory(source, out_root, books_root, verbose=args.verbose)
    logging.info(f"COMPLETE: {b_count} books processed, {c_count} chapters written.")

if __name__ == "__main__":
    main()
