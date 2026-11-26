"""Crawl all active Egyptian Baccalaureate sections and extract all materials."""

import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

HEADERS = {"User-Agent": "Mozilla/5.0"}
BASE_EB = "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/"


def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def extract_active_card_links(html: str) -> list[tuple[str, str, str]]:
    """Extract only un-commented infoCard items (title, text, link)."""
    results = []
    for line in html.splitlines():
        trimmed = line.strip()
        if trimmed.startswith("//") or trimmed.startswith("/*") or trimmed.startswith("*"):
            continue
        m = re.search(r'title:\s*["\']([^"\']+)["\'],\s*text:\s*["\']([^"\']+)["\'],\s*link:\s*["\']([^"\']+)["\']', trimmed)
        if m:
            results.append((m.group(1), m.group(2), m.group(3)))
    return results


def main() -> None:
    html_main = fetch_url(BASE_EB)
    main_cards = extract_active_card_links(html_main)
    print(f"Active main EB sections: {[c[2] for c in main_cards]}")

    all_eb_items = []

    for main_title, main_desc, sec_rel in main_cards:
        sec_url = urllib.parse.urljoin(BASE_EB, sec_rel)
        try:
            html_sec = fetch_url(sec_url)
        except Exception as e:
            print(f"Skipping {sec_url}: {e}")
            continue

        sub_cards = extract_active_card_links(html_sec)
        print(f"Section {sec_rel} has active sub-links: {[s[2] for s in sub_cards]}")

        for sub_title, sub_desc, sub_rel in sub_cards:
            leaf_url = urllib.parse.urljoin(sec_url, sub_rel)
            try:
                html_leaf = fetch_url(leaf_url)
            except Exception as e:
                print(f"Skipping {leaf_url}: {e}")
                continue

            leaf_items = extract_active_card_links(html_leaf)
            print(f"  Leaf {sub_rel} ({sub_title}) found {len(leaf_items)} items")

            for item_title, item_desc, link_val in leaf_items:
                full_link = urllib.parse.urljoin(leaf_url, link_val)
                all_eb_items.append({
                    "stage": "البكالوريا المصرية",
                    "grade": "الصف الثاني الثانوي",
                    "category": main_title.replace("🎓", "").strip(),
                    "subject": sub_title.replace("🎓", "").strip(),
                    "type": item_title.replace("🎓", "").strip(),
                    "description": item_desc.strip(),
                    "link": full_link
                })

    out_file = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_items.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_eb_items, f, ensure_ascii=False, indent=2)

    print(f"Total Egyptian Baccalaureate items collected: {len(all_eb_items)}")


if __name__ == "__main__":
    main()
