import json
import urllib.parse
import urllib.request
import ssl
import re
from pathlib import Path

SOURCE_FILE = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_items.json")
OUT_JSON = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_books.json")
OUT_MD = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_books.md")
OUT_TXT = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_links.txt")

OUT_DEEP_JSON = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_direct_pdfs.json")
OUT_DEEP_TXT = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_direct_pdfs.txt")

with open(SOURCE_FILE, "r", encoding="utf-8") as f:
    raw_items = json.load(f)

print(f"Loaded {len(raw_items)} raw items from {SOURCE_FILE.name}")

# Standardize the 19 main items
formatted_items = []

for idx, item in enumerate(raw_items, 1):
    stage = item.get("stage", "البكالوريا المصرية").strip()
    grade = item.get("grade", "الصف الثاني الثانوي").strip()
    category = item.get("category", "").strip()
    subject_raw = item.get("subject", "").strip()
    type_raw = item.get("type", "").strip()
    desc = item.get("description", "").strip()
    link = item.get("link", "").strip()

    if "الجزء الأول - الثاني" in type_raw or "الجزء الأول - الثاني" in desc:
        term = "الفصل الدراسى الأول والثاني"
    elif "الجزء الأول" in type_raw or "part1" in link.lower() or "Assessments-1" in link:
        term = "الفصل الدراسى الأول"
    elif "الجزء الثاني" in type_raw or "part2" in link.lower():
        term = "الفصل الدراسى الثاني"
    elif "القصة" in type_raw or "Story" in link:
        term = "الفصل الدراسى الأول والثاني"
    else:
        term = "الفصل الدراسى الأول والثاني"

    subject_display = subject_raw
    type_display = type_raw

    if category == "المواد التخصصية لكل مسار":
        subject_display = f"مسار {subject_raw} - {type_raw}"
        type_display = "حزمة الكتب والتقييمات التخصصية"
    elif category == "المواد الأساسية لجميع المسارات":
        if "اللغة الأجنبية الأولى" in subject_raw:
            subject_display = type_raw
            type_display = "حزمة كتب وتقييمات اللغة"
    elif category == "الأنشطة":
        subject_display = f"الأنشطة - {subject_raw} ({'عربي' if 'العربية' in desc else 'إنجليزي'})"
        type_display = "كتاب الطالب (الجزء الأول والثاني)"

    entry = {
        "stage": stage,
        "grade": grade,
        "term": term,
        "category": category,
        "subject": subject_display,
        "type": type_display,
        "book_type": type_display,
        "description": desc,
        "link": link
    }
    formatted_items.append(entry)

# 1. Save JSON (19 items)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(formatted_items, f, ensure_ascii=False, indent=2)
print(f"Saved JSON -> {OUT_JSON} ({OUT_JSON.stat().st_size} bytes)")

# 2. Save Links TXT (19 links)
with open(OUT_TXT, "w", encoding="utf-8") as f:
    for item in formatted_items:
        f.write(item["link"] + "\n")
print(f"Saved Links TXT -> {OUT_TXT} ({OUT_TXT.stat().st_size} bytes)")

# 3. Crawl Deep direct PDFs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_cards(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        html = urllib.request.urlopen(req, context=ctx, timeout=8).read().decode('utf-8', errors='ignore')
    except Exception:
        return []
    cards = []
    for line in html.splitlines():
        line = line.strip()
        if line.startswith('//') or line.startswith('/*') or line.startswith('*'):
            continue
        m = re.search(r'title:\s*["\']([^"\']+)["\'],\s*text:\s*["\']([^"\']+)["\'],\s*link:\s*["\']([^"\']+)["\']', line)
        if m:
            cards.append((m.group(1).replace('🎓','').strip(), m.group(2).strip(), m.group(3).strip()))
    return cards

def crawl_all(url, path=None):
    if path is None:
        path = []
    cards = get_cards(url)
    results = []
    for title, desc, link in cards:
        full = urllib.parse.urljoin(url, link)
        if full.endswith('.pdf'):
            results.append((path + [title], desc, full))
        elif full.endswith('/') and full != url:
            sub = crawl_all(full, path + [title])
            if sub:
                results.extend(sub)
            else:
                results.append((path + [title], desc, full))
        else:
            results.append((path + [title], desc, full))
    return results

