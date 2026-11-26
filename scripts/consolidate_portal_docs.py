"""Consolidate all educational resources from the Egyptian Ministry of Education portal.

This script aggregates data from all explored domains:
1. School Books (Primary, Preparatory, Secondary)
2. Kindergarten (KG1, KG2)
3. Egyptian Baccalaureate (Core, Specialized, Activities)
4. Performance & Assessments (التقييمات والأداءات الصفية والمنزلية)
5. Exam Paper Specifications (مواصفات الورقة الامتحانية)

It generates:
- all_portal_resources.json: Complete unified JSON database.
- all_portal_resources.md: Comprehensive markdown catalog.
- all_portal_download_links.txt: Clean list of all URLs for downloaders.
And arranges all individual category documents into structured folders under docs/.
"""

import json
import shutil
from pathlib import Path

BASE_DIR = Path(r"D:\WORKSPACE\PROJECTS\school-lessons")
DOCS_DIR = BASE_DIR / "docs"


def load_json_file(filename: str) -> list[dict]:
    """Load JSON file from base directory."""
    path = BASE_DIR / filename
    if not path.exists():
        print(f"Warning: {filename} does not exist.")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    # 1. Load all datasets
    school_books = load_json_file("all_school_books.json")
    kg_books = load_json_file("kindergarten_books.json")
    bacc_items = load_json_file("baccalaureate_books.json")
    bacc_direct = load_json_file("baccalaureate_direct_pdfs.json")
    assessments = load_json_file("performance_assessments.json")
    exam_specs = load_json_file("exam_specifications.json")

    print(f"Loaded records:")
    print(f"  - School Books (Primary, Prep, Sec): {len(school_books)}")
    print(f"  - Kindergarten Books: {len(kg_books)}")
    print(f"  - Egyptian Baccalaureate (tracks): {len(bacc_items)}")
    print(f"  - Egyptian Baccalaureate (direct PDFs): {len(bacc_direct)}")
    print(f"  - Performance & Assessments: {len(assessments)}")
    print(f"  - Exam Paper Specifications: {len(exam_specs)}")

    # Prefer direct PDF items for Baccalaureate in the consolidated download list if available
    bacc_to_merge = bacc_direct if bacc_direct else bacc_items
    all_resources = school_books + kg_books + bacc_to_merge + assessments + exam_specs

    # 2. Extract and deduplicate download links
    all_links = []
    seen = set()
    for item in all_resources:
        link = item.get("link", "").strip()
        if link and link.startswith("http") and link not in seen:
            seen.add(link)
            all_links.append(link)

    print(f"Total unique download links across all sections: {len(all_links)}")

    # 3. Write Master Consolidated JSON
    master_json = BASE_DIR / "all_portal_resources.json"
    with open(master_json, "w", encoding="utf-8") as f:
        json.dump(all_resources, f, ensure_ascii=False, indent=2)

    # 4. Write Master Download Links File (one URL per line, only links)
    master_links = BASE_DIR / "all_portal_download_links.txt"
    with open(master_links, "w", encoding="utf-8") as f:
        for link in all_links:
            f.write(link + "\n")

    # 5. Write Master Consolidated Markdown Catalog
    md_lines = [
        "# فهرس الموارد التعليمية الشامل — بوابة المكتبة الإلكترونية لوزارة التربية والتعليم 2026-2027",
        "",
        "دليل روابط وتحميل جميع المناهج والموارد التعليمية من المنصة الرسمية لوزارة التربية والتعليم والتعليم الفني في مصر.",
        "",
        "## 📊 ملخص الإحصائيات والأقسام المكتملة",
        "",
        f"- **إجمالي الموارد والملفات:** {len(all_resources)} مورد",
        f"- **إجمالي الروابط الفريدة القابلة للتحميل:** {len(all_links)} رابط مباشر",
        f"- **الكتب الدراسية (الابتدائية والإعدادية والثانوية العامة):** {len(school_books)} كتاب",
        f"- **كتب رياض الأطفال (KG1 & KG2):** {len(kg_books)} كتب",
        f"- **البكالوريا المصرية (المسارات والكتب والتقييمات):** {len(bacc_to_merge)} مورد تعليمي",
        f"- **الأداءات والتقييمات الأسبوعية والصفية:** {len(assessments)} تقييم وكراسة أداء",
        f"- **مواصفات الورقة الامتحانية والنماذج الاسترشادية:** {len(exam_specs)} مواصفة ونموذج",
        "",
        "---",
        "",
        "## 🗂️ فهرس الأقسام الرئيسية والوثائق التفصيلية",
        "",
        "| القسم | عدد الروابط | ملف البيانات (JSON) | الدليل المفصل (Markdown) | روابط التحميل المباشرة |",
        "| :--- | :---: | :--- | :--- | :--- |",
        f"| **الكتب الدراسية (المراحل الثلاث)** | {len(school_books)} | `docs/school-books/all_school_books.json` | `docs/school-books/all_school_books.md` | `docs/school-books/all_school_books_links.txt` |",
        f"| **رياض الأطفال (KG)** | {len(kg_books)} | `docs/kindergarten/kindergarten_books.json` | `docs/kindergarten/kindergarten_books.md` | `docs/kindergarten/kindergarten_links.txt` |",
        f"| **البكالوريا المصرية** | {len(bacc_to_merge)} | `docs/baccalaureate/baccalaureate_books.json` | `docs/baccalaureate/baccalaureate_books.md` | `docs/baccalaureate/baccalaureate_links.txt` |",
        f"| **الأداءات والتقييمات الصفية** | {len(assessments)} | `docs/performance-assessments/performance_assessments.json` | `docs/performance-assessments/performance_assessments.md` | `docs/performance-assessments/performance_assessments_links.txt` |",
        f"| **مواصفات الورقة الامتحانية** | {len(exam_specs)} | `docs/exam-specifications/exam_specifications.json` | `docs/exam-specifications/exam_specifications.md` | `docs/exam-specifications/exam_specifications_links.txt` |",
        "",
        "---",
        "",
    ]

    master_md = BASE_DIR / "all_portal_resources.md"
    with open(master_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    # 6. Organize docs into categorized folders
    category_mappings = {
        "school-books": [
            "all_school_books.json",
            "all_school_books.md",
            "all_school_books_links.txt",
            "primary_books.json",
            "primary_books.md",
            "preparatory_books.json",
            "preparatory_books.md",
            "high_school_books.json",
            "high_school_books.md",
        ],
        "kindergarten": [
            "kindergarten_books.json",
            "kindergarten_books.md",
            "kindergarten_links.txt",
        ],
        "baccalaureate": [
            "baccalaureate_books.json",
            "baccalaureate_books.md",
            "baccalaureate_links.txt",
            "baccalaureate_items.json",
            "baccalaureate_direct_pdfs.json",
            "baccalaureate_direct_pdfs.txt",
        ],
        "performance-assessments": [
            "performance_assessments.json",
            "performance_assessments.md",
            "performance_assessments_links.txt",
        ],
        "exam-specifications": [
            "exam_specifications.json",
            "exam_specifications.md",
            "exam_specifications_links.txt",
        ],
    }

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    for cat_name, file_list in category_mappings.items():
        cat_dir = DOCS_DIR / cat_name
        cat_dir.mkdir(parents=True, exist_ok=True)
        for fname in file_list:
            src = BASE_DIR / fname
            if src.exists():
                dst = cat_dir / fname
                shutil.copy2(src, dst)
                print(f"Copied {fname} -> docs/{cat_name}/")

    print("\nMaster consolidation and document organization completed successfully.")


if __name__ == "__main__":
    main()
