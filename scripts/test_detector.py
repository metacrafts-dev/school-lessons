"""
Test and refine the unified multi-layer chapter detection engine.
"""
import sys, re, unicodedata
from pathlib import Path
import fitz

# Arabic words for numbers
AR_ORDINALS = {
    'الاولى': 1, 'الاول': 1, 'الثانية': 2, 'الثاني': 2, 'الثالثة': 3, 'الثالث': 3,
    'الرابعة': 4, 'الرابع': 4, 'الخامسة': 5, 'الخامس': 5, 'السادسة': 6, 'السادس': 6,
    'السابعة': 7, 'السابع': 7, 'الثامنة': 8, 'الثامن': 8, 'التاسعة': 9, 'التاسع': 9,
    'العاشرة': 10, 'العاشر': 10, 'الحادية عشرة': 11, 'الحادي عشر': 11,
    'الثانية عشرة': 12, 'الثاني عشر': 12,
}

AR_DIGIT_MAP = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

def clean_arabic(text: str) -> str:
    """Normalize NFKC, strip diacritics, tatweel, and control chars."""
    if not text:
        return ""
    text = unicodedata.normalize('NFKC', text)
    # remove control characters
    text = re.sub(r'[\x00-\x1f\x7f-\x9f\u200c-\u200f\ufeff]', '', text)
    # remove diacritics & tatweel
    text = re.sub(r'[\u064B-\u065F\u0670\u0640]', '', text)
    return text

def sanitize_title(title: str, max_len: int = 70) -> str:
    title = re.sub(r'[\\/:*?"<>|]', '-', title)
    title = re.sub(r'\s+', ' ', title).strip(' -')
    return title[:max_len]

