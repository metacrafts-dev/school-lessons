"""Script to arrange downloaded PDFs from C:\\Users\\mrt\\Downloads into structured folders.

Sections:
1. kg                     -> D:\\WORKSPACE\\PROJECTS\\school-lessons\\books\\kindergarten\\<year>\\<term>\\<subject>\\
2. Performance assessment -> D:\\WORKSPACE\\PROJECTS\\school-lessons\\performance-assessments\\<level>\\<year>\\<term>\\<subject>\\
3. Exam specifications    -> D:\\WORKSPACE\\PROJECTS\\school-lessons\\exam-specifications\\<level>\\<year>\\<term>\\<subject>\\
4. baccalaureate_books    -> D:\\WORKSPACE\\PROJECTS\\school-lessons\\baccalaureate\\<category>\\<subject>\\
"""

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

DOWNLOADS_DIR = Path(r"C:\Users\mrt\Downloads")
PROJECT_DIR = Path(r"D:\WORKSPACE\PROJECTS\school-lessons")

STAGE_MAP = {
    "الابتدائية": "primary",
    "الإعدادية": "prep",
    "الثانوي العام": "high-school",
    "الثانوي الفني": "vocational",
    "البكالوريا": "baccalaureate",
    "البكالوريا المصرية": "baccalaureate",
    "رياض الأطفال": "kindergarten",
}

GRADE_MAP = {
    "مستوى أول": "kg-1",
    "مستوى ثان": "kg-2",
    "الصف الأول الابتدائي": "year-1",
    "الصف الثاني الابتدائي": "year-2",
    "الصف الثالث الابتدائي": "year-3",
    "الصف الرابع الابتدائي": "year-4",
    "الصف الخامس الابتدائي": "year-5",
    "الصف السادس الابتدائي": "year-6",
    "الصف الأول الإعدادي": "year-1",
    "الصف الثاني الإعدادي": "year-2",
    "الصف الثالث الإعدادي": "year-3",
    "الصف الأول الثانوي": "year-1",
    "الصف الثاني الثانوي": "year-2",
    "الصف الثالث الثانوي": "year-3",
    "الصف الأول الثانوي الفني": "year-1",
    "الصف الثاني الثانوي الفني": "year-2",
    "الصف الثاني": "year-2",
}

TERM_MAP = {
    "الفصل الدراسى الأول": "term-1",
    "الفصل الدراسى الثاني": "term-2",
    "الفصل الدراسى الأول والثاني": "full-year",
}


def sanitize_name(name: str) -> str:
    """Sanitize string for Windows filesystem."""
    clean = re.sub(r'[\\/:*?"<>|]', "-", name.strip())
    return clean.strip(" -.")


def clean_subject_name(subject: str) -> str:
    subj = subject.strip()
    if "اللغة اليابانية" in subj:
        return "اللغة اليابانية-لغة أجنبية ثانية"
    return sanitize_name(subj)


def process_kg(execute: bool = True) -> dict:
    """Process Kindergarten PDFs."""
    src_dir = DOWNLOADS_DIR / "kg"
    meta_path = PROJECT_DIR / "docs" / "kindergarten" / "kindergarten_books.json"
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    dest_base = PROJECT_DIR / "books" / "kindergarten"
    files_map = {p.name.lower(): p for p in src_dir.glob("*.pdf")}
    moved, missing = 0, []

    for item in meta:
        link_fname = Path(item["link"].split("?")[0]).name
        year = GRADE_MAP.get(item.get("grade", ""), "kg-1")
        term = TERM_MAP.get(item.get("term", ""), "term-1")
        subj = clean_subject_name(item.get("subject", "عام"))

        target_dir = dest_base / year / term / subj
        target_file = target_dir / link_fname

        if target_file.exists():
            moved += 1
            continue

        if link_fname.lower() in files_map:
            src_file = files_map[link_fname.lower()]
            if execute:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src_file), str(target_file))
            moved += 1
        else:
            missing.append(link_fname)

    return {"section": "kg", "total": len(meta), "placed": moved, "missing": missing}


