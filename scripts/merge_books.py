"""Script to merge and format all school book links across Primary, Preparatory, and Secondary levels.

This script consolidates individual stage book records into:
- all_school_books.json: Complete structured JSON data.
- all_school_books_links.txt: Clean list of direct download links (one URL per line).
- all_school_books.md: Comprehensive, human-readable Markdown report with categorized tables.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"C:\Users\mrt")


def main() -> None:
    # 1. Load data from each school level
    primary_file = BASE_DIR / "primary_books.json"
    prep_file = BASE_DIR / "preparatory_books.json"
    sec_file = BASE_DIR / "high_school_books.json"

    with open(primary_file, "r", encoding="utf-8") as f:
        primary_books = json.load(f)

    with open(prep_file, "r", encoding="utf-8") as f:
        prep_books = json.load(f)

    with open(sec_file, "r", encoding="utf-8") as f:
        sec_books = json.load(f)

    all_books = primary_books + prep_books + sec_books
    print(f"Loaded books - Primary: {len(primary_books)}, Preparatory: {len(prep_books)}, Secondary: {len(sec_books)}")
    print(f"Total books combined: {len(all_books)}")

    # 2. Save consolidated JSON
    master_json = BASE_DIR / "all_school_books.json"
    with open(master_json, "w", encoding="utf-8") as f:
        json.dump(all_books, f, ensure_ascii=False, indent=2)

    # 3. Save plain links text file
    links_txt = BASE_DIR / "all_school_books_links.txt"
    with open(links_txt, "w", encoding="utf-8") as f:
        for book in all_books:
            f.write(book["link"].strip() + "\n")

    # 4. Generate formatted Markdown document
    stages = [
        ("المرحلة الابتدائية (Primary Stage)", primary_books),
        ("المرحلة الإعدادية (Preparatory Stage)", prep_books),
        ("مرحلة الثانوية العامة (Secondary / High School Stage)", sec_books),
    ]

    md_lines = [
        "# فهرس الكتب المدرسية لجميع المراحل الدراسية للعام الدراسي 2026-2027",
        "",
        "دليل روابط تحميل وفتح الكتب الدراسية لجميع المراحل التعليمية من المنصة الرسمية لوزارة التربية والتعليم والتعليم الفني في مصر.",
        "",
        f"- **إجمالي عدد الكتب والروابط:** {len(all_books)} كتاب ومورد تعليمي",
        f"- **المرحلة الابتدائية:** {len(primary_books)} كتاب (الصفوف من 1 إلى 6)",
        f"- **المرحلة الإعدادية:** {len(prep_books)} كتاب (الصفوف من 1 إلى 3)",
        f"- **مرحلة الثانوية العامة:** {len(sec_books)} كتاب (الصفوف من 1 إلى 3)",
        "",
        "---",
        "",
    ]

    for stage_name, books in stages:
        md_lines.append(f"## {stage_name} — ({len(books)} كتاب)")
        md_lines.append("")

        # Group by grade
        grades_dict = {}
        for item in books:
            g = item.get("grade", "عام")
            grades_dict.setdefault(g, []).append(item)

        for grade_name, grade_items in grades_dict.items():
            md_lines.append(f"### {grade_name} ({len(grade_items)} كتاب)")
            md_lines.append("")
            md_lines.append("| # | المادة الدراسية | الفصل الدراسي | نوع المحتوى | رابط الكتاب المباشر |")
            md_lines.append("|---|-----------------|----------------|-------------|---------------------|")

            for idx, book in enumerate(grade_items, 1):
                subject = book.get("subject", "").replace("|", "-")
                term = book.get("term", "").replace("|", "-")
                b_type = book.get("book_type", "").replace("|", "-")
                link = book.get("link", "").strip()
                md_lines.append(f"| {idx} | {subject} | {term} | {b_type} | [فتح / تحميل الكتاب]({link}) |")

            md_lines.append("")

    master_md = BASE_DIR / "all_school_books.md"
    with open(master_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    print(f"Generated {master_json.name} ({master_json.stat().st_size} bytes)")
    print(f"Generated {links_txt.name} ({links_txt.stat().st_size} bytes)")
    print(f"Generated {master_md.name} ({master_md.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
