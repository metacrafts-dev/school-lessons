import sys
from pathlib import Path
import fitz

sys.path.insert(0, r"D:\WORKSPACE\PROJECTS\school-lessons\scripts")
import split_chapters

books_root = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books")
text_books = [
  r"baccalaureate\عام\الأداب والفنون - اللغات الأجنبية الثانية (اللغة الصينية)\Chinese-L2-EB-Assessments-1.pdf",
  r"baccalaureate\عام\الأداب والفنون - اللغات الأجنبية الثانية (اللغة الصينية)\Chinese-L2-EB-part1.pdf",
  r"baccalaureate\عام\الأداب والفنون - اللغات الأجنبية الثانية (اللغة الصينية)\Chinese-L2-EB-part2.pdf",
  r"baccalaureate\عام\الأداب والفنون - علم النفس\Psychology-EB-Assessments-1.pdf",
  r"baccalaureate\عام\الثقافة المالية\FinancialLiteracy-Ar-EB-part1.pdf",
  r"baccalaureate\عام\الطب وعلوم الحياة - الفيزياء\Physics-Ar-EB-part2.pdf",
  r"baccalaureate\عام\اللغة العربية\Arabic-EB-Assessments-1.pdf",
  r"baccalaureate\عام\اللغة العربية\Story-Ar-EB.pdf",
  r"high-school\year-1\term-1\اللغة العربية-القصة\Arabic_language_STORY_Sec1_Tr1.pdf",
  r"high-school\year-1\term-1\اللغة العربية-القواعد الأساسية للنحو والصرف\naho_general_TR1_1sec.pdf",
  r"high-school\year-2\term-1\اللغة العربية-القواعد الأساسية للنحو والصرف\naho_general_TR1_1sec.pdf",
  r"high-school\year-2\term-1\المواطنة وحقوق الإنسان\Citizenship_and_Human_Rights_Sec2_Tr1.pdf",
  r"high-school\year-3\term-1\التربية الدينية الإسلامية\Islamic_religion_Sec3.pdf",
  r"kindergarten\kg-2\term-1\اللغة الإنجليزية\English_language_kg2_t1.pdf",
  r"prep\year-1\term-1\اللغة اليابانية-لغة أجنبية ثانية\EJSWorkbook.pdf",
  r"primary\year-4\term-1\التربية الدينية الإسلامية\Islamic_religion_prim4_t1.pdf",
]

print("=== Testing 16 text-bearing books with split_chapters.py v3 ===")
for rel in text_books:
    p = books_root / rel
    if p.exists():
        doc = fitz.open(p)
        chaps = split_chapters.detect_chapters(doc)
        src = chaps[0]["source"] if chaps else "none"
        print(f"[{src:12s}] {len(chaps):2d} chaps : {rel}")
        if len(chaps) > 1:
            for c in chaps[:3]:
                print(f"       p.{c['page']+1}: {c['title']}")
        doc.close()
    else:
        print(f"[MISSING] {rel}")
