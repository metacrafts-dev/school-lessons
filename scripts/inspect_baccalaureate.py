import json
import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open(r'D:\WORKSPACE\PROJECTS\school-lessons\baccalaureate_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items in baccalaureate_items.json: {len(items)}")

for i, item in enumerate(items):
    link = item['link']
    print(f"\n--- Item {i+1} ---")
    print(f"Category: {item.get('category')}")
    print(f"Subject: {item.get('subject')}")
    print(f"Type: {item.get('type')}")
    print(f"Description: {item.get('description')}")
    print(f"Link: {link}")
    
    if not link.endswith('.pdf'):
        try:
            req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(req, context=ctx, timeout=5).read().decode('utf-8', errors='ignore')
            print(f"HTML size: {len(html)}")
            # look for links
            links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
            card_matches = re.findall(r'title:\s*[\'"]([^\'"]+)[\'"].*?link:\s*[\'"]([^\'"]+)[\'"]', html, re.DOTALL)
            print(f"Internal card definitions: {card_matches}")
            pdf_links = [l for l in links if '.pdf' in l.lower()]
            print(f"PDF links in HTML: {pdf_links}")
        except Exception as e:
            print(f"Fetch error: {e}")
