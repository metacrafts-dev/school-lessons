"""Script to fetch, format, and document Performance & Assessments (الأداءات والتقييمات).

Source: https://ellibrary.moe.gov.eg/Performance_Assessments/books.json
Generates:
1. performance_assessments.json - Structured JSON database.
2. performance_assessments_links.txt - Direct links list (one URL per line).
3. performance_assessments.md - Comprehensive human-readable Markdown index with categorized tables.
"""

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import ssl
import sys
import urllib.request
from typing import Any, Dict, List

# Target output directory
OUTPUT_DIR = Path(r"D:\WORKSPACE\PROJECTS\school-lessons")
SOURCE_URL = "https://ellibrary.moe.gov.eg/Performance_Assessments/books.json"

STAGE_ORDER = {
    "الابتدائية": 1,
    "المرحلة الابتدائية": 1,
    "الإعدادية": 2,
    "المرحلة الإعدادية": 2,
    "الثانوي العام": 3,
    "مرحلة الثانوي العام": 3,
    "البكالوريا": 4,
    "مرحلة البكالوريا": 4,
}

GRADE_ORDER = {
    "الصف الأول الابتدائي": 1,
    "الصف الثاني الابتدائي": 2,
    "الصف الثالث الابتدائي": 3,
    "الصف الرابع الابتدائي": 4,
    "الصف الخامس الابتدائي": 5,
    "الصف السادس الابتدائي": 6,
    "الصف الأول الإعدادي": 11,
    "الصف الثاني الإعدادي": 12,
    "الصف الثالث الإعدادي": 13,
    "الصف الأول الثانوي": 21,
    "الصف الثاني الثانوي": 22,
    "الصف الثالث الثانوي": 23,
}


def get_type_sort_key(item_type: str) -> int:
    """Return an integer sort key for the assessment type."""
    if "كتاب" in item_type:
        return 0
    # Match week numbers like (1), (2), etc.
    match = re.search(r"\((\d+)\)", item_type)
    if match:
        return int(match.group(1))
    return 99


def fetch_source_data(url: str) -> List[Dict[str, Any]]:
    """Fetch JSON data from Ministry of Education portal."""
    print(f"Fetching data from {url}...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        },
    )

    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        content = resp.read().decode("utf-8")
        data = json.loads(content)
        print(f"Successfully fetched {len(data)} items.")
        return data


