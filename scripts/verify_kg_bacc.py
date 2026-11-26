import sys
from pathlib import Path
import fitz

books_root = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books")
chapters_root = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books-by-chapter")

stages = ["kindergarten", "baccalaureate"]
errors = []
stats = {stage: {"books": 0, "chapters": 0} for stage in stages}
detailed_breakdown = {}

for stage in stages:
    stage_books = sorted(list((books_root / stage).rglob("*.pdf")))
    detailed_breakdown[stage] = []
    
    for b in stage_books:
        rel = b.relative_to(books_root)
        stem = b.stem
        target_dir = chapters_root / rel.parent / stem
        
        if not target_dir.exists():
            errors.append(f"Missing target dir: {target_dir}")
            continue
            
        chapter_files = sorted(list(target_dir.glob("*.pdf")))
        if len(chapter_files) < 2:
            errors.append(f"Fewer than 2 chapters ({len(chapter_files)}) in {rel}")
            
        fallback_files = [f for f in chapter_files if "كامل الكتاب" in f.name]
        if fallback_files:
            errors.append(f"Contains fallback files ({[f.name for f in fallback_files]}) in {rel}")
            
        # Verify with PyMuPDF
        valid_chapters = 0
        total_pages = 0
        for f in chapter_files:
            try:
                doc = fitz.open(f)
                p_cnt = len(doc)
                if p_cnt == 0:
                    errors.append(f"Zero-page PDF: {f}")
                total_pages += p_cnt
                valid_chapters += 1
                doc.close()
            except Exception as e:
                errors.append(f"Corrupted PDF {f}: {e}")
                
        stats[stage]["books"] += 1
        stats[stage]["chapters"] += valid_chapters
        detailed_breakdown[stage].append({
            "rel": str(rel),
            "stem": stem,
            "chapters": valid_chapters,
            "pages": total_pages
        })

print("\n" + "=" * 65)
print("VERIFICATION SUMMARY")
print("=" * 65)
for stage in stats:
    b_cnt = stats[stage]["books"]
    c_cnt = stats[stage]["chapters"]
    print(f"{stage}: {b_cnt} books verified, {c_cnt} valid chapter PDFs")

print(f"\nTotal Errors / Violations: {len(errors)}")
if errors:
    for err in errors:
        print(f"ERROR: {err}")
else:
    print("SUCCESS: Zero errors! All books have >= 2 chapters, 0 fallback files, and all PDFs are valid!")
print("=" * 65)

print("\n--- DETAILED BREAKDOWN ---")
for stage in stages:
    print(f"\n[{stage.upper()}] ({len(detailed_breakdown[stage])} books):")
    for item in detailed_breakdown[stage]:
        print(f"  - {item['stem']}: {item['chapters']} chapters ({item['pages']} pages)")
