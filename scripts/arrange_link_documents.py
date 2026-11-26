"""Script to arrange all link documents and catalogs into a structured directory hierarchy.

Hierarchy structure:
    docs / <level> / <year> / <term> / <subject> /
        ├── links.txt       (Clean list of download URLs, one per line)
        ├── links.md       (Formatted Markdown document containing links & descriptions)
        ├── data.json      (Structured JSON document containing links & metadata)
        ├── books_links.txt           (if textbooks present)
        ├── assessments_links.txt     (if weekly evaluations present)
        └── exam_specs_links.txt      (if exam blueprints present)

Also maintains category-specific trees under:
    docs / by-category / <category> / <level> / <year> / <term> / <subject> /
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(r"D:\WORKSPACE\PROJECTS\school-lessons")
DOCS_DIR = BASE_DIR / "docs"

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
    """Sanitize string for Windows directory/file naming."""
    clean = re.sub(r'[\\/:*?"<>|]', "-", name.strip())
    return clean.strip(" -.")


def clean_subject_name(subject: str) -> str:
    """Group specialized materials under clean subject names."""
    subj = subject.strip()
    if "اللغة اليابانية" in subj:
        return "اللغة اليابانية-لغة أجنبية ثانية"
    return sanitize_name(subj)


def determine_category(item: dict) -> str:
    """Categorize item into its primary educational domain."""
    b_type = item.get("type", "")
    stage = item.get("stage", "")

    if "رياض الأطفال" in stage:
        return "kindergarten"
    if "البكالوريا" in stage:
        return "baccalaureate"
    if "مواصفات" in b_type or "امتحانية" in b_type:
        return "exam-specifications"
    if "الأداءات" in b_type or "تقييم" in b_type or "تقييمات" in b_type:
        return "performance-assessments"
    return "school-books"


def write_subject_documents(folder: Path, items: list[dict], title: str) -> None:
    """Write links.txt, links.md, and data.json into a specific subject folder."""
    folder.mkdir(parents=True, exist_ok=True)

    # 1. Plain links.txt (clean, one URL per line)
    links = [item["link"].strip() for item in items if item.get("link")]
    # deduplicate preserving order
    unique_links = list(dict.fromkeys(links))
    with open(folder / "links.txt", "w", encoding="utf-8") as f:
        for link in unique_links:
            f.write(link + "\n")

    # 2. Structured data.json
    with open(folder / "data.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    # 3. Formatted links.md
    md_lines = [
        f"# {title}",
        "",
        f"- **إجمالي الموارد والملفات:** {len(items)}",
        f"- **إجمالي الروابط الفريدة:** {len(unique_links)}",
        "",
        "| # | عنوان المورد / المادة | النوع | الفصل الدراسي | رابط التحميل المباشر |",
        "|---|-----------------------|-------|---------------|-----------------------|",
    ]

    for idx, item in enumerate(items, 1):
        subj = item.get("subject", "").replace("|", "-")
        itype = item.get("type", "").replace("|", "-")
        term = item.get("term", "").replace("|", "-")
        link = item.get("link", "").strip()
        md_lines.append(f"| {idx} | {subj} | {itype} | {term} | [تحميل / فتح الملف]({link}) |")

    md_lines.append("")
    with open(folder / "links.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    # Also sub-links files if multiple categories exist in this subject
    cat_groups = {}
    for item in items:
        cat = determine_category(item)
        cat_groups.setdefault(cat, []).append(item)

    if len(cat_groups) > 1:
        for cat, cat_items in cat_groups.items():
            cat_links = list(dict.fromkeys(i["link"].strip() for i in cat_items if i.get("link")))
            with open(folder / f"{cat}_links.txt", "w", encoding="utf-8") as f:
                for l in cat_links:
                    f.write(l + "\n")


def main() -> None:
    json_path = BASE_DIR / "all_portal_resources.json"
    with open(json_path, "r", encoding="utf-8") as f:
        resources = json.load(f)

    print(f"Total resources to organize into link documents: {len(resources)}")

    # Grouping by:
    # 1. Unified hierarchy: (stage_en, grade_en, term_en, subject_clean)
    # 2. Category hierarchy: (category, stage_en, grade_en, term_en, subject_clean)
    unified_tree = {}
    category_tree = {}

    for r in resources:
        stage_en = STAGE_MAP.get(r.get("stage", ""), "general")
        grade_en = GRADE_MAP.get(r.get("grade", ""), "general")
        term_en = TERM_MAP.get(r.get("term", ""), "term-1")
        subj_clean = clean_subject_name(r.get("subject", "عام"))
        cat = determine_category(r)

        key_unified = (stage_en, grade_en, term_en, subj_clean)
        unified_tree.setdefault(key_unified, []).append(r)

        key_cat = (cat, stage_en, grade_en, term_en, subj_clean)
        category_tree.setdefault(key_cat, []).append(r)

    print(f"Total unified subject folders to create: {len(unified_tree)}")
    print(f"Total category subject folders to create: {len(category_tree)}")

    # 1. Create Unified Hierarchy under docs/
    for (stg, grd, trm, subj), items in unified_tree.items():
        folder = DOCS_DIR / stg / grd / trm / subj
        title = f"{subj} — {items[0].get('grade', '')} ({items[0].get('stage', '')})"
        write_subject_documents(folder, items, title)

    # 2. Create Category Hierarchy under docs/by-category/
    for (cat, stg, grd, trm, subj), items in category_tree.items():
        folder = DOCS_DIR / "by-category" / cat / stg / grd / trm / subj
        title = f"[{cat}] {subj} — {items[0].get('grade', '')} ({items[0].get('stage', '')})"
        write_subject_documents(folder, items, title)

    # 3. Create level-level and grade-level summary documents in docs/
    stages_set = set(k[0] for k in unified_tree.keys())
    for stg in stages_set:
        stg_items = [r for r in resources if STAGE_MAP.get(r.get("stage", "")) == stg]
        stg_links = list(dict.fromkeys(r["link"].strip() for r in stg_items if r.get("link")))
        stg_folder = DOCS_DIR / stg
        with open(stg_folder / "links.txt", "w", encoding="utf-8") as f:
            for l in stg_links:
                f.write(l + "\n")

    # Master index in docs/README.md
    with open(DOCS_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write("# دليل وثائق وروابط المكتبة الإلكترونية المنظمة في مجلدات\n\n")
        f.write(f"- إجمالي الموارد: {len(resources)}\n")
        f.write(f"- إجمالي مجلدات المواد المُنظمة: {len(unified_tree)}\n\n")
        f.write("## الأقسام والمراحل التعليمية:\n")
        for stg in sorted(stages_set):
            count = len([r for r in resources if STAGE_MAP.get(r.get("stage", "")) == stg])
            f.write(f"- **[{stg}](./{stg}/)**: {count} مورد تعليمي\n")

    print("\nSuccessfully organized all link documents into folders!")


if __name__ == "__main__":
    main()