def clean_and_normalize(raw_items: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Clean strings, ensure all required fields exist, and validate data integrity."""
    cleaned = []
    required_fields = ["stage", "grade", "term", "subject", "type", "link"]

    for idx, item in enumerate(raw_items):
        clean_item = {
            "stage": str(item.get("stage", "")).strip(),
            "grade": str(item.get("grade", "")).strip(),
            "term": str(item.get("term", "")).strip(),
            "subject": str(item.get("subject", "")).strip(),
            "type": str(item.get("type", "")).strip(),
            "link": str(item.get("link", "")).strip(),
        }

        # Check for any missing field
        for field in required_fields:
            if not clean_item[field]:
                print(f"Warning: Item #{idx} has empty field '{field}': {clean_item}")

        cleaned.append(clean_item)

    # Sort logically: Stage -> Grade -> Subject -> Assessment Type
    cleaned.sort(
        key=lambda x: (
            STAGE_ORDER.get(x["stage"], 99),
            GRADE_ORDER.get(x["grade"], 99),
            x["subject"],
            get_type_sort_key(x["type"]),
        )
    )

    return cleaned


def generate_markdown(items: List[Dict[str, str]]) -> str:
    """Generate comprehensive human-readable Markdown index."""
    total_count = len(items)

    # Statistics
    stage_counts = Counter(x["stage"] for x in items)
    grade_counts = Counter(x["grade"] for x in items)
    type_counts = Counter(x["type"] for x in items)

    # Group by stage then grade
    grouped: Dict[str, Dict[str, List[Dict[str, str]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for x in items:
        grouped[x["stage"]][x["grade"]].append(x)

    md_lines = [
        "# فهرس الأداءات والتقييمات الصفية والأسبوعية لجميع المراحل الدراسية للعام الدراسي 2026-2027",
        "",
        "دليل روابط تحميل وفتح كتب الأداءات والتقييمات الصفية والمنزلية والواجبات الأسبوعية من المنصة الرسمية لوزارة التربية والتعليم والتعليم الفني في مصر.",
        "",
        f"- **المصدر:** [المكتبة الإلكترونية - وزارة التربية والتعليم](https://ellibrary.moe.gov.eg/Performance_Assessments/)",
        f"- **إجمالي عدد التقييمات والأداءات:** {total_count} مورد تعليمي",
        f"- **المرحلة الابتدائية:** {stage_counts.get('الابتدائية', 0)} مورد (الصفوف من 1 إلى 6)",
        f"- **المرحلة الإعدادية:** {stage_counts.get('الإعدادية', 0)} مورد (الصفوف من 1 إلى 3)",
        f"- **مرحلة الثانوي العام:** {stage_counts.get('الثانوي العام', 0)} مورد (الصفين 1 و 2)",
        f"- **مرحلة البكالوريا:** {stage_counts.get('البكالوريا', 0)} مورد (الصف الثاني الثانوي)",
        "",
        "---",
        "",
        "## ملخص المراحل والصفوف الدراسية",
        "",
        "| المرحلة الدراسية | الصف الدراسي | عدد الموارد والتقييمات | الفصول الدراسية المتاحة |",
        "| :--- | :--- | :---: | :--- |",
    ]

    # Populate summary table
    sorted_stages = sorted(grouped.keys(), key=lambda s: STAGE_ORDER.get(s, 99))
    for stage in sorted_stages:
        sorted_grades = sorted(
            grouped[stage].keys(), key=lambda g: GRADE_ORDER.get(g, 99)
        )
        for grade in sorted_grades:
            g_items = grouped[stage][grade]
            terms = ", ".join(sorted(set(i["term"] for i in g_items)))
            md_lines.append(f"| {stage} | {grade} | {len(g_items)} | {terms} |")

    md_lines.extend([
        "",
        "---",
        "",
        "## ملخص أنواع التقييمات والأداءات",
        "",
        "| نوع المورد | عدد الملفات المتاحة | الوصف |",
        "| :--- | :---: | :--- |",
    ])

    sorted_types = sorted(type_counts.keys(), key=get_type_sort_key)
    for t in sorted_types:
        count = type_counts[t]
        desc = "الكتاب الشامل للأداءات والتقييمات الفصلية" if "كتاب" in t else "المهام والتقييمات الأسبوعية والواجبات المنزلية"
        md_lines.append(f"| {t} | {count} | {desc} |")

    md_lines.extend(["", "---", ""])

    # Detailed tables by stage and grade
    stage_titles = {
        "الابتدائية": "المرحلة الابتدائية (Primary Stage)",
        "الإعدادية": "المرحلة الإعدادية (Preparatory Stage)",
        "الثانوي العام": "مرحلة الثانوي العام (Secondary Stage)",
        "البكالوريا": "مرحلة البكالوريا المصرية (Egyptian Baccalaureate)",
    }

    for stage_idx, stage in enumerate(sorted_stages, 1):
        st_title = stage_titles.get(stage, stage)
        st_count = stage_counts[stage]
        md_lines.extend([
            f"## {stage_idx}. {st_title} — ({st_count} مورد)",
            "",
        ])

        sorted_grades = sorted(
            grouped[stage].keys(), key=lambda g: GRADE_ORDER.get(g, 99)
        )
        for grade in sorted_grades:
            g_items = grouped[stage][grade]
            md_lines.extend([
                f"### {grade} ({len(g_items)} مورد)",
                "",
                "| # | المادة الدراسية | الفصل الدراسي | نوع التقييم / الأداء | رابط المورد المباشر |",
                "|---|-----------------|----------------|----------------------|----------------------|",
            ])

            for idx, item in enumerate(g_items, 1):
                subject = item["subject"]
                term = item["term"]
                item_type = item["type"]
                link = item["link"]
                link_text = f"[فتح / تحميل التقييم]({link})"
                md_lines.append(
                    f"| {idx} | {subject} | {term} | {item_type} | {link_text} |"
                )

            md_lines.append("")

    return "\n".join(md_lines)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    json_file = OUTPUT_DIR / "performance_assessments.json"
    md_file = OUTPUT_DIR / "performance_assessments.md"
    links_file = OUTPUT_DIR / "performance_assessments_links.txt"

    # 1. Fetch raw data
    raw_data = fetch_source_data(SOURCE_URL)

    # 2. Clean and format
    cleaned_items = clean_and_normalize(raw_data)
    total_count = len(cleaned_items)
    print(f"Total processed items: {total_count}")

    # 3. Write performance_assessments.json
    print(f"Writing {json_file}...")
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_items, f, indent=2, ensure_ascii=False)

    # 4. Write performance_assessments_links.txt
    print(f"Writing {links_file}...")
    with open(links_file, "w", encoding="utf-8") as f:
        for item in cleaned_items:
            f.write(item["link"] + "\n")

    # 5. Write performance_assessments.md
    print(f"Writing {md_file}...")
    markdown_content = generate_markdown(cleaned_items)
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    # 6. Verification
    print("Verifying generated files...")
    assert json_file.exists() and json_file.stat().st_size > 0, "JSON file missing or empty"
    assert links_file.exists() and links_file.stat().st_size > 0, "Links file missing or empty"
    assert md_file.exists() and md_file.stat().st_size > 0, "Markdown file missing or empty"

    with open(json_file, "r", encoding="utf-8") as f:
        verified_json = json.load(f)
    assert len(verified_json) == total_count, f"JSON item count mismatch: {len(verified_json)} vs {total_count}"

    with open(links_file, "r", encoding="utf-8") as f:
        links_lines = [line.strip() for line in f if line.strip()]
    assert len(links_lines) == total_count, f"Links count mismatch: {len(links_lines)} vs {total_count}"

    print(f"All verification checks passed successfully! Total items: {total_count}")


if __name__ == "__main__":
    main()
