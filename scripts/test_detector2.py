"""
Comprehensive detector test script.
"""
import sys, re, unicodedata
from pathlib import Path
import fitz

AR_DIGIT_MAP = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

def clean_arabic(text: str) -> str:
    if not text: return ""
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'[\x00-\x1f\x7f-\x9f\u200c-\u200f\ufeff]', '', text)
    text = re.sub(r'[\u064B-\u065F\u0670\u0640]', '', text)
    return text

def sanitize_title(title: str, max_len: int = 70) -> str:
    title = re.sub(r'[\\/:*?"<>|]', '-', title)
    title = re.sub(r'\s+', ' ', title).strip(' -')
    return title[:max_len]

def parse_page_num(num_str: str, total_pages: int, prev_page: int = 0) -> int:
    num_ascii = num_str.translate(AR_DIGIT_MAP)
    try:
        val = int(num_ascii)
        # Check reversed digits (e.g. 51 -> 15, 64 -> 46)
        rev_val = int(num_ascii[::-1]) if len(num_ascii) > 1 else val
        # If val is > total_pages but rev_val is <= total_pages: definitely reversed
        if val > total_pages and rev_val <= total_pages:
            return rev_val
        # If rev_val is closer to or greater than prev_page and <= total_pages:
        if val < prev_page and rev_val >= prev_page and rev_val <= total_pages:
            return rev_val
        if 1 <= val <= total_pages:
            return val
        if 1 <= rev_val <= total_pages:
            return rev_val
    except ValueError:
        pass
    return -1