deep_results = crawl_all('https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/')
print(f"Deep crawl found {len(deep_results)} items.")

deep_pdf_items = []
for p, d, link in deep_results:
    if not link.endswith('.pdf'):
        continue
    full_path_str = " -> ".join(p)
    term = "الفصل الدراسى الأول"
    if "الجزء الثاني" in full_path_str or "part2" in link.lower():
        term = "الفصل الدراسى الثاني"
    elif "القصة" in full_path_str or "Story" in link or "الجزء الأول - الثاني" in full_path_str:
        term = "الفصل الدراسى الأول والثاني"

    subject = p[1] if len(p) > 1 else "عام"
    if len(p) > 2 and p[1] in ["اللغة الأجنبية الأولى", "الطب وعلوم الحياة", "الهندسة وعلوم الحاسب", "الأعمال", "الأداب والفنون"]:
        subject = f"{p[1]} - {p[2]}"
        if len(p) > 3 and "اللغات الأجنبية الثانية" in p[2]:
            subject = f"{p[1]} - {p[2]} ({p[3]})"
    
    btype = p[-1]
    deep_pdf_items.append({
        "stage": "البكالوريا المصرية",
        "grade": "الصف الثاني الثانوي",
        "term": term,
        "track": p[0],
        "subject": subject,
        "type": btype,
        "link": link
    })

# Save deep JSON & TXT
with open(OUT_DEEP_JSON, "w", encoding="utf-8") as f:
    json.dump(deep_pdf_items, f, ensure_ascii=False, indent=2)
print(f"Saved Deep JSON -> {OUT_DEEP_JSON} ({len(deep_pdf_items)} items)")

with open(OUT_DEEP_TXT, "w", encoding="utf-8") as f:
    for it in deep_pdf_items:
        f.write(it["link"] + "\n")
print(f"Saved Deep Links TXT -> {OUT_DEEP_TXT} ({len(deep_pdf_items)} lines)")

# 4. Generate Markdown
core_rows = []
spec_rows = []
act_rows = []

for item in formatted_items:
    cat = item["category"]
    subj = item["subject"]
    term = item["term"]
    btype = item["type"]
    link = item["link"]

    if "المواد الأساسية" in cat:
        core_rows.append(f"| {len(core_rows)+1} | {subj} | {term} | {btype} | [فتح / تحميل المحتوى]({link}) |")
    elif "المواد التخصصية" in cat:
        spec_rows.append(f"| {len(spec_rows)+1} | {subj} | {term} | {btype} | [فتح / تحميل المحتوى]({link}) |")
    else:
        act_rows.append(f"| {len(act_rows)+1} | {subj} | {term} | {btype} | [فتح / تحميل المحتوى]({link}) |")

md_lines = [
    "# كتب ومصادر البكالوريا المصرية (Egyptian Baccalaureate)",
    "",
    "**المصدر:** وزارة التربية والتعليم والتعليم الفني - [بوابة البكالوريا المصرية الرسمية](https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/)",
    f"**إجمالي عدد المواد والمصادر المنظمة:** {len(formatted_items)} مادة ومصدر تعليمي",
    f"**إجمالي الكتب والتقييمات المباشرة (Direct PDFs):** {len(deep_pdf_items)} ملف PDF مباشر",
    "**المرحلة الدراسية:** البكالوريا المصرية (الصف الثاني الثانوي)",
    "**العام الدراسي:** 2026-2027",
    "",
    "---",
    "",
    "## فهرس الأقسام والمسارات التعليمية",
    "",
    "1. [المواد الأساسية لجميع المسارات (Core Subjects)](#1-المواد-الأساسية-لجميع-المسارات-core-subjects)",
    "2. [المواد التخصصية لكل مسار (Specialized Tracks)](#2-المواد-التخصصية-لكل-مسار-specialized-tracks)",
    "3. [الأنشطة التعليمية - الثقافة المالية (Financial Literacy)](#3-الأنشطة-التعليمية---الثقافة-المالية-financial-literacy)",
    "4. [ملحق روابط التحميل المباشرة لجميع الكتب والتقييمات (Direct PDF Downloads)](#4-ملحق-روابط-التحميل-المباشرة-لجميع-الكتب-والتقييمات-77-ملف-pdf)",
    "",
    "---",
    "",
    "## 1. المواد الأساسية لجميع المسارات (Core Subjects)",
    "",
    "تشمل اللغة العربية، التاريخ الوطني والمصري، واللغات الأجنبية الأولى (الإنجليزية والفرنسية) المقررة على كافة طلاب البكالوريا المصرية.",
    "",
    "| # | المادة الدراسية | الفصل الدراسي | نوع المحتوى | الرابط المباشر للمصدر |",
    "| :-: | :--- | :--- | :--- | :--- |"
]
md_lines.extend(core_rows)

