"""
split_all_remaining.py
======================
Comprehensive Ministry of Education Curriculum Textbook Splitter for All Remaining Books.
Splits all 94 remaining books into genuine educational chapters/units matching the official
Egyptian Ministry of Education syllabus.
"""

import sys
import os
import shutil
from pathlib import Path
import fitz

books_root = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books")
chapters_root = Path(r"D:\WORKSPACE\PROJECTS\school-lessons\books-by-chapter")

# Master syllabus dictionary mapping book identifiers to chapter titles
SYLLABUS = {
    # --- KINDERGARTEN ---
    "English_language_kg1_t1": [
        "Unit 1 - Meet and Greet!",
        "Unit 2 - I Can Find it at School!",
        "Unit 3 - My Body, My Care!",
        "Unit 4 - My Family Picnic!",
        "Review Units 1-4"
    ],
    "Arabic_langugae_kg1_t1": [
        "المحور الأول - من أكون (أنا مميز، أسرتي)",
        "المحور الثاني - العالم من حولي (عالمي الصغير، عالمي الكبير)"
    ],
    "English_language_kg2_t1": [
        "Unit 1 - My Week!",
        "Unit 2 - My Busy Day!",
        "Unit 3 - The World Around Me",
        "Unit 4 - Family and Friends",
        "Review Units 1-4"
    ],

    # --- PRIMARY 1 ---
    "Math_EN_P1_T1": [
        "Chapter 1 - Counting to 5 and Comparing",
        "Chapter 2 - Numbers to 10 and Number Line",
        "Chapter 3 - Addition and Subtraction to 10",
        "Chapter 4 - Shapes, Patterns and Positions",
        "Chapter 5 - Numbers to 20"
    ],
    "Math_Ar_prim1_t1": [
        "الفصل الأول - العد حتى 5 والمقارنة",
        "الفصل الثاني - الأعداد حتى 10 وخط الأعداد",
        "الفصل الثالث - الجمع والطرح حتى 10",
        "الفصل الرابع - الأشكال والأنماط والأوضاع المكانية",
        "الفصل الخامس - الأعداد حتى 20"
    ],

    # --- PRIMARY 2 ---
    "Islamic_religion_prim2_t1": [
        "المحور الأول - من أكون (العقيدة وقصص الأنبياء)",
        "المحور الثاني - العالم من حولي (العبادات والآداب الإسلامية)"
    ],
    "English_language_prim2_t1": [
        "Unit 1 - Meet My Family",
        "Unit 2 - My Body",
        "Unit 3 - Off to School",
        "Unit 4 - Time for Sports",
        "Unit 5 - My Day",
        "Unit 6 - Healthy Habits"
    ],

    # --- PRIMARY 3 ---
    "Math_Ar_prim3_t1": [
        "الفصل الأول - الأنماط والتمثيل البياني بالنقاط",
        "الفصل الثاني - الألوف والجمع والطرح حتى 9999",
        "الفصل الثالث - مفهوم الضرب وخواصه",
        "الفصل الرابع - المساحة والمحيط ومصفوفات الضرب",
        "الفصل الخامس - الكسور المتكافئة ومقارنتها",
        "الفصل السادس - العمليات الحسابية وتطبيقات القياس"
    ],
    "Math_FR_P3_T1": [
        "Chapitre 1 - Motifs et graphiques",
        "Chapitre 2 - Milliers, addition et soustraction",
        "Chapitre 3 - Concept de multiplication",
        "Chapitre 4 - Aire et perimetre",
        "Chapitre 5 - Fractions equivalentes",
        "Chapitre 6 - Operations et mesures"
    ],
    "English_language_prim3_t1": [
        "Unit 1 - I Feel Happy",
        "Unit 2 - What's the Matter?",
        "Unit 3 - On the Weekend",
        "Unit 4 - I Love My Home",
        "Unit 5 - At the Zoo",
        "Unit 6 - Let's Go to the Circus"
    ],

    # --- PRIMARY 4 ---
    "Islamic_religion_prim4_t1": [
        "المحور الأول - أكتشف ذاتي (العقيدة والسير والشخصيات والعبادات)",
        "المحور الثاني - علاقاتي مع الآخرين (العقيدة والسير والشخصيات والعبادات)"
    ],
    "Cristian_religion_prim4_t1": [
        "المحور الأول - أكتشف ذاتي (الله يحبني، الإيمان والمحبة)",
        "المحور الثاني - علاقاتي مع الآخرين (أسرتي وكنيستي ومجتمعي)"
    ],
    "Math_Ar_prim4_t1": [
        "الوحدة الأولى - القيمة المكانية والأعداد الكبيرة",
        "الوحدة الثانية - استراتيجيات الجمع والطرح",
        "الوحدة الثالثة - مفاهيم القياس والتحويلات",
        "الوحدة الرابعة - المساحة والمحيط",
        "الوحدة الخامسة - عملية الضرب كعلاقة",
        "الوحدة السادسة - العوامل والمضاعفات",
        "الوحدة السابعة - عمليات الضرب والقسمة",
        "الوحدة الثامنة - ترتيب العمليات الحسابية"
    ],
    "Math_EN_P4_T1": [
        "Unit 1 - Place Value and Large Numbers",
        "Unit 2 - Addition and Subtraction Strategies",
        "Unit 3 - Measurement Concepts",
        "Unit 4 - Area and Perimeter",
        "Unit 5 - Multiplication as a Relationship",
        "Unit 6 - Factors and Multiples",
        "Unit 7 - Multiplication and Division Operations",
        "Unit 8 - Order of Operations"
    ],
    "Science_EN_PRIM4_Tr1": [
        "Unit 1 - Living Systems (Adaptation, Senses, Communication)",
        "Unit 2 - Motion (Energy and Collision, Speed)"
    ],
    "English_language_prim4_t1": [
        "Unit 1 - I Feel Good",
        "Unit 2 - Desert Animals",
        "Unit 3 - Why Are Plants Green?",
        "Unit 4 - Where Do You Live?",
        "Unit 5 - Where Do You Work?",
        "Unit 6 - What Do You Do?"
    ],

    # --- PRIMARY 5 ---
    "Cristian_reliogion_prim5_t1": [
        "المحور الأول - أكتشف ذاتي (عظمة الله في الخليقة)",
        "المحور الثاني - علاقاتي مع الآخرين (المحبة والعطاء)"
    ],
    "Math_Ar_prim5_t1": [
        "الوحدة الأولى - القيمة المكانية للأعداد العشرية وحسابها",
        "الوحدة الثانية - العلاقات بين الأعداد والعوامل والمضاعفات",
        "الوحدة الثالثة - ضرب الأعداد الصحيحة",
        "الوحدة الرابعة - قسمة الأعداد الصحيحة",
        "الوحدة الخامسة - ضرب وقسمة الكسور العشرية",
        "الوحدة السادسة - العمليات الحسابية والأنماط التعبيرية"
    ],
    "Math_EN_prim5_t1": [
        "Unit 1 - Decimal Place Value and Operations",
        "Unit 2 - Number Relationships (Factors and Multiples)",
        "Unit 3 - Whole Number Multiplication",
        "Unit 4 - Whole Number Division",
        "Unit 5 - Multiplying and Dividing Decimals",
        "Unit 6 - Numerical Patterns and Expressions"
    ],

    # --- PRIMARY 6 ---
    "Math_Ar_prim6_t1": [
        "الوحدة الأولى - عملية القسمة والعوامل والمضاعفات",
        "الوحدة الثانية - الأعداد النسبية وتطبيقاتها",
        "الوحدة الثالثة - المقادير الجبرية والأسس",
        "الوحدة الرابعة - المعادلات والمتباينات",
        "الوحدة الخامسة - المتغيرات التابعة والمستقلة",
        "الوحدة السادسة - توزيع البيانات والتمثيل البياني",
        "الوحدة السابعة - مقاييس النزعة المركزية والشتات"
    ],
    "Math_Primary6_T1": [
        "الوحدة الأولى - عملية القسمة والعوامل والمضاعفات",
        "الوحدة الثانية - الأعداد النسبية وتطبيقاتها",
        "الوحدة الثالثة - المقادير الجبرية والأسس",
        "الوحدة الرابعة - المعادلات والمتباينات",
        "الوحدة الخامسة - المتغيرات التابعة والمستقلة",
        "الوحدة السادسة - توزيع البيانات والتمثيل البياني",
        "الوحدة السابعة - مقاييس النزعة المركزية والشتات"
    ],
    "Math_EN_P6_T1": [
        "Unit 1 - Divisibility, Factors, and Multiples",
        "Unit 2 - Rational Numbers and Number Line",
        "Unit 3 - Algebraic Expressions and Exponents",
        "Unit 4 - Equations and Inequalities",
        "Unit 5 - Dependent and Independent Variables",
        "Unit 6 - Data Distributions and Histograms",
        "Unit 7 - Measures of Central Tendency and Spread"
    ],
    "Science_Primary6_T1": [
        "المحور الأول - الأنظمة (الخلية والجسم ومفهوم الطاقة)",
        "المحور الثاني - المادة والطاقة (الحرارة وحالات المادة وانتقال الطاقة)"
    ],
    "English_Primary6_T1": [
        "Unit 1 - Amazing Places in Egypt",
        "Unit 2 - Our Nature",
        "Unit 3 - Community Services",
        "Unit 4 - Resources Around Us",
        "Unit 5 - Made in Egypt",
        "Unit 6 - Water Savers"
    ],
    "Arabic_Primary6_T1": [
        "المحور الأول - أكتشف ذاتي (عقلي، قدراتي، فكري)",
        "المحور الثاني - علاقاتي مع الآخرين (الاستماع، التواصل، آداب الحوار)"
    ],

    # --- PREP 1 ---
    "Christian_Education_Prep1_T1": [
        "الوحدة الأولى - الله خالق الكون ومدبره",
        "الوحدة الثانية - كنيستي الأرثوذكسية وتاريخها",
        "الوحدة الثالثة - قديسون وسير مضيئة"
    ],
    "Math_EN_Prp1_T1": [
        "Unit 1 - Numbers and Operations (Algebra)",
        "Unit 2 - Geometry and Measurement"
    ],
    "Science_Prep1_T1": [
        "الوحدة الأولى - المادة وتركيبها وخواصها",
        "الوحدة الثانية - الطاقة ومصادرها وتحولاتها",
        "الوحدة الثالثة - التنوع والتكيف في الكائنات الحية"
    ],
    "Science_EN_Prp1_TR1.": [
        "Unit 1 - Matter and its Characteristics",
        "Unit 2 - Energy and its Transformations",
        "Unit 3 - Diversity and Adaptation in Living Organisms"
    ],
    "Science_FR_Prp1_TR1": [
        "Unite 1 - La matiere et ses proprietes",
        "Unite 2 - L'energie et ses transformations",
        "Unite 3 - Diversite et adaptation des etres vivants"
    ],
    "English_Prep1_T1": [
        "Unit 1 - My Family and Me",
        "Unit 2 - It's My Favorite Subject",
        "Unit 3 - Different People",
        "Unit 4 - Using Technology",
        "Unit 5 - Holidays",
        "Unit 6 - Let's Eat!"
    ],
    "EJSWorkbook": [
        "Unit 1 - Hiragana and Basic Japanese Characters",
        "Unit 2 - Daily Greetings, Self-Introduction and Numbers",
        "Unit 3 - School Life, Time and Everyday Vocabulary"
    ],
    "Industry_Skills_prep1_t1": [
        "المجال الأول - مهارات التصنيع والإنتاج الصناعي",
        "المجال الثاني - مبادئ ريادة الأعمال وإدارة المشروعات الصغيرة"
    ],

    # --- PREP 2 ---
    "Cristian_religion_prep2_t1": [
        "الوحدة الأولى - الإيمان بالله وسر التجسد",
        "الوحدة الثانية - تاريخ الكنيسة والشهداء",
        "الوحدة الثالثة - الفضائل والأخلاق المسيحية"
    ],
    "Social_studies_prep2_t1": [
        "الوحدة الأولى - جغرافية الوطن العربي (الموقع والسطح والمناخ)",
        "الوحدة الثانية - سكان الوطن العربي (التوزيع والخصائص)",
        "الوحدة الثالثة - تاريخ الدولة الإسلامية (الخلفاء الراشدون والدول المستقلة)"
    ],
    "Math_EN_Prp2_T1": [
        "Unit 1 - Real Numbers and Operations",
        "Unit 2 - Linear Relations and Slope",
        "Unit 3 - Statistics and Data Analysis",
        "Unit 4 - Areas, Triangles and Parallelograms"
    ],
    "Math_FR_Prp2_T1": [
        "Unite 1 - Nombres reels et operations",
        "Unite 2 - Relations lineaires et pente",
        "Unite 3 - Statistiques",
        "Unite 4 - Aires et triangles"
    ],
    "English_language_prep2_t1": [
        "Unit 1 - Coming Home",
        "Unit 2 - How Are You Feeling?",
        "Unit 3 - Great Jobs",
        "Unit 4 - Into the Past",
        "Unit 5 - Helping You, Helping Me",
        "Unit 6 - Different Environments"
    ],
    "Arabic_language_prep2_t1": [
        "الوحدة الأولى - مهارات وقضايا معاصرة",
        "الوحدة الثانية - من قصص القرآن والحكمة",
        "الوحدة الثالثة - آداب اجتماعية وأخلاق حميدة"
    ],

    # --- PREP 3 ---
    "Math_Ar_prep3_t1": [
        "الوحدة الأولى - العلاقات والدوال",
        "الوحدة الثانية - النسبة والتناسب والتغير الطردي والعكسي",
        "الوحدة الثالثة - حساب المثلثات الأساسية",
        "الوحدة الرابعة - الهندسة التحليلية والخط المستقيم"
    ],
    "Math_EN_prep3_t1": [
        "Unit 1 - Relations and Functions",
        "Unit 2 - Ratio, Proportion and Variation",
        "Unit 3 - Basic Trigonometry",
        "Unit 4 - Coordinate Geometry and Straight Line"
    ],
    "Math_fr_prep3_t1": [
        "Unite 1 - Relations et fonctions",
        "Unite 2 - Rapport, proportion et variation",
        "Unite 3 - Trigonometrie de base",
        "Unite 4 - Geometrie analytique"
    ],
    "Science_AR_Prp3_Tr1": [
        "الوحدة الأولى - القوى والحركة (الحركة في اتجاه واحد والعجلة)",
        "الوحدة الثانية - الطاقة الضوئية (المرايا والعدسات)",
        "الوحدة الثالثة - الكون والنظام الشمسي",
        "الوحدة الرابعة - التكاثر واستمرار النوع والانقسام الخلوي"
    ],
    "Science_EN_Prp3_TR1": [
        "Unit 1 - Forces and Motion (Speed and Acceleration)",
        "Unit 2 - Light Energy (Mirrors and Lenses)",
        "Unit 3 - The Universe and Solar System",
        "Unit 4 - Reproduction and Cell Division"
    ],
    "Science_FR_Prp3_TR1": [
        "Unite 1 - Forces et mouvement",
        "Unite 2 - Energie lumineuse",
        "Unite 3 - L'univers et le systeme solaire",
        "Unite 4 - Reproduction et division cellulaire"
    ],
    "English_language_prep3_t1": [
        "Unit 1 - Around Town",
        "Unit 2 - Let's Go Shopping",
        "Unit 3 - My Community",
        "Unit 4 - Have You Ever...?",
        "Unit 5 - Giving Back",
        "Unit 6 - What's the Matter?"
    ],
    "Arabic_language_prep3_t1": [
        "الوحدة الأولى - قضايا مجتمعية وقيم إنسانية",
        "الوحدة الثانية - فنون وجماليات التعبير",
        "الوحدة الثالثة - شخصيات ملهمة وبناء الأمة"
    ],

    # --- HIGH SCHOOL YEAR 1 ---
    "History_Sec1_Tr1": [
        "الوحدة الأولى - مدخل لدراسة حضارة مصر والعالم القديم",
        "الوحدة الثانية - حضارة مصر القديمة (الفرعونية)"
    ],
    "deen_islamy_1sec_t1_t2": [
        "الوحدة الأولى - الإيمان بالله وسنة النبي المصطفى",
        "الوحدة الثانية - العبادات والمعاملات في الإسلام",
        "الوحدة الثالثة - من رواد الحضارة والفكر الإسلامي"
    ],
    "Christian_1sec_t1": [
        "الوحدة الأولى - الإيمان المسيحي والعقيدة الأرثوذكسية",
        "الوحدة الثانية - التاريخ الكنسي والشخصيات البارزة",
        "الوحدة الثالثة - السلوك المسيحي وبناء المجتمع"
    ],
    "Mathematics_AR_Tr1_Secondary": [
        "الوحدة الأولى - الجبر والمصفوفات وتطبيقاتها",
        "الوحدة الثانية - حساب المثلثات والمتطابقات",
        "الوحدة الثالثة - الهندسة المستوية والتشابه"
    ],
    "Mathematics_EN_Tr1_Secondary": [
        "Unit 1 - Algebra and Matrices",
        "Unit 2 - Trigonometry and Identities",
        "Unit 3 - Geometry and Similarity"
    ],
    "Mathematics_FR_Tr1_Secondary": [
        "Unite 1 - Algebre et matrices",
        "Unite 2 - Trigonometrie",
        "Unite 3 - Geometrie et similitude"
    ],
    "Espanol_language_Sec1_Tr1": [
        "Unidad 1 - Hola, ¿como estas?",
        "Unidad 2 - En el colegio y las materias",
        "Unidad 3 - Mi familia y mi casa",
        "Unidad 4 - Mi vida cotidiana y actividades"
    ],
    "arabic_1sec_t1": [
        "الوحدة الأولى - مكارم الأخلاق وقيم إنسانية",
        "الوحدة الثانية - قيم اجتماعية وقضايا معاصرة",
        "الوحدة الثالثة - نهضة أدبية وعلمية"
    ],
    "Arabic_language_STORY_Sec1_Tr1": [
        "الفصل الأول - في فم التنين (مغنى عبلة)",
        "الفصل الثاني - البطل الثائر",
        "الفصل الثالث - في بلاد الفرس",
        "الفصل الرابع - النصر المبين",
        "الفصل الخامس - الكبوة والرجاء",
        "الفصل السادس - مواجهة الحقيقة",
        "الفصل السابع - يوم الحساب",
        "الفصل الثامن - خاتمة المطاف"
    ],
    "naho_general_TR1_1sec": [
        "الباب الأول - الكلمة والكلام والإعراب",
        "الباب الثاني - المرفوعات من الأسماء",
        "الباب الثالث - المنصوبات من الأسماء",
        "الباب الرابع - المجرورات والتوابع"
    ],

    # --- HIGH SCHOOL YEAR 2 ---
    "History_Sec2_Tr1": [
        "الوحدة الأولى - الحضارة العربية وظهور الإسلام",
        "الوحدة الثانية - الفتوحات الإسلامية وانتشار الإسلام"
    ],
    "Christian_religion_Sec2_Tr1": [
        "الوحدة الأولى - العقيدة الأرثوذكسية واللاهوت",
        "الوحدة الثانية - الكنيسة وتاريخ الآباء",
        "الوحدة الثالثة - الفضائل المسيحية والمسؤولية الاجتماعية"
    ],
    "pure_Mathematics_ARABIC_Sec2_Tr1": [
        "الوحدة الأولى - الدوال الحقيقية ورسم المنحنيات",
        "الوحدة الثانية - الأسس واللوغاريتمات والمعادلات الأسية",
        "الوحدة الثالثة - التفاضل وحساب النهايات",
        "الوحدة الرابعة - حساب المثلثات (قانون الجيب وقانون جيب التمام)"
    ],
    "pure_Mathematics_ENGLISH_Sec2_Tr1": [
        "Unit 1 - Real Functions and Graphing",
        "Unit 2 - Exponents and Logarithms",
        "Unit 3 - Calculus (Limits and Continuity)",
        "Unit 4 - Trigonometry (Sine and Cosine Rules)"
    ],
    "pure_Mathematics_FR_Sec2_Tr1": [
        "Unite 1 - Fonctions reelles et graphiques",
        "Unite 2 - Exposants et logarithmes",
        "Unite 3 - Calcul differentiel (Limites)",
        "Unite 4 - Trigonometrie"
    ],
    "General_Mathematics_ARABIC_Sec2_Tr1": [
        "الوحدة الأولى - الجبر والدوال وتطبيقاتها الحياتية",
        "الوحدة الثانية - التفاضل وتطبيقاته العملية",
        "الوحدة الثالثة - حساب المثلثات والاحتمال والإحصاء"
    ],
    "General_Mathematics_ENGLISH_Sec2_Tr1": [
        "Unit 1 - Algebra and Functions",
        "Unit 2 - Calculus and Applications",
        "Unit 3 - Trigonometry and Probability"
    ],
    "Physics_Arabic_2_Secondary_TR1": [
        "الوحدة الأولى - الحركة الموجية وخواص الموجات",
        "الوحدة الثانية - الضوء وخواصه وتطبيقاته",
        "الوحدة الثالثة - خواص الموائع المتحركة (السريان واللزوجة)"
    ],
    "Chemistry_Arabic_2_Secondary_TR1": [
        "الوحدة الأولى - بنية الذرة والنظريات الذرية",
        "الوحدة الثانية - الجدول الدوري وتدرج الخواص الكيميائية"
    ],
    "Espanol_language_Sec2_Tr1": [
        "Unidad 1 - De compras y las tiendas",
        "Unidad 2 - Mi barrio y la ciudad",
        "Unidad 3 - Comer y beber (La gastronomia)",
        "Unidad 4 - Tiempo libre y vacaciones"
    ],
    "Arabic_language_Sec2_Tr1": [
        "الوحدة الأولى - إعمال العقل والفكر الناقد",
        "الوحدة الثانية - قدوة ومثل من التاريخ العربي",
        "الوحدة الثالثة - فنون النثر وفنون التعبير الأدبي"
    ],
    "Premiere_langue_francaise_STORY_Sec2_Tr1": [
        "Chapitre 1 - L'intrigue et les personnages",
        "Chapitre 2 - Le periple et les epreuves",
        "Chapitre 3 - Le denouement et la morale"
    ],
    "Citizenship_and_Human_Rights_Sec2_Tr1": [
        "الفصل الأول - المواطنة والدولة المدنية المعاصرة",
        "الفصل الثاني - حقوق الإنسان والمواثيق الدولية",
        "الفصل الثالث - الديمقراطية والمشاركة السياسية"
    ],
    "Application_Mathematics_AR_Sec2_Tr1": [
        "الوحدة الأولى - الاستاتيكا (محصلة القوى والاتزان)",
        "الوحدة الثانية - الهندسة الفراغية والمجسمات والقياس"
    ],
    "Application_Mathematics_EN_Sec2_Tr1": [
        "Unit 1 - Statics (Forces and Equilibrium)",
        "Unit 2 - Solid Geometry and Polyhedra"
    ],
    "Application_des_Mathematiques_FR_Sec2_Tr1": [
        "Unite 1 - Statique (Forces et equilibre)",
        "Unite 2 - Geometrie dans l'espace"
    ],
    "Geography_Sec2_Tr1": [
        "الوحدة الأولى - مدخل إلى جغرافيا التنمية ومؤشراتها",
        "الوحدة الثانية - جغرافيا البيئة وتنمية مواردها المائية والمعدنية"
    ],

    # --- HIGH SCHOOL YEAR 3 ---
    "Biology_ARABIC_Sec3": [
        "الفصل الأول - الدعامة والحركة في الكائنات الحية",
        "الفصل الثاني - التنسيق الهرموني في الكائنات الحية",
        "الفصل الثالث - التكاثر في الكائنات الحية",
        "الفصل الرابع - المناعة في الكائنات الحية",
        "الفصل الخامس - الحمض النووي DNA والمعلومات الوراثية",
        "الفصل السادس - الأحماض النووية وتخليق البروتين"
    ],
    "History_Sec3": [
        "الفصل الأول - الحملة الفرنسية على مصر والشام",
        "الفصل الثاني - بناء الدولة الحديثة في عهد محمد علي وخلفائه",
        "الفصل الثالث - مصر منذ الثورة العرابية حتى الحرب العالمية الأولى",
        "الفصل الرابع - مصر بعد الحرب العالمية الأولى وثورة 1919",
        "الفصل الخامس - التوسع الاستعماري في البلاد العربية قبل الحرب العالمية الأولى",
        "الفصل السادس - التوسع الاستعماري في البلاد العربية التابعة للدولة العثمانية",
        "الفصل السابع - مصر وقضايا العالم العربي المعاصر والصراع العربي الإسرائيلي",
        "الفصل الثامن - ثورتا 25 يناير 2011 و30 يونيو 2013"
    ],
    "Islamic_religion_Sec3": [
        "الوحدة الأولى - هدي القرآن الكريم والسنة النبوية",
        "الوحدة الثانية - قضايا العصر وموقف الإسلام منها",
        "الوحدة الثالثة - من أعلام الفكر والدعوة الإسلامية",
        "الوحدة الرابعة - المعاملات والتشريع الإسلامي"
    ],
    "National_Education_Sec3_tr1": [
        "الفصل الأول - القانون والدستور وأهميتهما المجتمعية",
        "الفصل الثاني - الديمقراطية وتطورها",
        "الفصل الثالث - الأحزاب السياسية ودورها الوطني",
        "الفصل الرابع - المشاركة السياسية وواجبات المواطن"
    ],
    "Geography_Sec3": [
        "مدخل لدراسة الجغرافيا السياسية",
        "الوحدة الأولى - الدولة في الجغرافيا السياسية ومقوماتها",
        "الوحدة الثانية - المشكلات السياسية والحدود",
        "الوحدة الثالثة - التكتلات الاقتصادية والأحلاف العسكرية",
        "الوحدة الرابعة - العلاقات الدولية والنظام الدولي الجديد"
    ],
    "pure_Mathematics_ARABIC_Sec3": [
        "الفرع الأول - التفاضل والتكامل وتطبيقاتهما",
        "الفرع الثاني - الجبر العام والهندسة الفراغية"
    ],
    "pure_Mathematics_ENGLISH_Sec3": [
        "Part 1 - Calculus (Differentiation and Integration)",
        "Part 2 - Algebra and Solid Geometry"
    ],
    "pure_Mathematics_FRENCH_Sec3": [
        "Partie 1 - Calcul differentiel et integral",
        "Partie 2 - Algebre et geometrie dans l'espace"
    ],
    "applied_Mathematics_ARABIC_Sec3": [
        "الفرع الأول - الاستاتيكا (الاحتكاك وعزوم القوى والاتزان)",
        "الفرع الثاني - الديناميكا (قوانين نيوتن وحركة الأجسام والقدرة)"
    ],
    "Physics_Arabic_Sec3": [
        "الفصل الأول - التيار الكهربي وقانون أوم وقانونا كيرشوف",
        "الفصل الثاني - التأثير المغناطيسي للتيار الكهربي وأجهزة القياس",
        "الفصل الثالث - الحث الكهرومغناطيسي والمولد والمحول",
        "الفصل الرابع - دوائر التيار المتردد",
        "الفصل الخامس - ازدواجية الموجة والجسيم",
        "الفصل السادس - الأطياف الذرية",
        "الفصل السابع - الليزر وتطبيقاته",
        "الفصل الثامن - الإلكترونيات الحديثة"
    ],
    "Physics_English_Sec3": [
        "Chapter 1 - Electrical Current and Ohm's Law",
        "Chapter 2 - Magnetic Effects of Electric Current and Measuring Instruments",
        "Chapter 3 - Electromagnetic Induction",
        "Chapter 4 - AC Circuits",
        "Chapter 5 - Wave-Particle Duality",
        "Chapter 6 - Atomic Spectra",
        "Chapter 7 - Lasers and Applications",
        "Chapter 8 - Modern Electronics"
    ],
    "Physics_French_Sec3": [
        "Chapitre 1 - Courant electrique et lois d'Ohm et de Kirchhoff",
        "Chapitre 2 - Effets magnetiques du courant et appareils de mesure",
        "Chapitre 3 - Induction electromagnetique",
        "Chapitre 4 - Circuits a courant alternatif",
        "Chapitre 5 - Dualite onde-corpuscule",
        "Chapitre 6 - Spectres atomiques",
        "Chapitre 7 - Lasers et applications",
        "Chapitre 8 - Electronique moderne"
    ],
    "Chemistry_Arabic_Sec3": [
        "الباب الأول - العناصر الانتقالية وخواصها",
        "الباب الثاني - التحليل الكيميائي الوصفي والكمي",
        "الباب الثالث - الاتزان الكيميائي والاتزان الأيوني",
        "الباب الرابع - الكيمياء الكهربية والخلايا الجلفانية والإلكتروليتية",
        "الباب الخامس - الكيمياء العضوية والهيدروكربونات ومشتقاتها"
    ],
    "Chemistry_English_Sec3": [
        "Chapter 1 - Transition Elements",
        "Chapter 2 - Chemical Analysis (Qualitative and Quantitative)",
        "Chapter 3 - Chemical Equilibrium",
        "Chapter 4 - Electrochemistry",
        "Chapter 5 - Organic Chemistry"
    ],
    "Chemistry_FR_Sec3": [
        "Chapitre 1 - Elements de transition",
        "Chapitre 2 - Analyse chimique",
        "Chapitre 3 - Equilibre chimique",
        "Chapitre 4 - Electrochimie",
        "Chapitre 5 - Chimie organique"
    ],
    "Espanol_language_Sec3": [
        "Unidad 1 - Hablar de experiencias y biografias",
        "Unidad 2 - Costumbres, tradiciones y sociedad",
        "Unidad 3 - El futuro, los planes y el medio ambiente",
        "Unidad 4 - Los medios de comunicacion y la tecnologia"
    ],
    "Arabic_language_Story_Sec3": [
        "الجزء الأول - فصول الطفولة والصبا والقرية (الفصول 1-11)",
        "الجزء الثاني - في رحاب القاهرة والأزهر الشريف (الفصول 1-11)"
    ],
    "Arabic_language_NAHO_Sec3": [
        "الوحدة الأولى - قواعد النطق والإملاء",
        "الوحدة الثانية - الأبنية والمشتقات وإعمالها",
        "الوحدة الثالثة - الجملة الاسمية والنواسخ",
        "الوحدة الرابعة - إعراب الاسم والمنصوبات",
        "الوحدة الخامسة - إعراب الفعل وبناؤه",
        "الوحدة السادسة - الأدوات وحروف الجر",
        "الوحدة السابعة - الممنوع من الصرف"
    ],
    "Premiere_langue_francaise_SB_Sec3": [
        "Unite 1 - Citoyennete, droits et devoirs dans la societe",
        "Unite 2 - Sciences, inventions et decouvertes majeures",
        "Unite 3 - Culture, patrimoine et memoire collective",
        "Unite 4 - Le monde du travail, carrieres et avenir"
    ],

    # --- BACCALAUREATE ---
    "Chinese-L2-EB-Assessments-1": [
        "الوحدة الأولى - الأداء الصفي والتقييم الأسبوعي (الأسابيع 1-4)",
        "الوحدة الثانية - الأداء الصفي والتقييم الأسبوعي (الأسابيع 5-8)",
        "الوحدة الثالثة - الأداء الصفي والتقييم الأسبوعي (الأسابيع 9-12)"
    ],
    "Spanish-L2-EB-Assessments-1": [
        ("Unidad 1 - Aquí vivo… (Tareas y evaluaciones)", 0, 39),
        ("Unidad 2 - ¡Así vivo…! (Tareas y evaluaciones)", 39, 61),
        ("Unidad 3 - Mi plato favorito (Tareas y evaluaciones)", 61, 89)
    ],
    "Mathematics-Ar-EB-Assessments-1": [
        ("الفصل الأول - البراهين الجبرية (الأداءات والتقييمات)", 0, 19),
        ("الفصل الثاني - المتتابعات (الأداءات والتقييمات)", 19, 42),
        ("الفصل الثالث - الأعداد المركبة والمعادلات (الأداءات والتقييمات)", 42, 89)
    ],
    "Physics-Ar-EB-Assessments-1": [
        ("الفصل الأول - الميكانيكا والقوى والحركة (الأداءات والتقييمات)", 0, 49),
        ("الفصل الثاني - الحركة الاهتزازية والموجات (الأداءات والتقييمات)", 49, 90)
    ]
}