def detect_chapters(doc: fitz.Document) -> list:
    """
    Returns list of dicts: [{'page': 0-based page index, 'title': str}]
    """
    total_pages = len(doc)
    
    # -------------------------------------------------------------
    # Strategy 1: Check PDF embedded bookmarks / TOC
    # -------------------------------------------------------------
    toc = doc.get_toc(simple=True)
    if toc:
        # Check if TOC entries look real
        real_entries = []
        for lvl, title, page_1based in toc:
            t = title.strip()
            # filter out raw file paths / wizara / Book_ / page numbers
            if not re.search(r'wizara|Book_|[_\-]{2,}|^Page\s*\d+$', t, re.I) and len(t) > 2:
                p_idx = max(0, min(total_pages - 1, page_1based - 1))
                real_entries.append((p_idx, t))
        if len(real_entries) >= 2:
            # Dedup pages
            seen_p = set()
            res = []
            for p, t in real_entries:
                if p not in seen_p:
                    seen_p.add(p)
                    res.append({'page': p, 'title': t, 'source': 'pdf-toc'})
            if len(res) >= 2:
                return sorted(res, key=lambda x: x['page'])

    # -------------------------------------------------------------
    # Strategy 2: Page-by-page full scan for major chapter headers
    # Look for Units, Axes, Chapters, Modules, Themes
    # -------------------------------------------------------------
    # Patterns to match at the beginning of lines or dominant blocks
    unit_patterns = [
        # Arabic: الوحدة / المحور / الفصل / الباب
        re.compile(r'(?:^|\n)\s*(الوحدة\s+(?:الأولى|الثانية|الثالثة|الرابعة|الخامسة|السادسة|السابعة|الثامنة|التاسعة|العاشرة|الحادية عشرة|الثانية عشرة|[٠١٢٣٤٥٦٧٨٩\d]+)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(المحور\s+(?:الأول|الثاني|الثالث|الرابع|الخامس|السادس|[٠١٢٣٤٥٦٧٨٩\d]+)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(الفصل\s+(?:الأول|الثاني|الثالث|الرابع|الخامس|السادس|السابع|الثامن|التاسع|العاشر|[٠١٢٣٤٥٦٧٨٩\d]+)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(الباب\s+(?:الأول|الثاني|الثالث|الرابع|الخامس|السادس|[٠١٢٣٤٥٦٧٨٩\d]+)[^\n]*)', re.I),
        # English: Unit / Chapter / Theme / Module
        re.compile(r'(?:^|\n)\s*(Unit\s+(?:\d+|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(Chapter\s+(?:\d+|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(Theme\s+(?:\d+|One|Two|Three|Four)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(Module\s+(?:\d+|One|Two|Three|Four|Five|Six)[^\n]*)', re.I),
        # French: Unité / Chapitre / Thème
        re.compile(r'(?:^|\n)\s*(Unité\s+(?:\d+|I|II|III|IV|V|VI)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(Chapitre\s+(?:\d+|I|II|III|IV|V|VI)[^\n]*)', re.I),
        re.compile(r'(?:^|\n)\s*(Thème\s+(?:\d+|I|II|III|IV)[^\n]*)', re.I),
    ]

    candidates = []
    # Start scanning after initial title/preface pages (e.g. from page 4 onwards, or page 0 if book is short)
    start_page = 3 if total_pages > 15 else 0

    for i in range(start_page, total_pages):
        page = doc[i]
        txt = clean_arabic(page.get_text())
        if not txt:
            continue
        
        # Check against patterns
        matched = False
        for pat in unit_patterns:
            m = pat.search(txt)
            if m:
                heading = m.group(1).strip()
                # Clean up heading: take first line or up to 60 chars
                heading = heading.split('\n')[0].strip()
                # Exclude if it mentions 'تدريبات' (exercises) or 'تقييم' (evaluation) or 'نهاية' (end)
                if any(w in heading for w in ['تدريبات', 'تقييم', 'مراجعة', 'امتحان', 'أسئلة', 'Review', 'Exercises', 'Test']):
                    continue
                candidates.append((i, heading))
                matched = True
                break

    if candidates:
        # Group and deduplicate: chapters should be separated by at least 3 pages
        # and consecutive entries with the same core unit number should be collapsed
        filtered = []
        for p, h in candidates:
            if not filtered:
                filtered.append({'page': p, 'title': h, 'source': 'text-heading'})
            else:
                last_p = filtered[-1]['page']
                last_h = filtered[-1]['title']
                if p - last_p < 4:
                    # Too close: keep the one with longer/better title
                    if len(h) > len(last_h):
                        filtered[-1] = {'page': last_p, 'title': h, 'source': 'text-heading'}
                else:
                    filtered.append({'page': p, 'title': h, 'source': 'text-heading'})

        if len(filtered) >= 2:
            return filtered

    # -------------------------------------------------------------
    # Strategy 3: Printed TOC Parsing in first 12 pages
    # -------------------------------------------------------------
    for toc_p in range(min(12, total_pages)):
        raw_toc_text = clean_arabic(doc[toc_p].get_text())
        if any(k in raw_toc_text for k in ['الفهرس', 'المحتويات', 'المحتوى', 'Contents', 'CONTENTS', 'Table of Contents', 'Sommaire']):
            # Look for lines with chapter titles and page numbers
            lines = [l.strip() for l in raw_toc_text.split('\n') if l.strip()]
            toc_parsed = []
            for line in lines:
                # Check for Unit/Chapter in line
                m_num = re.search(r'(\d+|[٠١٢٣٤٥٦٧٨٩]+)', line)
                m_chap = re.search(r'(الوحدة|المحور|الفصل|الباب|Unit|Chapter|Module|Theme)\s*([^\.0-9٠-٩]+)?', line)
                if m_chap and m_num:
                    num_str = m_num.group(1).translate(AR_DIGIT_MAP)
                    try:
                        pg = int(num_str)
                        # Check reversed 2-digit number (e.g. 62 -> 26)
                        if pg > total_pages and len(num_str) == 2:
                            pg = int(num_str[::-1])
                        if 1 <= pg <= total_pages:
                            title = m_chap.group(0).strip(' .:\t-')
                            toc_parsed.append({'page': pg - 1, 'title': title, 'source': 'printed-toc'})
                    except ValueError:
                        pass
            if len(toc_parsed) >= 2:
                # Sort and dedup
                toc_parsed = sorted(toc_parsed, key=lambda x: x['page'])
                dedup = []
                for entry in toc_parsed:
                    if not dedup or entry['page'] - dedup[-1]['page'] >= 3:
                        dedup.append(entry)
                if len(dedup) >= 2:
                    return dedup

    # -------------------------------------------------------------
    # Fallback: Single chapter for whole book
    # -------------------------------------------------------------
    return [{'page': 0, 'title': 'كامل الكتاب - Full Book', 'source': 'fallback'}]

# Test on 4 real books
test_files = [
    r"D:\WORKSPACE\PROJECTS\school-lessons\books\primary\year-1\term-1\اللغة العربية\Arabic_language_prim1_t1.pdf",
    r"D:\WORKSPACE\PROJECTS\school-lessons\books\primary\year-4\term-1\العلوم باللغة العربية\Science_Ar_prim4_t1.pdf",
    r"D:\WORKSPACE\PROJECTS\school-lessons\books\prep\year-1\term-1\العلوم باللغة العربية\Science_Prep1_T1.pdf",
    r"D:\WORKSPACE\PROJECTS\school-lessons\books\high-school\year-3\term-1\الفيزياء باللغة الإنجليزية\Physics_English_Sec3.pdf",
]

for f in test_files:
    p = Path(f)
    if not p.exists():
        continue
    doc = fitz.open(p)
    chaps = detect_chapters(doc)
    print(f"\n{'='*70}")
    print(f"Book: {p.name} ({len(doc)} pages)")
    print(f"Detected {len(chaps)} chapter(s) [via {chaps[0]['source']}]:")
    for idx, c in enumerate(chaps, 1):
        print(f"  {idx}. Page {c['page']+1}: {c['title']}")
    doc.close()