def detect_chapters(doc: fitz.Document) -> list:
    total_pages = len(doc)
    
    # ---------------------------------------------------------
    # 1. Embedded PDF Bookmarks / Outline
    # ---------------------------------------------------------
    toc = doc.get_toc(simple=True)
    if toc:
        entries = []
        for lvl, title, p_1based in toc:
            t = title.strip()
            if not re.search(r'wizara|Book_|[_\-]{2,}|^Page\s*\d+$', t, re.I) and len(t) > 2:
                p_idx = max(0, min(total_pages - 1, p_1based - 1))
                entries.append((p_idx, t))
        if len(entries) >= 2:
            seen = set()
            res = []
            for p, t in entries:
                if p not in seen:
                    seen.add(p)
                    res.append({'page': p, 'title': sanitize_title(t), 'source': 'pdf-toc'})
            if len(res) >= 2:
                return sorted(res, key=lambda x: x['page'])

    # ---------------------------------------------------------
    # 2. Printed Table of Contents Page (Pages 1 - 12)
    # ---------------------------------------------------------
    for toc_idx in range(min(12, total_pages)):
        page_txt = clean_arabic(doc[toc_idx].get_text())
        if any(k in page_txt for k in ['الفهرس', 'المحتويات', 'المحتوى', 'Contents', 'CONTENTS', 'Table of Contents', 'Sommaire']):
            lines = [l.strip() for l in page_txt.split('\n') if l.strip()]
            toc_entries = []
            prev_p = 0
            
            for line in lines:
                # Check for major unit keywords
                m_chap = re.search(r'(الوحدة|المحور|الفصل|الباب|Unit|Chapter|Theme|Module|Unité|Chapitre)[^\.\d٠-٩\n]*', line, re.I)
                # Check for page number in line (usually separated by dots)
                m_nums = re.findall(r'(\d+|[٠١٢٣٤٥٦٧٨٩]+)', line)
                
                if m_chap and m_nums:
                    # Usually the page number is the first or last number in the line
                    cand_num = m_nums[0] if line.startswith(m_nums[0]) else m_nums[-1]
                    pg = parse_page_num(cand_num, total_pages, prev_p)
                    if pg > 0:
                        prev_p = pg
                        title = sanitize_title(m_chap.group(0))
                        toc_entries.append((pg - 1, title))
            
            # Also check block-level layout where title and page number are in separate lines
            if len(toc_entries) < 2:
                # Iterate through blocks
                blocks = doc[toc_idx].get_text('blocks')
                curr_title = None
                for b in blocks:
                    btxt = clean_arabic(b[4].strip())
                    m_kw = re.search(r'(الوحدة\s+[^\n]+|المحور\s+[^\n]+|الفصل\s+[^\n]+|Unit\s+[^\n]+|Chapter\s+[^\n]+)', btxt, re.I)
                    if m_kw:
                        curr_title = sanitize_title(m_kw.group(1))
                    elif curr_title:
                        m_nums = re.findall(r'(\d+|[٠١٢٣٤٥٦٧٨٩]+)', btxt)
                        if m_nums:
                            pg = parse_page_num(m_nums[0], total_pages, prev_p)
                            if pg > 0:
                                prev_p = pg
                                toc_entries.append((pg - 1, curr_title))
                                curr_title = None

            if len(toc_entries) >= 2:
                # Sort and deduplicate
                toc_entries = sorted(toc_entries, key=lambda x: x[0])
                dedup = []
                for p, t in toc_entries:
                    if not dedup or p - dedup[-1]['page'] >= 3:
                        dedup.append({'page': p, 'title': t, 'source': 'printed-toc'})
                if len(dedup) >= 2:
                    return dedup

    # ---------------------------------------------------------
    # 3. Direct Full-Text Page Scan (Look for Unit / Chapter Banners)
    # ---------------------------------------------------------
    unit_re = re.compile(
        r'(?:^|\n)\s*(?:الْ?وَحْدَة|الْ?مِحْوَر|الْ?فَصْل|الْ?بَاب|الوحدة|المحور|الفصل|الباب|Unit|Chapter|Theme|Module|Unité|Chapitre)\s*([^\n]+)',
        re.I
    )
    candidates = []
    start = 3 if total_pages > 15 else 0
    for p in range(start, total_pages):
        txt = clean_arabic(doc[p].get_text())
        if not txt: continue
        # Take the first 3 lines
        first_lines = [l.strip() for l in txt.split('\n') if l.strip()][:3]
        joined_top = ' '.join(first_lines)
        m = unit_re.search(joined_top)
        if m:
            heading = m.group(0).strip()
            # Filter out exercises / tests / reviews
            if not any(w in heading for w in ['تدريبات', 'تقييم', 'مراجعة', 'امتحان', 'أسئلة', 'Review', 'Exercises', 'Test']):
                title = sanitize_title(heading)
                candidates.append((p, title))

    if candidates:
        dedup = []
        for p, t in candidates:
            if not dedup or p - dedup[-1]['page'] >= 4:
                dedup.append({'page': p, 'title': t, 'source': 'text-heading'})
        if len(dedup) >= 2:
            return dedup

    # ---------------------------------------------------------
    # 4. Fallback
    # ---------------------------------------------------------
    return [{'page': 0, 'title': 'كامل الكتاب - Full Book', 'source': 'fallback'}]

books_root = Path(r'D:\WORKSPACE\PROJECTS\school-lessons\books')
sample = [
    books_root / r'primary\year-1\term-1\اللغة العربية\Arabic_language_prim1_t1.pdf',
    books_root / r'primary\year-4\term-1\العلوم باللغة العربية\Science_Ar_prim4_t1.pdf',
    books_root / r'prep\year-1\term-1\العلوم باللغة العربية\Science_Prep1_T1.pdf',
]

for b in sample:
    if not b.exists(): continue
    doc = fitz.open(b)
    ch = detect_chapters(doc)
    print(f"\n{'='*65}\n{b.name} ({len(doc)}p) -> {len(ch)} chapters via {ch[0]['source']}:")
    for i, item in enumerate(ch, 1):
        print(f"  {i}. Page {item['page']+1}: {item['title']}")
    doc.close()
