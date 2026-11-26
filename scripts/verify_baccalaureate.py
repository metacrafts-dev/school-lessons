import json
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

JSON_FILE = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_books.json")
MD_FILE = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_books.md")
TXT_FILE = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_links.txt")

with open(JSON_FILE, "r", encoding="utf-8") as f:
    items = json.load(f)

print(f"Total items in JSON: {len(items)}")

# 1. Field validation
required_fields = ["stage", "grade", "term", "subject", "type", "link"]
field_errors = []
for i, item in enumerate(items, 1):
    for rf in required_fields:
        if rf not in item or not str(item[rf]).strip():
            field_errors.append(f"Item {i} missing or empty '{rf}'")

if field_errors:
    print(f"FAILED Field Validation: {field_errors}")
else:
    print("PASSED Field Validation: All 6 required fields (stage, grade, term, subject, type, link) present in all items.")

# 2. File counts validation
with open(TXT_FILE, "r", encoding="utf-8") as f:
    txt_links = [line.strip() for line in f if line.strip()]
print(f"Links count in TXT: {len(txt_links)}")
assert len(txt_links) == len(items) == 19, "Counts mismatch between JSON and TXT!"

# 3. URL accessibility check
headers = {"User-Agent": "Mozilla/5.0"}
url_errors = []
print("\nChecking URL accessibility:")
for i, item in enumerate(items, 1):
    link = item["link"]
    try:
        req = urllib.request.Request(link, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            status = resp.status
            size = resp.headers.get("Content-Length", "unknown")
            print(f"  [{i:02d}/19] HTTP {status} (size: {size}) -> {item['subject']}")
    except Exception as e:
        url_errors.append((i, link, str(e)))
        print(f"  [{i:02d}/19] FAIL: {e} -> {link}")

if not url_errors:
    print("\nALL 19 URLs successfully responded with HTTP 200 OK!")
else:
    print(f"\n{len(url_errors)} URLs failed: {url_errors}")
