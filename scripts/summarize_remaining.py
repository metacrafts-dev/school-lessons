import json
with open(r'D:\WORKSPACE\PROJECTS\school-lessons\scripts\remaining_books.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

by_stage = {}
for b in books:
    by_stage.setdefault(b['stage'], []).append(b)

for stage, blist in by_stage.items():
    print(f"\n=== {stage} ({len(blist)} books) ===")
    for b in blist:
        gr = b['grade']
        sb = b['subject']
        sm = b['stem']
        pg = b['pages']
        print(f"  {gr:10s} | {sb:35s} | {sm} ({pg}p)")
