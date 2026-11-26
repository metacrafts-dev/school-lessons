"""
Quick test: run split_chapters logic on 2 specific PDFs and show results.
"""
import sys, logging
sys.path.insert(0, r"D:\WORKSPACE\PROJECTS\school-lessons\scripts")
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

from pathlib import Path
import fitz, statistics, re

# Import detection functions from the main script
import importlib.util
spec = importlib.util.spec_from_file_location(
    "split_chapters",
    r"D:\WORKSPACE\PROJECTS\school-lessons\scripts\split_chapters.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TEST_BOOKS = [
    r"D:\WORKSPACE\PROJECTS\school-lessons\books\primary\year-1\term-1\اللغة العربية\Arabic_language_prim1_t1.pdf",
    r"D:\WORKSPACE\PROJECTS\school-lessons\books\primary\year-4\term-1\العلوم باللغة العربية\Science_Ar_prim4_t1.pdf",
]

for book_path in TEST_BOOKS:
    p = Path(book_path)
    if not p.exists():
        print(f"NOT FOUND: {book_path}")
        continue
    doc = fitz.open(str(p))
    total = doc.page_count
    print(f"\n{'='*60}")
    print(f"Book: {p.name}  ({total} pages)")

    # P1
    b = mod.detect_chapters_toc(doc)
    print(f"P1 TOC: {len(b)} boundaries -> {b[:5]}")

    # P2
    sizes = mod.collect_font_sizes(doc)
    med = statistics.median(sizes) if sizes else 12
    print(f"  median font size: {med:.1f}")
    b2 = mod.detect_chapters_font(doc, med, verbose=True)
    print(f"P2 font: {len(b2)} boundaries -> {b2[:8]}")

    # P3
    b3 = mod.detect_chapters_keywords(doc, verbose=False)
    print(f"P3 keyword: {len(b3)} boundaries -> {b3[:8]}")
    doc.close()
print("\nDone.")