def process_performance_assessment(execute: bool = True) -> dict:
    """Process Performance & Assessments PDFs."""
    src_dir = DOWNLOADS_DIR / "Performance assessment"
    meta_path = PROJECT_DIR / "docs" / "performance-assessments" / "performance_assessments.json"
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    dest_base = PROJECT_DIR / "performance-assessments"
    files_map = {p.name.lower(): p for p in src_dir.rglob("*.pdf")}
    moved, missing = 0, []

    for item in meta:
        link_fname = Path(item["link"].split("?")[0]).name
        stage = STAGE_MAP.get(item.get("stage", ""), "general")
        year = GRADE_MAP.get(item.get("grade", ""), "year-1")
        term = TERM_MAP.get(item.get("term", ""), "term-1")
        subj = clean_subject_name(item.get("subject", "عام"))

        target_dir = dest_base / stage / year / term / subj
        target_file = target_dir / link_fname

        if target_file.exists():
            moved += 1
            continue

        if link_fname.lower() in files_map:
            src_file = files_map[link_fname.lower()]
            if execute:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src_file), str(target_file))
                del files_map[link_fname.lower()]
            moved += 1
        else:
            missing.append(link_fname)

    return {"section": "performance-assessment", "total": len(meta), "placed": moved, "missing": len(missing)}


def process_exam_specifications(execute: bool = True) -> dict:
    """Process Exam Paper Specifications PDFs."""
    src_dir = DOWNLOADS_DIR / "Exam specifications"
    meta_path = PROJECT_DIR / "docs" / "exam-specifications" / "exam_specifications.json"
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    dest_base = PROJECT_DIR / "exam-specifications"
    files_map = {p.name.lower(): p for p in src_dir.rglob("*.pdf")}
    unique_links = set(Path(item["link"].split("?")[0]).name.lower() for item in meta)
    moved = 0
    missing = []

    # Map each item to its target folder
    for item in meta:
        link_fname = Path(item["link"].split("?")[0]).name
        stage = STAGE_MAP.get(item.get("stage", ""), "general")
        year = GRADE_MAP.get(item.get("grade", ""), "year-1")
        term = TERM_MAP.get(item.get("term", ""), "term-1")
        subj = clean_subject_name(item.get("subject", "عام"))

        target_dir = dest_base / stage / year / term / subj
        target_file = target_dir / link_fname

        if target_file.exists():
            moved += 1
            continue

        if link_fname.lower() in files_map:
            src_file = files_map[link_fname.lower()]
            if execute:
                target_dir.mkdir(parents=True, exist_ok=True)
                # Copy because one PDF file can be referenced across multiple grades/subjects
                shutil.copy2(str(src_file), str(target_file))
            moved += 1
        else:
            missing.append(link_fname)

    # After copying all references, remove source files if executing
    if execute and src_dir.exists():
        for p in list(src_dir.glob("*.pdf")):
            try:
                p.unlink()
            except Exception:
                pass

    return {"section": "exam-specifications", "total_records": len(meta), "unique_files": len(unique_links), "placed_records": moved, "missing": len(missing)}


def process_baccalaureate(execute: bool = True) -> dict:
    """Process Egyptian Baccalaureate PDFs."""
    src_dir = DOWNLOADS_DIR / "baccalaureate_books"
    meta_path = PROJECT_DIR / "docs" / "baccalaureate" / "baccalaureate_direct_pdfs.json"
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    dest_base = PROJECT_DIR / "baccalaureate"
    books_bacc_base = PROJECT_DIR / "books" / "baccalaureate"

    files_map = {p.name.lower(): p for p in src_dir.rglob("*.pdf")}
    moved, missing = 0, []

    for item in meta:
        link_fname = Path(item["link"].split("?")[0]).name
        category = sanitize_name(item.get("category", "عام"))
        subj = clean_subject_name(item.get("subject", "عام"))

        target_dir = dest_base / category / subj
        target_file = target_dir / link_fname
        books_target_dir = books_bacc_base / category / subj
        books_target_file = books_target_dir / link_fname

        if target_file.exists():
            moved += 1
            continue

        if link_fname.lower() in files_map:
            src_file = files_map[link_fname.lower()]
            if execute:
                target_dir.mkdir(parents=True, exist_ok=True)
                books_target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(src_file), str(target_file))
                shutil.move(str(src_file), str(books_target_file))
                del files_map[link_fname.lower()]
            moved += 1
        else:
            missing.append(link_fname)

    return {"section": "baccalaureate", "total": len(meta), "placed": moved, "missing": len(missing)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Arrange downloaded PDFs into project folders.")
    parser.add_argument("--section", choices=["kg", "performance-assessment", "exam-specifications", "baccalaureate", "all"], default="all")
    parser.add_argument("--check", action="store_true", help="Dry run check without moving")
    args = parser.parse_args()

    execute = not args.check
    results = {}

    if args.section in ("kg", "all"):
        results["kg"] = process_kg(execute)
    if args.section in ("performance-assessment", "all"):
        results["performance-assessment"] = process_performance_assessment(execute)
    if args.section in ("exam-specifications", "all"):
        results["exam-specifications"] = process_exam_specifications(execute)
    if args.section in ("baccalaureate", "all"):
        results["baccalaureate"] = process_baccalaureate(execute)

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