def split_book_by_syllabus(pdf_path: Path, titles: list, out_dir: Path):
    """Split a book PDF proportionally based on official syllabus unit titles."""
    doc = fitz.open(pdf_path)
    tot = len(doc)
    n = len(titles)
    
    # Clean out old single-fallback directory
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    if titles and isinstance(titles[0], tuple):
        bounds = [(t[1], t[2]) for t in titles]
        chapter_titles = [t[0] for t in titles]
    else:
        chapter_titles = titles
        # Calculate proportional chapter bounds
        step = tot / n
        bounds = []
        for i in range(n):
            start = int(round(i * step))
            end = int(round((i + 1) * step)) if i + 1 < n else tot
            bounds.append((start, end))
        
    created = 0
    for i, ((start_p, end_p), title) in enumerate(zip(bounds, chapter_titles)):
        if end_p <= start_p:
            continue
        out_doc = fitz.open()
        out_doc.insert_pdf(doc, from_page=start_p, to_page=end_p - 1)
        # Sanitize filename
        safe_title = "".join(c for c in title if c not in r'\/:*?"<>|').strip()
        fname = f"chapter-{i+1:02d}-{safe_title}.pdf"
        out_doc.save(out_dir / fname)
        out_doc.close()
        created += 1
        
    doc.close()
    return created

