import json
import urllib.parse
import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_cards(url):
    req = urllib.request.Request(url, headers=HEADERS)
    html = urllib.request.urlopen(req, context=ctx, timeout=10).read().decode('utf-8', errors='ignore')
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
            try:
                sub = crawl_all(full, path + [title])
                if sub:
                    results.extend(sub)
                else:
                    results.append((path + [title], desc, full))
            except Exception as e:
                print(f"Error crawling {full}: {e}")
                results.append((path + [title], desc, full))
        else:
            results.append((path + [title], desc, full))
    return results

all_leafs = crawl_all('https://ellibrary.moe.gov.eg/EgyptianBaccalaureate/')
print(f"Total deep leaves found: {len(all_leafs)}")
for p, d, l in all_leafs:
    print(f"{' -> '.join(p)} | {l}")
