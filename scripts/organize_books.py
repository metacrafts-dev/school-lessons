"""Organize downloaded Egyptian school books into a structured directory hierarchy.

Hierarchy structure:
    books / <level> / <year> / <term> / <subject> / <book_files>

Levels:
    - primary      (year-1 to year-6)
    - prep         (year-1 to year-3)
    - high-school  (year-1 to year-3)
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

# Paths
BASE_PROJECT_DIR = Path(r"D:\WORKSPACE\PROJECTS\school-lessons")
SOURCE_DOWNLOADS_DIR = Path(r"C:\Users\mrt\Downloads\school-books")
BOOKS_DEST_DIR = BASE_PROJECT_DIR / "books"
METADATA_JSON_PATH = BASE_PROJECT_DIR / "all_school_books.json"

STAGE_MAP = {
    "الابتدائية": "primary",
    "الإعدادية": "prep",
    "الثانوي العام": "high-school",
}

GRADE_MAP = {
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
}

TERM_MAP = {
    "الفصل الدراسى الأول": "term-1",
}


def sanitize_folder_name(name: str) -> str:
    """Sanitize subject name to be safe for Windows file paths."""
    invalid_chars = [":", "*", "?", '"', "<", ">", "|", "\\", "/"]
    sanitized = name.strip()
    for ch in invalid_chars:
        sanitized = sanitized.replace(ch, "-")
    return sanitized.strip()


def clean_subject_name(subject: str) -> str:
    """Group specialized materials under clean subject folder names."""
    subj = subject.strip()
    if "اللغة اليابانية" in subj:
        return "اللغة اليابانية-لغة أجنبية ثانية"
    return sanitize_folder_name(subj)


def load_metadata() -> list[dict]:
    """Load metadata list from JSON."""
    if not METADATA_JSON_PATH.exists():
        raise FileNotFoundError(f"Metadata file not found: {METADATA_JSON_PATH}")
    with open(METADATA_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_source_file_index() -> dict[str, Path]:
    """Build a lookup dictionary of all files in the downloads directory."""
    index = {}
    if not SOURCE_DOWNLOADS_DIR.exists():
        return index

    for root, _, files in os.walk(SOURCE_DOWNLOADS_DIR):
        for file in files:
            p = Path(root) / file
            index[file.lower()] = p
    return index


def organize_stage(stage_target: str, execute: bool = True) -> dict:
    """Organize books belonging to a specific stage.
    
    stage_target can be 'primary', 'prep', 'high-school', or 'all'.
    """
    books = load_metadata()
    file_index = build_source_file_index()

    # Filter books for this stage
    selected_books = []
    for b in books:
        stage_en = STAGE_MAP.get(b.get("stage", ""))
        if stage_target == "all" or stage_en == stage_target:
            selected_books.append(b)

    results = {
        "stage": stage_target,
        "total_expected": len(selected_books),
        "moved": 0,
        "already_placed": 0,
        "missing": [],
    }

    for b in selected_books:
        stage_en = STAGE_MAP[b["stage"]]
        year_en = GRADE_MAP[b["grade"]]
        term_en = TERM_MAP.get(b["term"], "term-1")
        subj_folder = clean_subject_name(b["subject"])

        target_dir = BOOKS_DEST_DIR / stage_en / year_en / term_en / subj_folder

        link = b["link"]
        expected_filename = Path(link.split("?")[0]).name
        expected_filename_lower = expected_filename.lower()

        target_file_path = target_dir / expected_filename

        # Check if already in target location
        if target_file_path.exists():
            results["already_placed"] += 1
            continue

        # Look for file in downloads
        if expected_filename_lower in file_index:
            src_path = file_index[expected_filename_lower]
            if execute:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src_path), str(target_file_path))
                # Update file index to reflect move
                del file_index[expected_filename_lower]
            results["moved"] += 1
        else:
            # Check if file was already placed in another stage/grade (e.g., shared textbook like Arabic grammar)
            existing_copy = None
            if BOOKS_DEST_DIR.exists():
                for root, _, files in os.walk(BOOKS_DEST_DIR):
                    for f in files:
                        if f.lower() == expected_filename_lower:
                            existing_copy = Path(root) / f
                            break
                    if existing_copy:
                        break

            if existing_copy:
                if execute:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(str(existing_copy), str(target_file_path))
                results["moved"] += 1
            else:
                results["missing"].append({
                    "filename": expected_filename,
                    "subject": b["subject"],
                    "grade": b["grade"],
                })

    # Also handle extracted Japanese audio and video folders if organizing prep
    if stage_target in ("prep", "all") and execute:
        japanese_folder = BOOKS_DEST_DIR / "prep" / "year-1" / "term-1" / "اللغة اليابانية-لغة أجنبية ثانية"
        japanese_folder.mkdir(parents=True, exist_ok=True)
        for extra_name in ["EJS_G7_audio", "G7_Can_d0"]:
            extra_src = SOURCE_DOWNLOADS_DIR / extra_name
            extra_dst = japanese_folder / extra_name
            if extra_src.exists() and not extra_dst.exists():
                shutil.move(str(extra_src), str(extra_dst))

        # Also check if existing loose test file English_Prep1_T1.pdf is in prep/year-1/T1
        old_test_file = BOOKS_DEST_DIR / "prep" / "year-1" / "T1" / "English_Prep1_T1.pdf"
        target_english = BOOKS_DEST_DIR / "prep" / "year-1" / "term-1" / "اللغة الإنجليزية-لغة أجنبية أولى" / "English_Prep1_T1.pdf"
        if old_test_file.exists():
            if not target_english.exists():
                target_english.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(old_test_file), str(target_english))
            else:
                old_test_file.unlink()

        # Clean up empty T1 and T2 folders in prep/year-1 if they exist and are empty
        for old_dir_name in ["T1", "T2"]:
            old_dir = BOOKS_DEST_DIR / "prep" / "year-1" / old_dir_name
            if old_dir.exists() and not any(old_dir.iterdir()):
                old_dir.rmdir()

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize school books into categorized folders.")
    parser.add_argument(
        "--stage",
        choices=["primary", "prep", "high-school", "all"],
        default="all",
        help="School level to organize",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check matching without moving files",
    )
    args = parser.parse_args()

    results = organize_stage(args.stage, execute=not args.check)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
