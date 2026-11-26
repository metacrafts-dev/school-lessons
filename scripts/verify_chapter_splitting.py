"""
verify_chapter_splitting.py
===========================
Comprehensive audit script for verifying textbook chapter splitting across
all 5 Egyptian Ministry of Education stages:
1. Kindergarten (kindergarten)
2. Primary (primary)
3. Preparatory (prep)
4. High School (high-school)
5. Baccalaureate (baccalaureate)

Checks:
- 296/296 source books accounted for in destination directories
- Zero books contain single-file fallback ('كامل الكتاب' / 'Full Book')
- Every book directory contains >= 2 genuine chapter PDFs
- 100% of chapter PDFs are non-empty and valid (%PDF header + PyMuPDF loadable)
- Full statistical breakdown by educational stage
"""

import os
import sys
import json
from pathlib import Path
import fitz

BOOKS_ROOT = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books")
CHAPTERS_ROOT = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books-by-chapter")
REPORT_PATH = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\verification_split_report.json")

STAGES = [
    ("kindergarten", "رياض الأطفال (Kindergarten)"),
    ("primary", "المرحلة الابتدائية (Primary)"),
    ("prep", "المرحلة الإعدادية (Preparatory)"),
    ("high-school", "مرحلة الثانوية العامة (High School)"),
    ("baccalaureate", "شهادة البكالوريا الدولية/المصرية (Baccalaureate)")
]

def verify_all():
    print("=" * 75)
    print("STARTING AUDIT: School Lessons Curriculum Chapter Splitting Verification")
    print("=" * 75)

    source_books = sorted(list(BOOKS_ROOT.rglob("*.pdf")))
    total_source_books = len(source_books)
    print(f"Total source textbooks found in {BOOKS_ROOT}: {total_source_books}")

    results_by_stage = {}
    all_books_status = []
    total_chapter_files = 0
    total_chapter_size_bytes = 0
    total_fallbacks = 0
    total_lt2_chapters = 0
    corrupt_files = []

    for stage_key, stage_name in STAGES:
        stage_dir = BOOKS_ROOT / stage_key
        stage_books = sorted(list(stage_dir.rglob("*.pdf"))) if stage_dir.exists() else []

        stage_stat = {
            "stage_key": stage_key,
            "stage_name": stage_name,
            "source_book_count": len(stage_books),
            "verified_book_dirs": 0,
            "total_chapters": 0,
            "total_size_mb": 0.0,
            "books_with_fallback": 0,
            "books_under_2_chapters": 0,
            "valid_pdfs": 0,
            "corrupt_pdfs": 0,
            "all_passed": True
        }

        stage_size_bytes = 0

        for b in stage_books:
            rel = b.relative_to(BOOKS_ROOT)
            # Corresponding chapter dir is chapters_root / rel.parent / b.stem
            target_dir = CHAPTERS_ROOT / rel.parent / b.stem
            
            book_info = {
                "rel_path": str(rel),
                "book_name": b.name,
                "stage": stage_key,
                "target_dir": str(target_dir),
                "exists": target_dir.exists(),
                "fallback_found": False,
                "fallback_files": [],
                "chapter_count": 0,
                "chapters": [],
                "passed": False
            }

            if not target_dir.exists():
                stage_stat["all_passed"] = False
                all_books_status.append(book_info)
                continue

            stage_stat["verified_book_dirs"] += 1
            all_files = list(target_dir.glob("*.pdf"))

            fallback_files = [f for f in all_files if "كامل الكتاب" in f.name or "Full Book" in f.name]
            chapter_files = [f for f in all_files if f not in fallback_files]

            if fallback_files:
                stage_stat["books_with_fallback"] += 1
                total_fallbacks += 1
                book_info["fallback_found"] = True
                book_info["fallback_files"] = [f.name for f in fallback_files]

            chap_count = len(chapter_files)
            book_info["chapter_count"] = chap_count
            stage_stat["total_chapters"] += chap_count
            total_chapter_files += chap_count

            if chap_count < 2:
                stage_stat["books_under_2_chapters"] += 1
                total_lt2_chapters += 1

            # Check validity of each chapter file
            for ch_file in chapter_files:
                f_size = ch_file.stat().st_size
                stage_size_bytes += f_size
                total_chapter_size_bytes += f_size

                # Fast check header
                is_valid = True
                try:
                    with open(ch_file, "rb") as f:
                        header = f.read(5)
                        if header != b"%PDF-":
                            is_valid = False
                except Exception:
                    is_valid = False

                if is_valid and f_size > 0:
                    try:
                        doc = fitz.open(ch_file)
                        if len(doc) == 0:
                            is_valid = False
                        doc.close()
                    except Exception:
                        is_valid = False

                if is_valid:
                    stage_stat["valid_pdfs"] += 1
                else:
                    stage_stat["corrupt_pdfs"] += 1
                    corrupt_files.append(str(ch_file))

            passed = (not book_info["fallback_found"]) and (chap_count >= 2)
            book_info["passed"] = passed
            if not passed:
                stage_stat["all_passed"] = False

            all_books_status.append(book_info)

        stage_stat["total_size_mb"] = round(stage_size_bytes / (1024 * 1024), 2)
        results_by_stage[stage_key] = stage_stat

    # Output report
    print("\n" + "=" * 90)
    print("STAGE-BY-STAGE VERIFICATION SUMMARY")
    print("=" * 90)
    header = f"{'Educational Stage':<38} | {'Books':<5} | {'Dirs':<5} | {'Chapters':<8} | {'Fallbacks':<9} | {'< 2 Chaps':<9} | {'Status':<6}"
    print(header)
    print("-" * 90)

    all_stages_passed = True
    for stage_key, stage_name in STAGES:
        st = results_by_stage[stage_key]
        status_str = "PASS" if st["all_passed"] and st["books_with_fallback"] == 0 and st["books_under_2_chapters"] == 0 else "FAIL"
        if status_str != "PASS":
            all_stages_passed = False
        print(f"{st['stage_name']:<38} | {st['source_book_count']:<5} | {st['verified_book_dirs']:<5} | {st['total_chapters']:<8} | {st['books_with_fallback']:<9} | {st['books_under_2_chapters']:<9} | {status_str:<6}")

    print("-" * 90)
    total_size_mb = round(total_chapter_size_bytes / (1024 * 1024), 2)
    grand_status = "PASSED (100% OK)" if (all_stages_passed and total_fallbacks == 0 and total_lt2_chapters == 0 and len(corrupt_files) == 0) else "INCOMPLETE / FAILED"
    print(f"{'GRAND TOTAL':<38} | {total_source_books:<5} | {len(all_books_status):<5} | {total_chapter_files:<8} | {total_fallbacks:<9} | {total_lt2_chapters:<9} | {grand_status}")
    print(f"Total Size of Chapter PDFs: {total_size_mb:.2f} MB")
    print(f"Corrupt/Invalid Chapter PDFs: {len(corrupt_files)}")
    print("=" * 90)

    # Save complete JSON audit
    full_report = {
        "status": grand_status,
        "total_source_books": total_source_books,
        "total_verified_books": len(all_books_status),
        "total_chapter_files": total_chapter_files,
        "total_size_mb": total_size_mb,
        "total_fallbacks_remaining": total_fallbacks,
        "total_under_2_chapters": total_lt2_chapters,
        "corrupt_files_count": len(corrupt_files),
        "stages": results_by_stage,
        "books": all_books_status
    }

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(full_report, f, ensure_ascii=False, indent=2)
    print(f"Detailed verification report written to: {REPORT_PATH}")

    return full_report

if __name__ == "__main__":
    verify_all()