md_lines.extend([
    "",
    "---",
    "",
    "## 2. المواد التخصصية لكل مسار (Specialized Tracks)",
    "",
    "تشمل مسارات: الطب وعلوم الحياة (رياضيات، فيزياء)، الهندسة وعلوم الحاسب (كيمياء، برمجة وذكاء اصطناعي)، الأعمال (محاسبة، إدارة أعمال)، والآداب والفنون (علم نفس، لغات أجنبية ثانية).",
    "",
    "| # | المسار والمادة التخصصية | الفصل الدراسي | نوع المحتوى | الرابط المباشر للمصدر |",
    "| :-: | :--- | :--- | :--- | :--- |"
])
md_lines.extend(spec_rows)

md_lines.extend([
    "",
    "---",
    "",
    "## 3. الأنشطة التعليمية - الثقافة المالية (Financial Literacy)",
    "",
    "مقرر الثقافة المالية للأنشطة المدرسية متاح باللغتين العربية والإنجليزية.",
    "",
    "| # | المادة | الفصل الدراسي | نوع الكتاب | الرابط المباشر |",
    "| :-: | :--- | :--- | :--- | :--- |"
])
md_lines.extend(act_rows)

md_lines.extend([
    "",
    "---",
    "",
    f"## 4. ملحق روابط التحميل المباشرة لجميع الكتب والتقييمات ({len(deep_pdf_items)} ملف PDF)",
    "",
    "قائمة تفصيلية كاملة بجميع الكتب الدراسية، كتب التمارين والأنشطة، القصص، وكتب التقييمات والأداءات بصيغة PDF المباشرة المستخرجة من بوابة البكالوريا المصرية:",
    "",
    "| # | المسار / المادة | الفصل الدراسي | نوع الملف | رابط التحميل المباشر PDF |",
    "| :-: | :--- | :--- | :--- | :--- |"
])

for i, pdf_item in enumerate(deep_pdf_items, 1):
    subj = pdf_item["subject"]
    term = pdf_item["term"]
    t = pdf_item["type"]
    link = pdf_item["link"]
    md_lines.append(f"| {i} | {subj} | {term} | {t} | [تحميل PDF]({link}) |")

md_lines.extend([
    "",
    "---",
    "",
    "## ملخص الإحصائيات",
    "",
    f"- **المصادر الرئيسية المنظمة:** 19 مورد أساسي وتخصصي ونشاط",
    f"  - **المواد الأساسية:** {len(core_rows)} مصادر (اللغة العربية: 4، التاريخ المصري: 3، اللغات الأولى: 2)",
    f"  - **المواد التخصصية:** {len(spec_rows)} مسارات ومواد (الطب: 2، الهندسة: 2، الأعمال: 2، الآداب والفنون: 2)",
    f"  - **الأنشطة والثقافة المالية:** {len(act_rows)} موارد (عربي وإنجليزي)",
    f"- **إجمالي ملفات PDF المباشرة المستخرجة:** {len(deep_pdf_items)} كتاب ومورد PDF مباشر",
    ""
])

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print(f"Saved Markdown -> {OUT_MD} ({OUT_MD.stat().st_size} bytes)")
