"""Probe script to inspect Egyptian Baccalaureate sub-pages and extract resource links."""

import re
import urllib.request
from html.parser import HTMLParser

class SimpleLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "a" and "href" in attr_dict:
            self.links.append(attr_dict["href"])
        elif tag == "script" and "src" in attr_dict:
            self.scripts.append(attr_dict["src"])

LEAF_URLS = [
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/CoreSubjects/Arabic/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/CoreSubjects/EgyptianHistory/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/CoreSubjects/FirstForeignLanguage/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/SpecializedSubjects/Medicine-LifeSciences/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/SpecializedSubjects/Engineering-ComputerScience/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/SpecializedSubjects/Business/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/SpecializedSubjects/Arts-Humanities/",
    "https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/Activities/FinancialLiteracy/",
]

def check_url(url: str) -> None:
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        
        parser = SimpleLinkParser()
        parser.feed(html)
        
        print(f"URL: {url}")
        print(f"  Scripts: {parser.scripts}")
        for l in parser.links:
            if any(l.lower().endswith(ext) for ext in [".pdf", ".zip", ".rar", ".xlsx", ".docx"]):
                print(f"  File link: {l}")
            elif not l.startswith("http") and not l.startswith("#"):
                print(f"  Internal link: {l}")
                
        # Check if books.json exists
        try:
            req_j = urllib.request.Request(url.rstrip("/") + "/books.json", headers=headers)
            with urllib.request.urlopen(req_j) as resp_j:
                data = resp_j.read()
                print(f"  [+] Found books.json ({len(data)} bytes)")
        except Exception:
            pass
    except Exception as e:
        print(f"Error {url}: {e}")

if __name__ == "__main__":
    for u in LEAF_URLS:
        check_url(u)