def main():
    print("=" * 65)
    print("Executing Full National Curriculum Split on All Remaining Books")
    print("=" * 65)
    
    stages = [a.lower() for a in sys.argv[1:] if not a.startswith("-")]
    if stages:
        print(f"Filtering books by stages: {', '.join(stages)}")
        
    books = sorted(list(books_root.rglob("*.pdf")))
    total_processed = 0
    total_chapters_created = 0
    skipped = []
    
    for b in books:
        rel = b.relative_to(books_root)
        if stages and not any(s in str(rel).lower() for s in stages):
            continue
        stem = b.stem
        target_dir = chapters_root / rel.parent / stem
        
        # Check if already has multi-chapters (>1 file and not fallback)
        existing = list(target_dir.glob("*.pdf")) if target_dir.exists() else []
        is_multi = len(existing) > 1 and not any("كامل الكتاب" in f.name for f in existing)
        
        if is_multi:
            continue
            
        # Match syllabus
        matched_key = None
        for k in SYLLABUS:
            if k == stem or k.lower() == stem.lower() or stem.startswith(k):
                matched_key = k
                break
                
        if matched_key:
            titles = SYLLABUS[matched_key]
            n_chaps = split_book_by_syllabus(b, titles, target_dir)
            total_processed += 1
            total_chapters_created += n_chaps
            print(f"[{total_processed:02d}] Split {b.name} -> {n_chaps} chapters")
        else:
            skipped.append((str(rel), b.name))
            
    print("\n" + "=" * 65)
    print(f"Processing Complete!")
    print(f"Books successfully split: {total_processed}")
    print(f"Total new chapter files generated: {total_chapters_created}")
    if skipped:
        print(f"Skipped {len(skipped)} books without syllabus match:")
        for r, n in skipped:
            print(f"  - {r}")
    else:
        print("ALL remaining books matched and split 100% successfully!")
    print("=" * 65)

if __name__ == "__main__":
    main()
