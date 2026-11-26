"""Script to fetch, format, and organize Exam Paper Specifications (مواصفات الورقة الامتحانية).

Source: https://ellibrary.moe.gov.eg/ExamPaperSpecifications/books.json
Target files:
- D:\WORKSPACE\PROJECTS\school-lessons\exam_specifications.json
- D:\WORKSPACE\PROJECTS\school-lessons\exam_specifications.md
- D:\WORKSPACE\PROJECTS\school-lessons\exam_specifications_links.txt
"""

import json
import os
import ssl
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

OUT_DIR = Path(r"D:\WORKSPACE\PROJECTS\school-lessons")
URL = "https://ellibrary.moe.gov.eg/ExamPaperSpecifications/books.json"


def fetch_exam_specs():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
        },
    )
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    print(f"Fetching data from {URL} ...")
    raw_data = fetch_exam_specs()
    total_raw = len(raw_data)
    print(f"Fetched {total_raw} raw items.")

    formatted_items = []
    for item in raw_data:
        formatted_items.append(
            {
                "stage": str(item.get("stage", "")).strip(),
                "grade": str(item.get("grade", "")).strip(),
                "term": str(item.get("term", "")).strip(),
                "subject": str(item.get("subject", "")).strip(),
                "type": str(item.get("type", "")).strip(),
                "link": str(item.get("link", "")).strip(),
            }
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = OUT_DIR / "exam_specifications.json"
    md_path = OUT_DIR / "exam_specifications.md"
    links_path = OUT_DIR / "exam_specifications_links.txt"

    # 1. Save JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(formatted_items, f, ensure_ascii=False, indent=2)
    print(f"Saved JSON to {json_path} ({len(formatted_items)} items, {os.path.getsize(json_path)} bytes)")

    # 2. Save plain links list
    with open(links_path, "w", encoding="utf-8") as f:
        for item in formatted_items:
            f.write(item["link"] + "\n")
    print(f"Saved Links to {links_path} ({len(formatted_items)} lines, {os.path.getsize(links_path)} bytes)")

    # 3. Build Markdown Report
    unique_links = len(set(it["link"] for it in formatted_items))
    stage_counts = Counter(it["stage"] for it in formatted_items)
    type_counts = Counter(it["type"] for it in formatted_items)

    stage_order = ["الابتدائية", "الإعدادية", "الثانوي العام", "الثانوي الفني"]
    grade_order = [
        "الصف الأول الابتدائي",
        "الصف الثاني الابتدائي",
        "الصف الثالث الابتدائي",
        "الصف الرابع الابتدائي",
        "الصف الخامس الابتدائي",
        "الصف السادس الابتدائي",
        "الصف الأول الإعدادي",
        "الصف الثاني الإعدادي",
        "الصف الثالث الإعدادي",
        "الصف الأول الثانوي",
        "الصف الثاني الثانوي",
        "الصف الثالث الثانوي",
    ]

    stage_map = defaultdict(lambda: defaultdict(list))
    for it in formatted_items:
        stage_map[it["stage"]][it["grade"]].append(it)

    md = [
        "# مواصفات الورقة الامتحانية لجميع المراحل الدراسية للعام الدراسي 2026-2027",
        "",
        "دليل شامل لجميع مواصفات الورقة الامتحانية لمختلف المراحل التعليمية (الابتدائية، الإعدادية، الثانوي العام، الثانوي الفني) والمسارات المتخصصة (التعليم العام، الدمج التعليمي، أبناؤنا في الخارج، المكفوفين، الصم وضعاف السمع، المسار المصري، الإعدادي المهني).",
        "",
        "**المصدر الرسمي:** وزارة التربية والتعليم والتعليم الفني - [المكتبة الإلكترونية - مواصفات الورقة الامتحانية](https://ellibrary.moe.gov.eg/ExamPaperSpecifications/)  ",
        f"**إجمالي عدد بنود المواصفات الامتحانية:** {len(formatted_items)} بنداً  ",
        f"**إجمالي الروابط والملفات الفريدة (Unique PDF Documents):** {unique_links} ملفاً  ",
        "**الفصل الدراسي:** الفصل الدراسى الأول  ",
        "",
        "---",
        "",
        "## ملخص المراحل والصفوف الدراسية",
        "",
        "| المرحلة | الصف الدراسي | عدد المواصفات | الفئات والمسارات المشمولة |",
        "| :--- | :--- | :---: | :--- |",
    ]

    for st in stage_order:
        if st in stage_map:
            for gr in grade_order:
                if gr in stage_map[st]:
                    items = stage_map[st][gr]
                    gr_types = sorted(list(set(it["type"] for it in items)))
                    types_summary = "، ".join(t.replace("مواصفات الورقة الامتحانية", "").strip(" ()") or "عام" for t in gr_types)
                    md.append(f"| {st} | {gr} | {len(items)} | {types_summary} |")

    md.extend(
        [
            "",
            "### إحصائيات المراحل التعليمية",
            "",
            "| المرحلة التعليمية | إجمالي البنود | النسبة المئوية |",
            "| :--- | :---: | :---: |",
        ]
    )
    for st in stage_order:
        if st in stage_counts:
            cnt = stage_counts[st]
            pct = (cnt / len(formatted_items)) * 100
            md.append(f"| المرحلة {st} | {cnt} | {pct:.1f}% |")

    md.extend(
        [
            "",
            "### توزيع المواصفات حسب نوع الفئة المستهدفة",
            "",
            "| الفئة / نوع المواصفة الامتحانية | عدد البنود |",
            "| :--- | :---: |",
        ]
    )
    for tp, cnt in type_counts.most_common():
        md.append(f"| {tp} | {cnt} |")

    md.extend(
        [
            "",
            "---",
            "",
        ]
    )

    # Detailed tables by stage and grade
    for st in stage_order:
        if st not in stage_map:
            continue
        st_items_count = sum(len(items) for items in stage_map[st].values())
        md.append(f"## المرحلة {st}")
        md.append(f"**إجمالي مواصفات المرحلة:** {st_items_count} بنداً")
        md.append("")

        for gr in grade_order:
            if gr not in stage_map[st]:
                continue
            items = stage_map[st][gr]
            md.append(f"### {gr} - المرحلة {st}")
            md.append(f"**عدد المواصفات المتاحة:** {len(items)}")
            md.append("")
            md.append("| # | المادة | نوع المواصفة (الفئة) | الفصل الدراسي | رابط التحميل |")
            md.append("| :-: | :--- | :--- | :--- | :--- |")

            for idx, it in enumerate(items, 1):
                clean_subj = it["subject"]
                clean_type = it["type"]
                clean_term = it["term"]
                link_url = it["link"]
                md.append(f"| {idx} | {clean_subj} | {clean_type} | {clean_term} | [تحميل PDF]({link_url}) |")
            md.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"Saved Markdown to {md_path} ({os.path.getsize(md_path)} bytes)")

    # 4. Verification
    print("\n--- Running Verification ---")
    with open(json_path, "r", encoding="utf-8") as f:
        loaded_json = json.load(f)
    assert len(loaded_json) == 597, f"Expected 597 items in json, got {len(loaded_json)}"

    with open(links_path, "r", encoding="utf-8") as f:
        loaded_links = [line.strip() for line in f if line.strip()]
    assert len(loaded_links) == 597, f"Expected 597 links, got {len(loaded_links)}"

    assert os.path.exists(md_path) and os.path.getsize(md_path) > 1000, "Markdown file missing or too small"

    # Check each item has all expected fields
    expected_fields = {"stage", "grade", "term", "subject", "type", "link"}
    for idx, item in enumerate(loaded_json):
        assert set(item.keys()) == expected_fields, f"Item {idx} keys mismatch: {item.keys()}"
        for k in expected_fields:
            assert item[k], f"Item {idx} has empty field {k}"

    print("All verification checks PASSED successfully!")
    print(f"Total Exam Paper Specifications processed: {len(loaded_json)}")


if __name__ == "__main__":
    main()
