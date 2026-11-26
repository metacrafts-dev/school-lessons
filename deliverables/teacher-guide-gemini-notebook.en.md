# Gemini Notebook for Egyptian Teachers — The Complete Guide

**Edition 2 · 21 November 2026 · Replaces "Master Notebook Guide" (Edition 1, 17 November 2026) and its two inserts: the 5-Stage Prompt Sequence and the Split / Summarize / Prompt cheat sheet**
Arabic version: `teacher-guide-gemini-notebook.ar.md` (same content, same section numbers).

This guide turns a textbook lesson into a **checked lesson pack** that students actually listen to, watch and practise with: audio, video, flashcards, a quiz, a mind map and a printable study guide. It is built for teachers in Egyptian schools, from kindergarten to secondary, for every subject and every language of instruction.

> **How to read this guide**
> - **Every teacher:** Parts A–D (what you will use every week), then your subject in Part E and your language case in Part F, then **Sections 15–18 and 20**. Print **Appendix A**.
> - **Supervisors:** add Section 19.
> - **Trainers / AI technicians:** everything, especially Section 19.
> - Upload this file (PDF or Markdown) as the first source of the **Master notebook** (Section 4.4).

**Labels in the app.** Google renamed NotebookLM to **Gemini Notebook** in 2026; teachers will see both names. Keep the English on-screen labels exactly as written here: **Sources, Chat, Studio, Add sources, Configure Chat, Audio Overview, Video Overview, Mind Map, Reports, Flashcards, Quizzes, Settings → Output Language.** If the app and this guide disagree, the app and Google's current help pages win (Section 21).

---

## Contents

- **Part A — Foundations:** 1. What the tool does and does not do · 2. The eight laws · 3. Verified feature reference
- **Part B — Setup:** 4. Notebooks and sources · 5. The Teacher Notes source · 6. The select ritual
- **Part C — Build a lesson pack:** 7. What a pack contains · 8. The workflow · 9. Prompt library
- **Part D — Engagement:** 10. Why students switch off, and the design rules · 11. By school stage · 12. The classroom loop and distribution
- **Part E — Subject playbooks:** 13.1 Mathematics · 13.2 Sciences · 13.3 Arabic · 13.4 English · 13.5 Second foreign languages · 13.6 Social studies, history, geography · 13.7 Religious education · 13.8 Philosophy, logic, psychology, sociology · 13.9 ICT and programming · 13.10 Values and citizenship · 13.11 Activity subjects · 13.12 Kindergarten
- **Part F — Language heuristics:** 14. The language matrix, register, notation and pronunciation
- **Part G — Quality and operations:** 15. The Teacher Check · 16. Privacy, age, accounts · 17. Limits and production planning · 18. The Microsoft 365 library · 19. Train the trainer · 20. Troubleshooting · 21. Sources and what is still to verify · 22. What changed from Edition 1
- **Part H — Programme delivery:** 23. Research method · 24. Onboarding stages for the Master notebook · 25. The training video · 26. The Prompt Builder · Appendix A. Teacher Quick Card

---

# Part A — Foundations

## 1. What Gemini Notebook does — and does not do

**It does:**
- Answer questions **from the sources you add** (PDFs, Google Docs and Slides, web pages, YouTube videos with captions, audio files, images, Markdown, text and more), with **citations** you can click to read the exact passage. Google: *"Chat responses in Gemini Notebook only use data from your sources"* (standard chat; the experimental agentic features below can search the web).
- Generate, in **Studio**, from the sources you have **checked**: Audio Overviews, Video Overviews, Mind Maps, Reports, Flashcards, Quizzes (and, for adult accounts, Infographics and Slide Decks).
- Say *"Gemini Notebook can't answer this question"* when your sources don't cover something. **That message is useful:** it tells you a source is missing.

**It does not:**
- **Know your curriculum.** It knows only the sources checked in that notebook. It will **not** go back to an earlier grade's lesson by itself. If a lesson needs earlier material, you add it (Section 13.1, "Bridge").
- **Run a task list.** Uploading a guide and saying "do everything in it" gives one generic summary. Each pack part is a separate generation that you start.
- **Guarantee accuracy.** Google warns that audio and video "may contain inaccuracies or audio glitches." A citation shows *where* an answer came from; it does not prove the answer read the passage correctly. **A teacher checks every pack before students see it** (Section 15).
- **Update old outputs.** If you correct a source, outputs already generated from it do **not** change. Regenerate them.

**Agentic chat.** Chat also has experimental agentic features (web search, running code, creating files). **Programme rule:** never use them for pack work. Packs come from your sources only.

## 2. The eight laws of this programme

Each law marked **(P)** is a *Programme rule* (our local practice). Anything not marked is documented by Google.

1. **Sources control everything. (P)** Whatever is checked is what the AI uses. To change what it says, change the sources and the checkboxes. A prompt only steers *emphasis* inside the checked sources.
2. **Facts from the book; everyday examples from the teacher. (P)** Facts, definitions, rules, dates and methods come only from the textbook. Analogies, local examples, characters and stories come only from your **Teacher Notes** source (Section 5). Both are checkable.
3. **One goal per output. (P)** One video teaches one idea. Three short outputs beat one long one.
4. **The teacher solves; the AI presents. (P)** For any problem with an answer (math, physics, chemistry, grammar parsing), solve and check it in Chat first. Then paste the checked solution into the Studio steering prompt. A video must never be the first place a solution is worked out.
5. **No pack reaches students unchecked. (P)** Use the Teacher Check (Section 15). No signature, no publishing.
6. **No student personal data, ever. (P)** No names, photos, marks or identifiable work in any notebook (Section 16).
7. **Engagement is designed, not hoped for. (P)** Every audio or video output has a hook, a local example, a character or question, and a call to act (Part D); text outputs end with a question or task.
8. **Sacred content is protected in every subject. (P)** No AI recitation of Quran verses, and no depiction of any prophet, companion or angel in any image, in **any** subject: religious education, Arabic texts, history, values. Steer against it, watch the full video, and regenerate if it appears (Section 13.7). Christian education follows its own church's guidance on images, decided by its teacher.

## 3. Verified feature reference

Checked against Google's help pages on 21 November 2026 (Section 21). **"Check" means: confirm in the account you will teach from.**

| Feature | What it gives you | Key facts and limits |
|---|---|---|
| **Configure Chat** | The notebook's conversational role | Styles: **Default** (general research), **Learning Guide** (educational, tutor-like, asks probing questions), **Custom** (a role you write). Plus a response-length setting. |
| **Audio Overview** | Podcast-style audio | Formats: **Deep Dive** (two hosts, in depth, default) · **The Brief** (one speaker, key takeaways, under 2 minutes) · **The Critique** (two hosts give constructive critique) · **The Debate** (two hosts argue perspectives). Length: Shorter / Default / Longer (**Longer is English-only**). 80+ languages. **Interactive Mode** (you join the conversation): **English only**, newly generated overviews only. Customize prompt: focus and expertise level. |
| **Video Overview** | Narrated video with visuals | Formats: **Explainer** (structured, comprehensive) · **Short** (~60 seconds) · **Cinematic** (**18+, English only**). Visual styles (**18+ accounts only; not for Short or Cinematic**): Classic, Whiteboard, Watercolor, Retro Print, Heritage, Paper-craft, Kawaii, Anime, Auto-select, Custom. Optional steering prompt. Can take **more than 30 minutes**. **Review producer notes**: read and adjust the plan before final rendering (once you select Proceed you can't refine it further). Public link sharing is **disabled for Workspace Education accounts**. Language lists differ by format: check that Arabic appears for Short. |
| **Flashcards / Quizzes** | Practice | Customize (pencil): difficulty **easy / medium / hard**, number **fewer / standard / more**, a focus prompt. Flashcards: "Got it!" / "Missed it!", progress saved, retake only missed cards, CSV download. Quizzes: **Hint** and **Explain** buttons. Rolling out since September 2026 (check): editing and adding questions, new question formats (short answer, fill in the blank), and chatting about your last quiz result. |
| **Mind Map** | Concept map of the sources | Web only (not on mobile). |
| **Reports** | Written documents | **Document** reports (templates or suggested formats; **Edit** to customize). **Interactive** reports (web only; a *Learning Overview* template that embeds quizzes, flashcards and mind maps; some content 18+; rolling out). |
| **Infographic / Slide Deck** | Visual summary / slides | **18+ only.** Teachers may generate them for class use; students never need an account. |
| **Notes** | Your saved text | A note can be **converted to a source** (**Convert**, or **Convert all notes to source**). Checked note sources are used in Chat **and** Studio; unchecked ones are excluded. Note sources have their own limit (500 per notebook on the free plan). They **don't count** toward the 50 sources. |
| **Output language** | Language of outputs | **Settings → Output Language** (global; default = your Google Account language). Audio, Video, Flashcards/Quizzes (mobile), Infographics and Slide Decks also have a per-output language choice in their customize panels. Different features support different languages. |
| **Sources** | What the AI uses | Up to **500,000 words or 200 MB** per source. Free plan: **100 notebooks**, **50 sources per notebook** (notes excluded). Paid plans raise this (AI Plus 200/100, AI Pro 500/300, AI Ultra up to 500/600). Workspace editions differ. YouTube: public videos with captions only. |
| **Usage** | How much you can generate | **Compute-based** (prompt complexity, features, number of sources and chat length all count). Refreshes **every 5 hours** up to a **weekly** limit. Workspace Standard Access shows daily caps of about **3 Audio Overviews, 3 Video Overviews**, and **10** each of Reports, Flashcards, Quizzes and Mind Maps (check your edition). Caps for free personal accounts aren't published; record your own for one week. |
| **Mobile app** | Phone use | Sources: PDF, website, YouTube, audio and copied text only. **No** chat configuration, no Mind Maps, no Reports, no note creation. Audio plays offline but can't be downloaded as a file. **Prepare packs on a computer.** |
| **Age** | Who sees what | Users verify age in their Google Account; stricter content policies apply under 18. **18+ only:** Cinematic video, video visual styles, Infographics, Slide Decks, Deep Research, real-time voice chat, some interactive-report content. Workspace for Education: available to **all ages** if the school's admin has turned it on. |

---

# Part B — Setup

## 4. Notebooks and sources

### 4.1 Four kinds of notebook

| Notebook | One per | Contains | Chat style |
|---|---|---|---|
| **Subject notebook** — where packs are made | Grade + Subject + Term, e.g. `Math-P5-T1` | That term's lesson PDFs, Bridge PDFs, the exam Spec, and note sources (Teacher Notes, checked summaries) | **Learning Guide** |
| **Prerequisite Finder** | Subject, across all years, e.g. `FINDER-Math` | **Whole** books from earlier grades (one book = one source) | Default |
| **Master notebook** | Programme | This guide + Google's help pages (Section 21). **Never** lesson chapters. | **Custom** (Section 4.4) |
| **Share notebook** (optional) | Lesson to share | A copy of one lesson set. **Requires student accounts** (Workspace for Education with admin access on), so it isn't used in Phase 1. | Learning Guide |

**Why one notebook per term?** Egyptian textbooks are published per term, and a term's lessons, bridges and spec fit well under the 50-source free limit. Notes don't count toward it. If a term still passes **40** sources, split by unit. Keep 10 free for corrections.

### 4.2 The lesson set — up to five sources per lesson

| Role | Source name (Latin letters, hyphens) | What it is | Counts toward 50? |
|---|---|---|---|
| **Lesson** | `Math-P5-T1-U2-L3-Lesson.pdf` | The lesson pages only (trimmed) | Yes |
| **Bridge** (if needed) | `Math-P5-T1-U2-L3-Bridge.pdf` | Earlier-grade pages this lesson depends on (Section 13.1) | Yes |
| **Notes** | `Math-P5-T1-U2-L3-Notes` | Your Teacher Notes, as a note converted to a source (Section 5) | No |
| **Checked Summary** | `Math-P5-T1-U2-L3-Checked-Summary` | Your checked summary, worked solutions and misconceptions, as a note converted to a source (Section 8, Step 5) | No |
| **Spec** (quizzes only) | `Math-P5-T1-Spec.pdf` | The ministry exam specification for this grade, subject and term | Yes (one per notebook) |

Grade codes: `KG1 KG2 · P1–P6 · Prep1–Prep3 · Sec1–Sec3`.

**Never** add a whole textbook to a Subject notebook, and never add both a book and its chapter files. Duplicated passages confuse retrieval and double the citations. Whole books belong only in the Prerequisite Finder.

### 4.3 Preparing the PDFs (a 5-minute test that saves hours)

Once per term, before step 1: **Create new notebook** → name it `Subject-Grade-Term` → **Add sources** → upload → **Configure Chat → Learning Guide**.

1. **Trim** to the pages you teach. Your trainer gives you the link to the administration's shared library of textbooks, already split into chapters by stage, year, term and subject. Use those files where they exist.
2. **Extraction test.** After uploading, ask in Chat: *"Quote, word for word, the first exercise on page [p]."* Compare with the paper book.
   - **Clean** → continue.
   - **Garbled** (common with scanned pages, equations, Arabic diacritics and tables) → retype the key content (exercises, formulas, rules) into a Google Doc or Markdown file and add that as the Lesson source **instead**, named `…-Lesson`.
3. **Figures.** Diagrams, maps and graphs may not be "read" reliably. Describe each important figure in one line in your Teacher Notes ("Figure 3, p. 41: the water cycle, with 4 labelled arrows…").
4. **Exam spec and assessments.** From the same shared library, open the **Exam specifications** folder for your stage, year, term and subject and add the matching file as the Spec. The **Performance assessments** folder (weekly tasks) holds good examples of question style; use them **in place of the Spec only when no Spec exists for that lesson**.

> *Trainer note:* in the programme repository these are `books/<stage>/year-N/term-N/<subject>/`, `exam-specifications/…` and `performance-assessments/…`. Publish them to teachers as a SharePoint or Drive folder link.

### 4.4 Create the Master notebook (once)

1. **Create new notebook** → name it `MASTER — Teaching with Gemini Notebook`.
2. **Add sources**: this guide first, then the Google help pages listed in Section 21, each as a separate web source.
3. **Configure Chat → Custom** → paste the prompt below → Save.
4. Test: *"List the five roles in a lesson set and the four items of the Teacher Check, with a citation for each."* Missing citations mean a missing source.

```
You are the master assistant for a programme that trains Egyptian teachers to use
Gemini Notebook. Teach from the sources in this notebook only, and cite every factual
claim. If the sources do not cover a question, say so and name the source that would
be needed; never fill gaps from general knowledge. Write for a teacher new to AI:
short sentences, one step at a time, and always name the exact on-screen label
(Sources, Chat, Studio, Add sources, Configure Chat, Audio Overview, Video Overview,
Mind Map, Reports, Flashcards, Quizzes). Separate what Google documents from our
local practice: label local practice "Programme rule". When asked to prepare
training material, give: the goal, the source passages, the teacher's steps, what
students receive, and the Teacher Check. Never ask for, repeat or store any student's
personal data.
```

## 5. The Teacher Notes source — your strongest tool

The AI can only use what its sources contain. The Teacher Notes source is how **you** put your students, your town and your teaching style into every output, without letting the AI invent anything. Write it once per class profile, copy it per lesson, and add the lesson-specific lines.

**How:** in **Studio**, create a note → paste the template → fill it in → **Convert** to source → rename it `…-Notes`.

```
TEACHER NOTES — [Subject] [Grade] [Term] [Unit] [Lesson]
(Programme source written by the teacher. Not part of the textbook.)

STUDENTS: Grade [x], age [y], [urban/rural], reading level [weak/average/good].
They like: [football, mobile games, cooking, market, family trips… — your class's real interests].

EVERYDAY EXAMPLES ALLOWED (use only these):
- [e.g. a koshary plate at the price you checked this week; splitting a loaf of baladi bread into 4]
- [e.g. the microbus from the village to the city: 12 km in 20 minutes]

SERIES CHARACTERS (use the same ones in every lesson):
- [e.g. Uncle Hassan, the grocer, patient and funny]
- [e.g. Malak, 11, always asks "why?"]

KNOWN MISCONCEPTIONS IN MY CLASS:
- [e.g. "1/4 is bigger than 1/3 because 4 is bigger than 3"]

FIGURES IN THE BOOK (one line each):
- [Figure 2, p. 18: number line from 0 to 1 divided into quarters]

LANGUAGE: [e.g. explain in simple Egyptian Arabic; book terms exactly as printed]

AVOID (keep these defaults, add your own):
- interest/riba, alcohol, gambling or betting (including football bets and lotteries), pork, dating or romance
- in mixed classes, religion-specific examples outside religious education
- examples not listed above
(If the book itself teaches a topic such as interest, teach it as printed; add no extra examples of it.)
```

**Rules for the Notes source (P):**
- **Never** include student names, photos or marks. "Malak" is a fictional character, not a student.
- Examples must be **true**: real prices you checked, real places.
- Keep it under one page. Long notes dilute the lesson.

## 6. The select ritual — before every Chat question and every generation

1. In **Sources**, **uncheck all** (including note sources).
2. **Check only** the lesson set this output needs (table below).
3. **Read the checked names aloud.**
4. Then ask your question (Chat) or press **Generate** (Studio).

| Output | Check these |
|---|---|
| Chat prep: P2, P3, P4 | Lesson (+ Bridge if used) |
| P5 misconceptions | Lesson + Notes (+ Bridge if used) |
| P8 exam alignment | Lesson + Spec |
| Study Guide, Mind Map, Flashcards | Lesson + Checked Summary |
| Quiz | Lesson + Checked Summary + Spec |
| Audio, Video | Lesson + Checked Summary + Notes (+ Bridge if used) |
| Parent audio (Section 12.3) | All the unit's Checked Summaries + Notes |
| Unit mixed quiz | All the unit's Lessons and Checked Summaries + Spec (say aloud that you are selecting the whole unit) |

**The Spec covers the whole term.** If quiz questions drift into other lessons, uncheck the Spec and paste the relevant question types from it into the quiz prompt instead.

**Why:** Studio uses the checked sources. Prompt wording such as "only Lesson 3" steers emphasis but does **not** reliably stop Studio from using other checked sources. Forgetting this ritual is the most common cause of a wrong pack.

---

# Part C — Build a lesson pack

## 7. What a pack contains

**Core pack — every lesson (activity subjects: Section 13.11).** One media output per lesson means at most about 6 lessons a day on Workspace Standard's ~3 audio + ~3 video per day. For free accounts, see Section 17.

| Part | Made in | Student use |
|---|---|---|
| **Study Guide** (printable) | Studio → Reports → Document | One sheet to read and revise from |
| **Flashcards** | Studio → Flashcards | Terms, rules, formulas, vocabulary |
| **Quiz** | Studio → Quizzes | Self-test with hints and explanations |
| **One media output** — Audio *or* Video | Studio → Audio Overview / Video Overview | Hear or see the idea before class or at home |

**Extended pack — when time and limits allow:** Mind Map · a second media output (e.g. a 60-second Short as a class hook) · a **Parent audio** (Section 12.3) · Infographic or Slide Deck (teacher-generated, 18+).

The **textbook lesson** is always the reference, never an output. Every pack part must agree with it.

## 8. The workflow — eight steps, in order

> Plan an estimate: the first pack takes about 60–90 minutes of teacher time plus waiting time. Later packs take about 30–40 minutes (a programme estimate, not a Google figure).

**Step 1 — Prepare.** Lesson PDF trimmed, uploaded and extraction-tested (Section 4.3). Notes written and converted. Bridge added if needed. Spec added (Section 4.3, step 4).

**Step 2 — Definitions table (Chat).** Prompt P2 (Section 9.2). Check every row against the book.

**Step 3 — Layered summary (Chat).** P3: per section, then a merged summary.

**Step 4 — Worked solutions and misconceptions (Chat).** P4 for problem-solving subjects: recompute every number yourself. P5 for every lesson: check it against the book.

**Step 5 — Freeze.** Save the checked summary, the worked solutions and the checked misconceptions list (P5) as one note titled `…-Checked-Summary`, then **Convert** it to a source. **Nothing goes to Studio until this exists.**

**Step 6 — Studio, cheapest and easiest to check first:**
**Study Guide → Mind Map (if used) → Flashcards → Quiz → Audio or Video** (core pack: one of them; extended pack: both, audio first).
Text outputs first: errors are found fast and cost little. Audio and video last, because they are heavy, capped per day and slow.

**Step 7 — Video plan check.** Turn on **Review producer notes** before generating. Read the plan: is it one lesson, one goal, in the right language, using your example? Refine the plan there, then select **Proceed**. No changes are possible after Proceed. Generate the day before, never live.

**Step 8 — Teacher Check and filing.** Section 15, then Section 18.

## 9. Prompt library

### 9.1 The two prompt types — don't mix them

| Type | Where | Job |
|---|---|---|
| **Chat prompts** | Chat box | Prepare material the **teacher** checks: definitions, summaries, solutions, misconceptions, gaps |
| **Studio steering prompts** | The pencil (customize) on each Studio tile | Shape what **students** receive: focus, audience, order, tone, language |

Prompts may be written in Arabic or English; state the output language and register inside the prompt.

### 9.2 Chat prompts

Start every Chat prompt with the **header**:
```
From the checked sources only, for [Grade, Subject], in [language and register]:
[TASK]. Cite every row, bullet and answer. If the source does not give something,
write "Not in the source" — do not invent it.
```

**P2 — Definitions table**
```
List every term this lesson defines as a table: Term | Definition exactly as in the
book | Example from the book | Page. Then a separate list "Used but not defined".
```

**P3 — Layered summary**
```
(a) Summarize each section of the lesson in at most 5 bullets, one citation each.
(b) Then merge them into one summary of at most 10 bullets: definitions, rules and
steps only, in the book's order. No examples that are not in the sources.
```

**P4 — Worked solution** (math, sciences, grammar parsing)
```
Solve Exercise [n] on page [p] using exactly the method this lesson teaches (cite
where the book teaches it). Use the book's symbols and notation.
Given: … | Required: …
Rule: the rule or formula from the book, with citation.
Steps: numbered, ONE operation per step, each followed by a short "because …".
Check: substitute the answer back, or estimate it.
Common mistake: the mistake students usually make here, and why it is wrong.
Your turn: one similar exercise with different numbers; give its answer separately,
and label it "AI-made — teacher verifies".
If any value or symbol is unclear in the source, write "unclear in source".
```

**P5 — Misconceptions**
```
Check the lesson and the Notes source. For each misconception listed in Notes, and
any warning the book itself gives ("be careful…", "note that…"): the wrong idea,
the correct idea with a citation from the book, and one question that reveals whether
a student holds the wrong idea. Label the questions "AI-made — teacher verifies".
```

**P6 — Gap check**
```
What do the checked sources NOT cover that a student needs for this lesson? List
gaps only. For each, name the kind of source that would close it. Do not answer the
underlying question.
```
Verify the gaps yourself: the model can invent gaps as well as miss them.

**P7 — Prerequisite finder** (in the Prerequisite Finder notebook)
```
The new lesson is "[title]" ([Grade], [Term]). Using only these earlier-grade books:
list every skill a student must already have for it. For each skill give the book,
grade, term, lesson and page where it was taught, with a citation. Mark any skill not
found as "not found in these books".
```

**P8 — Exam alignment** (Lesson + Spec checked)
```
From the Spec source, list the question types, skills and mark weights that apply to
this lesson. Then check the quiz below against them and list what is missing.
[paste the quiz questions]
```

**P9 — Printable quiz with evidence** (for a paper quiz, or when your account can't export the Studio quiz)
```
Create a [10]-question quiz on this lesson from the checked sources only: [5] multiple
choice and [5] short answer, in the question styles of the Spec source. Each wrong
option is a common mistake from the Checked Summary. Give an answer key that quotes
the book passage behind each correct answer, with its page.
```

### 9.3 The Steering Card — for every Studio output

Fill in all nine lines for **Audio and Video**. For text outputs (Study Guide, Flashcards, Quiz), Notes isn't checked, so leave out START WITH and the Notes half of EXAMPLES. Short, concrete answers work best.

```
AUDIENCE: Grade [x] students in Egypt, age [y], [reading level], short attention.
ONE GOAL: By the end, a student can [verb + skill], e.g. "compare two fractions".
SCOPE: Only "[lesson title]", pages [a–b]. Skip [unit introduction / activities / other lessons].
START WITH: [a question, a puzzle or a mini-story with the series characters from Notes].
ORDER: 1) [ ] 2) [ ] 3) [ ]  (the book's order)
EXAMPLES: Facts and methods from the book only; everyday examples only from Notes.
LANGUAGE: [register — see Part F]; say every key term exactly as the book prints it. Warm, respectful tone; humour from situations, never from people.
PACE: One idea at a time; repeat the main idea in 3 sentences at the end.
END WITH: One question for the student to answer before next class.
```

**Additions by output:**

| Output | Add to the Steering Card |
|---|---|
| **Audio — Deep Dive** | "Two hosts: one explains, one is a curious student who asks the questions my students ask (from Notes)." |
| **Audio — The Brief** | "Only the 3 key takeaways, in under 2 minutes." |
| **Audio — The Debate** | "Argue only positions stated in the book. End by stating what the book concludes." |
| **Audio — The Critique** | "Critique only what the checked sources present; end with the book's rule." |
| **Video — Explainer** | "One idea per scene. Show each key term on screen as written in the book. Refer to the book's figures by page; do not invent diagrams, maps or labels." |
| **Video — Short** | "One idea only: [the idea]. Start with the question in the first 5 seconds." |
| **Video with a solution** | "Present exactly this checked solution, one step per scene. Do not change numbers, symbols or method: [paste]." |
| **Flashcards** | "Front: [term / question / English word]. Back: [definition from the book / answer / Arabic meaning + book sentence]." Set **Difficulty** in the customize panel: easy for new material, medium for revision. |
| **Quiz** | "Match the question types and skills in the Spec source. Each wrong option should be a common mistake from the misconceptions in the Checked Summary. Explanations must quote the book." Set Difficulty and number in the customize panel. |
| **Study Guide** (Reports → Document → Edit) | "One page: key terms with short definitions, the steps or sequence, one worked example from the book, and 5 practice questions with answers. Short sentences. Cite each part." The practice questions are AI-made: check each answer. |
| **Mind Map** | No prompt. Check the branches match the book's headings. |

### 9.4 Chat style per notebook

**Subject notebook = Learning Guide. Master notebook = Custom. Never both in one notebook.**

---

# Part D — Engagement

## 10. Why students switch off, and the design rules

Many students in our schools meet a lesson as dense text they can't read well, in a register they don't speak, with no link to their lives and no early success. Each design rule below answers one of those causes.

| Cause | Design rule | How, in this tool |
|---|---|---|
| Can't read well | **Ear and eye before text** | Audio/Video first; then the Study Guide as a read-along (students follow the text while listening) |
| Formal language feels foreign | **Speak their language, keep the book's terms** | Simple Egyptian Arabic for explanations; every term exactly as printed (Part F) |
| "Why do I need this?" | **Start from their world** | A hook from Teacher Notes: a price, a match, a trip, a puzzle |
| Long lessons lose attention | **One idea per output, short** | Shorts and Briefs; three short items beat one long one |
| No connection to people | **Recurring characters** | The same two characters in every lesson of the term |
| Fear of failure | **Early success, then challenge** | Easy flashcards first, then the quiz at medium (Secondary: hard, Section 11); praise the attempt |
| Forgetting | **Retrieval and spacing** | Quiz the next day; flashcards — retake only missed cards — at the end of the week; mixed quiz at the end of a unit |
| Abstract ideas | **Concrete → picture → symbol** | Real object or story, then a book figure, then the rule |
| Passive watching | **Every output ends with an action** | "Answer this before class", "Use two new words tonight" |

**Tone rules for every steering prompt (P):** warm, respectful, never mocking a wrong answer; humour from situations, not from people; no slang that parents would object to.

## 11. By school stage

| Stage | Media length (target) | Best formats | Approach |
|---|---|---|---|
| **KG** | Parent audio 2 min | Brief audio for **parents**; Short video only with the teacher | Children don't use devices; the teacher plays outputs in class (Section 13.12) |
| **Primary 1–3** | 1–3 min | Short video, Brief audio, easy flashcards | Story with characters, one idea, real objects, lots of repetition; read-along for reading |
| **Primary 4–6** | 3–6 min | Explainer (Whiteboard for math), Brief, flashcards, easy–medium quiz | Concrete example, then figure, then rule; one worked example and one "your turn" |
| **Prep 1–3** | 5–8 min | Explainer, Deep Dive, Debate, medium quiz | Open with a real-life puzzle; misconception first: "Most students think… but…" |
| **Secondary** | 8–15 min | Deep Dive, Critique, Debate, Spec-aligned hard quiz, Mind Map | Exam focus: question types, mark weights, common mistakes, time per question |

Lengths are programme targets. Check the real length of each output; the tool doesn't promise exact durations.

## 12. The classroom loop and distribution

### 12.1 The weekly loop

1. **Before class (home):** students receive the Audio or a Short (Extended pack) and answer one question. *This works only once you've confirmed that your account can download media (Section 21, item 4). Until then, play media in class.*
2. **Class start (5 minutes):** play a 60-second Short as the hook **if you made one (Extended pack); otherwise open with the audio**.
3. **Class:** teach as usual; use the Study Guide on paper.
4. **Class end or next day:** play the Quiz as a team game. The teacher reads the questions aloud; teams answer on paper; use **Explain** on the screen for wrong answers.
5. **End of week:** the teacher shows the flashcards in class, retaking only the cards the class got wrong. For home, download them as CSV and print or share the list.
6. **End of unit:** a mixed quiz across the unit (check all its lesson sources deliberately and say so).

### 12.2 Getting packs to students

- Students in this phase **don't need accounts**. They receive finished, checked files, or see the outputs on the teacher's screen in class.
- **Video public links are disabled on Workspace Education accounts.** Plan to play videos in class, or download and share the file if your account offers download (check).
- Audio on the mobile app plays offline but can't be downloaded as a file. Check web download in your account.
- Families pay for mobile data. Prefer **audio** and **Shorts** for home, and long videos in class.
- Share through the school's approved channel (e.g. the school's Teams or SharePoint channel; a WhatsApp group only if the school runs it — see Section 18). Never post student data with a file.

### 12.3 The Parent audio (one per unit)

Parents are the strongest engagement lever we have. Use The Brief, in simple Egyptian Arabic:
```
For parents of Grade [x] students. In under 2 minutes: what their child learns in
this unit (3 points from the Checked Summary), why it matters in daily life (from
Notes), and 3 simple questions a parent can ask at dinner (for KG: 3 games to
play at home with household objects). Respectful, warm, no jargon. Parents may
not read well; speak simply.
```

---

# Part E — Subject playbooks

Each playbook gives, where the subject needs them: **traps** (what goes wrong in this subject), **best outputs**, **sources**, a **steering add-on**, and **checks** to add to the Teacher Check.

## 13.1 Mathematics (Arabic-medium and English-medium)

**Traps:**
- The AI makes arithmetic or sign errors.
- Equations extract badly from scanned PDFs.
- Audio can't show symbols.
- The video may switch to Western notation when the book uses Arabic notation (س، ص, Eastern Arabic digits, right-to-left layout).
- Generated geometry figures can be wrong.

**Best outputs:**
- **Video Explainer in Whiteboard style** for procedures, built from the checked solution (Law 4).
- **Audio** only for meaning ("what does a fraction *mean*?"), never for long symbol work.
- Flashcards for rules and formulas.
- A quiz with a **wrong option per common mistake**.

**Sources:** Lesson (with the extraction test on exercises), **Bridge**, Notes (with real prices and distances), Spec.

**Prerequisites — the Bridge method (math depends on earlier years):**
1. In `FINDER-Math`, run **P7**.
2. Cut the cited pages from the earlier books into `…-Bridge.pdf`. Start with the book's own "Remember" (تذكّر) boxes if they exist.
3. Add the Bridge to the Subject notebook and check it for audio/video.
4. Steering add-on: *"Start with a 60-second 'Do you remember?' using only the Bridge source, then say how today's lesson uses it."*

**Steering add-on:**
```
Use exactly the book's symbols, digits and layout ([Arabic notation: س، ص and
Eastern Arabic digits] / [English notation]). Do not draw new figures; refer to the
book's figure by page. Present only this checked solution: [paste].
```

**Checks:**
- Recompute **every** number in every output.
- Check the notation matches the book.
- Watch the full worked-solution video.

## 13.2 Sciences (Discover, Science, Physics, Chemistry, Biology, Integrated Sciences)

**Traps:**
- Wrong units.
- Labels on generated diagrams.
- Unsafe "experiments" the book never mentions.
- Mixing up similar terms (mass/weight, heat/temperature).
- Vague cause and effect.

**Best outputs:**
- **Explainer** for processes (photosynthesis, circuits, the water cycle).
- **Deep Dive** with a curious-student host for "why" questions.
- **Debate** for science-and-society topics the book raises.
- Mind Map for classification.
- Flashcards for terms and units.

**Steering add-on:**
```
Describe only experiments and demonstrations in the book, with the book's safety
notes. Use SI units exactly as written in the book. Refer to the book's figures by
page; do not invent labelled diagrams. For every process, say cause → change →
result, in that order. Contrast commonly confused terms from the misconceptions list.
```

**Checks:**
- Every unit and value.
- Every label on any generated visual.
- No experiment outside the book.

**English- or French-medium science:** see Section 14, case C.

## 13.3 Arabic language (reading, grammar, texts and poetry, literature, composition, spelling)

**Traps:**
- AI voices may misplace vowels in classical text and break poetic meter.
- Grammatical parsing (إعراب) must exactly match the book's analysis.
- Diacritics may disappear in extraction.

**Best outputs:**
- **Grammar (نحو):** a P4-style worked parse in Chat. A video presents it one word per scene; flashcards hold rules and examples.
- **Texts and poetry:** Audio **explains** meaning, imagery and the poet's context. **The teacher's own recorded reading, played in class**, is the model reading. Don't add it as a source: it would only be transcribed and would use a source slot. The AI doesn't recite poetry for students to imitate, and never recites Quran verses that appear in Arabic texts (Law 8).
- **Reading (primary):** Short video with the target words on screen; the Study Guide as a read-along with diacritics on key words.
- **Composition:** Critique audio on a **sample essay written by the teacher**; save the essay as a note, Convert it, and check it with Lesson + Checked Summary + that note. Never on student essays with names.
- **Spelling (إملاء):** flashcards for rule plus example words.

**Steering add-on:**
```
Explain in simple Egyptian Arabic (up to Prep; Secondary: mostly MSA, Section 14.1); quote every verse, sentence and example in
Modern Standard Arabic exactly as in the book. Do not recite or read poetry aloud
as a model; explain meaning and imagery. Do not recite Quran verses; refer to them
by page. Parsing must follow the book's analysis word for word.
```

**Checks:**
- Every quotation matches the book letter for letter.
- Every parse matches.
- Diacritics on key words are correct.

## 13.4 English (first foreign language)

**Why students switch off:** English feels useless and frightening in a community that rarely uses it. The fix is meaning first, safety, repetition and small wins.

**Typical errors from Arabic speakers** (put the ones you see into Notes as misconceptions):
- Missing *is/are* ("He happy").
- Missing third-person *-s*.
- *p/b* and *v/f* confusion.
- Articles.
- Adjective after the noun ("a car red").
- Capital letters.
- Spelling by sound.

**Arabic–English balance by stage (P, adjust after trying):**

| Stage | Explanation language | English share in audio/video |
|---|---|---|
| Primary | Simple Egyptian Arabic | ~20%: the lesson's words and sentences only |
| Prep | Arabic and English, half and half | ~50% |
| Secondary | Mostly English | ~80%; Arabic only for hard points and exam tips |

**Best outputs:**
- **Deep Dive vocabulary show:**
  ```
  For each new word: say it in English slowly, twice; give the Arabic meaning; read
  the book's sentence; then one sentence about daily life in Egypt from Notes. Then
  act a one-minute scene using the words ([at a kiosk / meeting a new classmate]).
  End: say the words once more and challenge: "Use two of them at home tonight."
  ```
- **Short video:** one word set or one structure per 60 seconds.
- **Debate:** a simple question using the unit's vocabulary ("City or village?"). Students vote in class.
- **Interactive Mode** (English-only, which fits this subject): the teacher joins an English audio in class and **repeats the students' questions to the hosts in the teacher's own voice**. Students never speak into the device (Law 6: a child's voice is personal data). Unmute the microphone only while you speak, and mute it straight after.
- **Longer** audio length is available because the output is English (secondary listening practice).
- **Flashcards:** front = English word or sentence; back = Arabic meaning plus the book's example sentence.

**Settings:**
- For mixed Arabic–English audio, try Output Language **Arabic** with the mixing rules in the prompt.
- For English-only listening practice, use Output Language **English**.
- Test both before teaching (Section 21).

**Checks:**
- Every English word, spelling and example matches the book.
- Listen to the full pronunciation of the new words.

## 13.5 Second foreign languages (French, German, Italian, Spanish, …)

Same method as English, with these additions:
- Explanation in Arabic at the start (most students begin from zero).
- Put noun **gender** and articles on every flashcard ("la maison").
- Use the book's spelling and accents exactly; run the extraction test on accented letters.
- Interactive Mode and **Longer** audio are English-only, so they're not available here.
- Check that your target language appears in the language list for the format you choose.

## 13.6 Social studies, history, geography

**Traps:**
- Dates, names and numbers drift.
- The AI may add outside facts.
- **Generated maps are unreliable.**

**Best outputs:**
- **History:** a Chat timeline with a citation per event. **Debate** on causes, using *only causes the book states*. Explainer for sequences.
- **Geography:** an Explainer that refers to the book's maps by page. Flashcards for places and terms.
- **Civics topics:** Deep Dive with local examples from Notes.
- **Islamic history** (the Prophet's biography, the early caliphs, Islamic Egypt): Law 8 applies. Steer away from depicting prophets or companions, and watch the full video.

**Steering add-on:**
```
Use only dates, names, numbers and interpretations from the book. Do not draw maps;
say "look at the map on page [p]". In debates, argue only positions the book presents
and end with the book's conclusion.
```

**Checks:** every date, name and number; no generated map shown as fact.

## 13.7 Religious education (Islamic, Christian)

Handle with the greatest care. The **teacher of that religion** makes and checks the pack.

**Rules (P):**
- **Sacred text exactly from the book.** Quran verses, hadith and Bible passages appear only as printed in the book, and are cited.
- **No AI recitation of the Quran.** AI voices can mispronounce, and recitation has its own rules (tajweed). The audio says "the verse on page [p]"; students read it from the book or listen to a qualified human reciter the teacher chooses.
- **Images (Islamic education):** steer the video to show **no depiction of any prophet, companion or angel**. Use calligraphy, landscapes, objects and text. Watch the **full** video before use; regenerate if any such image appears. Christian education follows its own church's guidance on images, decided by its teacher.
- **No Debate or Critique formats on creed or sacred texts.** Use Deep Dive or The Brief to explain meanings, values and behaviour **as the book explains them**.
- Values and stories: only as told in the book; no added details.

**Steering add-on (Islamic education):**
```
Explain meanings and values only as the book explains them. Do not recite or read
Quran verses aloud; refer to them by page. Do not depict any prophet, companion or
angel in any image. Respectful, calm tone.
```

**Checks:** every sacred quotation; every image; the full audio and video.

## 13.8 Philosophy, logic, psychology, sociology (secondary)

**Best outputs:**
- **Debate** and **Critique** formats are excellent here: two hosts argue the positions the book presents.
- Mind Map of schools of thought.
- Flashcards for thinkers, terms and fallacies.

**Steering add-on:** *"Present each thinker's view as the book states it, then a counter-view the book gives; end with the book's evaluation. Use one everyday Egyptian example from Notes per idea."*

**Topics touching religion** (e.g. arguments about God, the soul, creed): **no Debate or Critique**. Use a Deep Dive that presents the book's text; the AI gives no verdict of its own and ends with the book's position.

**Checks:** each view is attributed to the right thinker as in the book.

## 13.9 ICT and programming

**Traps:**
- Menu names and steps differ between software versions.
- Generated code may not run, or may differ from the book.

**Best outputs:**
- Explainer that refers to the book's screenshots by page.
- Flashcards for terms and shortcuts.
- A quiz on "what happens if…".

**Steering add-on:** *"Use the exact menu names, steps and code from the book. Do not invent commands or code. Refer to screenshots by page."*

**Checks:** run every piece of code and every procedure yourself, in the version the school uses.

## 13.10 Values, respect for others, citizenship

**Best outputs:**
- Deep Dive on the book's scenarios.
- Debate on a dilemma the book raises, ending with the book's value.
- A Short as a class discussion starter.

**Steering add-on:** *"Use the book's scenarios and the Notes examples; show respectful disagreement; end with the value the book teaches and one action students can take this week."*

For dilemmas that touch religion, the Section 13.8 rule applies: no Debate; end with the book's position. Law 8 applies to all images.

## 13.11 Activity subjects (art, music, physical education, theatre, educational media)

These are mostly practical. Use the tool only for their **theory pages** (terms, history, safety rules): a Brief audio plus flashcards. The teacher's own demonstration is the core of the lesson, and generated video isn't a substitute for it.

## 13.12 Kindergarten

- **Children don't use devices** in this programme. The teacher plays a Short or Brief in class as a story moment.
- The main KG output is the **Parent audio** (Section 12.3), one per unit: what the child learns in this unit and 3 games to play at home with household objects (from Notes).
- Characters, repetition, one idea, under 2 minutes.

---

# Part F — Language heuristics

## 14. The language matrix

Decide two things for every pack: **the language of the content** (what the book is written in) and **the language of explanation** (what students understand best).

| Case | Example | Output Language | Rule |
|---|---|---|---|
| **A. Arabic content, Arabic explanation** | Arabic-medium math, science, social studies | Arabic | Explain in simple Egyptian Arabic; terms, rules, verses and quotations in the book's Modern Standard Arabic |
| **B. Learning a foreign language** | English, French | Primary and Prep: **Arabic**, with mixing by prompt (test with a Brief first). Secondary: the target language (Sections 13.4–13.5) | The target language for the content itself; Arabic for meaning and support, scaled by stage |
| **C. English- or French-medium subject** | Math_EN, Science_EN, Science_FR in language schools | The book's language | The exam is in the book's language, so key terms stay in it. Add simple-language explanations. Put the Arabic term on flashcard backs to support understanding. |
| **D. Classical or sacred text** | Poetry, Quran, hadith, Bible | Arabic | Quote exactly; never AI-recite the Quran; Bible passages follow the church's guidance; explain only (Sections 13.3, 13.7) |

### 14.1 Register (Arabic)

- **Simple Egyptian Arabic** (polite, clear, no street slang) for explanations in Audio and Video at all stages up to Prep. This is what students hear at home.
- **Modern Standard Arabic** for every term, rule, definition and quotation, exactly as the book prints it. Students must recognise them in the exam.
- Secondary: mostly Modern Standard Arabic, with Egyptian Arabic for asides and examples.
- **Test first.** Whether a given format holds Egyptian Arabic consistently must be checked in your account (Section 21). If the output drifts to formal Arabic, strengthen the prompt: *"Speak as an Egyptian teacher talks to students in class."*

### 14.2 Notation and numbers

- Match the book. If the book uses س، ص and Eastern Arabic digits (١٢٣), say so in every math or science prompt. If it uses x, y and 1 2 3, say that.
- Units as in the book (كجم / kg).

### 14.3 Pronunciation and names

- In Arabic audio, write English or French terms in their own letters inside the prompt ("photosynthesis") so the voice says them correctly. Listen to check.
- Local place names and personal names may be mispronounced. Check the first use; if it's wrong, regenerate or write the name in Arabic letters with diacritics in the Notes.

### 14.4 Mixing languages in one output

Output Language sets the main language. Mixing (Arabic explanation with English words) is done by prompt and **must be tested**: a Brief uses one Audio Overview of the daily cap — test once per format and language, not per lesson — before committing to a Deep Dive or video.

---

# Part G — Quality and operations

## 15. The Teacher Check — four items, no exceptions

The **maker** (the teacher who built the pack):
1. **Citations:** open **3 citations at random** and read each source passage word for word against the output.
2. **Exact content:** check **100%** of numbers, formulas, dates, names, quotations, sacred texts and solutions against the book.
3. **Full media review:** listen to the **full** audio and watch the **full** video (1.5× speed is fine). Check language, register, images, maps, diagrams and the series characters.
4. **Sign:** add your staff code to the file name: `…-v1-YYYY-MM-DD-checked-<maker code>` (Section 18). No signature, no publishing. **If an output has no file** (audio or video you cannot download), **put the same ending on the library item's title.**

The **supervisor** does a separate spot check: 3 citations, the first 60 seconds of each media output, and one random quiz item. Then the supervisor appends `-sv-<supervisor code>` to the file name. The two checks don't replace each other.

> Edition 1's "Check-3" listened to only 60 seconds. That contradicted its own rule to check media in full before use. Edition 2 requires the maker to review the full media.

## 16. Privacy, age and accounts

- **Never upload student personal data** (P): no names, photos, marks with names, or identifiable work. Curriculum pages and teacher-made material only.
- Google: content is **not used to train** its models **unless you give feedback**. Feedback (thumbs up/down) sends the related prompts, sources and outputs for review, kept up to **3 years**, disconnected from your account.
- **Workspace and Workspace for Education accounts:** uploads, queries and responses are **not reviewed by humans**, even with feedback, and **not used to train** models. **Prefer school-managed accounts** for school material.
- **Personal accounts (P):** don't press thumbs up/down. Feedback sends prompts, sources and outputs for human review.
- **Permission to upload (P):** before the programme starts, get written confirmation from the administration that teachers may upload ministry textbooks and exam specifications to Gemini Notebook and share the outputs with students.
- **Age:** teachers generate everything. 18+ features (visual styles, Infographics, Slide Decks, Cinematic) are used by teachers only, and students receive finished files.
- **Workspace for Education** makes Gemini Notebook available to all ages **only where the institution has it and an admin has turned it on**. This administration's library runs on Microsoft 365, so treat Education access as a **precondition to arrange and verify**, not a promise.

## 17. Limits and production planning

- **Free plan:** 100 notebooks; 50 sources per notebook (notes don't count; up to 500 note sources); 500,000 words or 200 MB per source.
- **Usage is compute-based:** refreshes every 5 hours up to a weekly limit. On Workspace Standard Access, expect about **3 Audio + 3 Video Overviews per day** (check your edition).
- **Plan the week** (P): Sunday–Wednesday, make the text outputs and one media output per lesson for the following week. Generate each media output at least one working day before it is taught (Sunday's media on the previous Thursday). Never stack heavy generations live in class.
- Check your remaining usage in the app before starting a heavy generation (Studio may show a cost or usage indicator; check where your account shows it).
- **Free personal accounts:** Google doesn't publish fixed caps. Record what you can generate in one week and plan from that.

## 18. The Microsoft 365 library — where checked packs live

- **One SharePoint document library** is the single source of truth, with three states: **Draft → Review → Published**.
- **Roles:**
  - The teacher (maker) creates the pack and does the maker check.
  - The supervisor does the spot check.
  - The **publisher** moves a pack to Published. This is the person the administration names for each subject (e.g. the senior subject supervisor), never the maker of the same pack.
- **Nine columns:** Grade, Subject, Term, Unit, Lesson, Part, Language, Teacher, Status. Columns are how a library groups, filters and tracks its contents (Microsoft Support: *Create a column in a list or library*).
- **File name** (Latin letters, hyphens only), the same pattern as the source names in Section 4.2:
  `Subject-Grade-Term-Unit-Lesson-Part-v1-YYYY-MM-DD-checked-<maker>-sv-<supervisor>`
  Example: `Math-P5-T1-U2-L3-Quiz-v1-2026-11-21-checked-T014-sv-SV01`. Use staff codes, not full names.
  Part codes: `StudyGuide, MindMap, Flashcards, Quiz, Audio, Video, ParentAudio, Infographic, Slides`.
- **Getting each part out of the notebook** (check in your account; only the flashcard CSV is confirmed on the help pages for every account):

| Part | How to file it |
|---|---|
| Study Guide (Report) | Copy it into a Word document, or export it if your account offers that |
| Flashcards | Download CSV |
| Quiz | Copy the questions, options and answer key into a Word document |
| Mind Map | Screenshot, or download if offered |
| Audio / Video | Download if your account offers it; otherwise record the notebook name and output title in the library item |
| Infographic | Download PNG if offered (check) |
| Slide Deck | Download or export if offered (check); teacher-only (18+) |
| Parent audio | As Audio |

- **Corrections:** fix the source, regenerate the output (old outputs don't update), save it as `v2`, and repeat the check.
- **Recall (P):** if an error is found after publishing:
  1. Move the item back to Review.
  2. Delete the file wherever you still can.
  3. Send one short correction message telling everyone to delete v1.
  4. Publish `v2`.

  Forwarded or downloaded copies can't be recalled, which is one more reason to check before publishing. Prefer a school-managed channel to a WhatsApp group, which exposes families' phone numbers.

## 19. Train the trainer

**The cascade:** trainers teach AI technicians → technicians teach teachers → teachers make packs. Everyone teaches from this guide and keeps a copy of the Master notebook.

**A technician is ready when they can, live and unaided:**
- ☐ Create a term Subject notebook, add a trimmed lesson and run the extraction test
- ☐ Write a Teacher Notes note and convert it to a source
- ☐ Perform the select ritual for each output type (Section 6 table)
- ☐ Run P2, P3, P4, P5 and P7; freeze and convert the Checked Summary
- ☐ Fill in a Steering Card for their own subject, using the Part E add-on
- ☐ Use Review producer notes to fix a video plan before rendering
- ☐ Perform the full Teacher Check aloud, and find **one error the assessor planted**
- ☐ State the privacy, age and limit rules without notes
- ☐ File a pack with the correct columns and checked file name

**The technician's 60-minute session for teachers:**

| Minutes | Content |
|---|---|
| 0–5 | Play a 60-second Short made for the session (an Explainer if Short isn't available) |
| 5–15 | What the tool does and doesn't do; the eight laws |
| 15–35 | Live build: one lesson, from the extraction test to the Checked Summary to **Flashcards** (fast) as the live Studio output, teachers following on laptops. Then show a video made the day before, since video can take more than 30 minutes. |
| 35–45 | Their subject's playbook (Part E) and Steering Card; the gap check live |
| 45–55 | Hands-on: each teacher writes Teacher Notes and starts a pack for a lesson they teach next week |
| 55–60 | The Teacher Check, filing, and the first-week commitment: **one checked pack, filed** |

**Keep the record current:** before each new cohort, reopen the help pages in Section 21 and compare names, limits and formats with the app. Record every local decision as a dated note labelled "Programme rule" in the Master notebook.

## 20. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| The output covers other lessons | Extra sources were checked | Select ritual (Section 6); regenerate |
| "Gemini Notebook can't answer this question" | The sources don't cover it, or the wording is unclear | Rephrase; run P6; add the missing source |
| Equations or diacritics come out garbled | Scanned PDF | Run the extraction test; retype the key content as a Doc or Markdown source |
| Wrong numbers in a video | The video worked out the solution itself | Law 4: paste the checked solution into the steering prompt |
| Audio too formal or too fast | Register and pace not specified | Add the Part F register line and "one idea at a time; slow pace" |
| English terms mispronounced in Arabic audio | Term written in Arabic letters | Write the term in English letters in the prompt |
| Wrong map, label or diagram in a video | A generated visual | "Refer to the figure on page [p]; do not draw it"; regenerate |
| Images of prophets in an Islamic education video | Image generation | Section 13.7 steering line; regenerate; full check |
| A corrected source but the output didn't change | Outputs don't update | Regenerate; save as v2 |
| A daily or weekly limit was reached | Usage caps | Section 17 plan; text outputs first |
| Can't make a Mind Map or Report on the phone | Not supported on mobile | Use a computer |
| Students don't watch | Too long, no hook, no follow-up | Switch to a Short or Brief; hook from Notes; quiz game next class |

## 21. Sources and what is still to verify

**Google help pages (add to the Master notebook as web sources):**
- Learn about Gemini Notebook — https://support.google.com/gemininotebook/answer/16164461
- Add or discover sources — https://support.google.com/gemininotebook/answer/16215270
- Use chat (Configure Chat) — https://support.google.com/gemininotebook/answer/16179559
- Audio Overviews — https://support.google.com/gemininotebook/answer/16212820
- Video Overviews — https://support.google.com/gemininotebook/answer/16454555
- Flashcards and Quizzes — https://support.google.com/gemininotebook/answer/16958963
- Notes — https://support.google.com/gemininotebook/answer/16262519
- Reports — https://support.google.com/gemininotebook/answer/18323649
- Usage limits — https://support.google.com/gemininotebook/answer/17670842
- Plans and limits — https://support.google.com/gemininotebook/answer/16213268
- Workspace editions — https://support.google.com/gemininotebook/answer/16337734
- Privacy — https://support.google.com/gemininotebook/answer/17004255
- Mobile app — https://support.google.com/gemininotebook/answer/16296687
- Output language — https://support.google.com/gemininotebook/answer/16261963
- September 2026 learning tools — https://workspaceupdates.googleblog.com/2026/09/new-back-to-school-features-and-learning-tools-available-in-Gemini-Notebook.html

**Microsoft:** Create a column in a list or library — Microsoft Support.

**Still to verify in the account you will teach from:**
1. Short Video Overview is available and Arabic is in its language list.
2. Whether Audio and Video hold **Egyptian Arabic** consistently, and whether Arabic–English mixing works (Section 14.4).
3. Whether a Study Guide template appears under Reports → Document (otherwise use Edit with the Section 9.3 Study Guide line).
4. Whether audio and video can be **downloaded** on the web in your account type.
5. Which new quiz features (editing, short answer, fill in the blank, chatting about results) have reached your account.
6. Whether diacritics on key words survive in the Study Guide.
7. The daily caps for your exact Workspace edition.
8. Workspace for Education access, if the programme intends to rely on it.
9. Whether the Arabic prompts (Arabic guide, Section 9) work as well as the English in Chat and in the Studio steering box. Test with one Brief.

## 22. What changed from Edition 1

| Edition 1 | Edition 2 | Why |
|---|---|---|
| One notebook per Grade + Subject; select only one source | One notebook per **Grade + Subject + Term**; a **lesson set** of up to 5 roles | Prerequisites and local examples need their own sources; books are published per term |
| Grounding seen as blocking engaging examples | **Teacher Notes** source: facts from the book, examples from the teacher | Engagement without invention |
| "Checked summary" saved as a note | Note **converted to a source** | A plain note isn't a source; a converted, checked note source is used by Chat and Studio |
| Studio order: Study Guide, Mind Map, Audio, Video, Flashcards, Quiz | Study Guide, Mind Map, Flashcards, Quiz, Audio, Video | Cheap, checkable outputs first; heavy, capped ones last |
| Check-3: first 60 seconds of media | Teacher Check: full media review by the maker; spot check by the supervisor | Edition 1 contradicted its own "check in full" rule |
| Formal Arabic everywhere | Register by stage and subject (Part F) | Students understand simple Egyptian Arabic; exams need the book's terms |
| Short "unverified" | Short (~60 s) documented; Arabic availability to check | Help page now lists Explainer, Short, Cinematic |
| Cinematic: Ultra-only, 18+ | Cinematic: 18+ and English-only | Help page; not usable for Arabic packs in any case |
| — | Producer-notes plan review before rendering | New: catch errors before a 30-minute render |
| — | Subject playbooks (Part E) and language matrix (Part F) | Each subject fails in its own way |
| — | Daily caps on Workspace, Education link sharing disabled, mobile limits | Real production and distribution constraints |
| — | Math Bridge method with a Prerequisite Finder notebook | The tool doesn't look back to earlier grades by itself |
| — | Religious education rules (no AI recitation, no depiction of prophets; now Law 8 for all subjects) | Accuracy and respect |
| — | Parent audio, classroom loop, distribution | Engagement happens around the pack, not only inside it |
| — | Law 8: sacred content protected in every subject | Verses and prophets appear in Arabic, history and values books too |
| — | Default AVOID list, upload permission, recall procedure, nine library columns, one file-name pattern | Second review: closing gaps between sections |
| Separate inserts: "5-Stage Prompt Sequence" and "Split / Summarize / Prompt cheat sheet" | Merged into Section 24 and Appendix A. The separate inserts are **withdrawn**. | Both still taught Edition 1 rules: one source per lesson, a 7-part pack, Check-3, formal Arabic, the old Studio order, "no fixed daily number", Cinematic as "Ultra-only", 6 library columns |
| Research guide (Edition 1, Section 5) | Section 23, with the Research Brief and Contradiction Check | Kept, and separated from lesson notebooks |
| Lecture map for the 19-slide Phase 1 deck | Replaced by the pilot-day deck and its slide-to-section map (`pilot-day-session-pack.md`) | The old deck teaches Edition 1 rules; retire or update it |
| — | Section 26: the Prompt Builder (ChatGPT, Claude, Gemini) and `prompt-builder.md` | Prompts are generated with the subject rules built in, so teachers make fewer errors |
| "Quiz with evidence" prompt | P9 (Section 9.2) | Gives a printable quiz with an answer key, since the help pages do not confirm an export for Studio quizzes |

**Edition 2.1 — 26 November 2026** (edit list: `docs/EDITION-2-REVIEW.md`):
- Reading path corrected: Parts A–D, then Sections 15–18 and 20; print Appendix A.
- P5 misconceptions is now part of Step 4 (with P4) and has its own select-ritual rows (Section 6, Quick Card).
- Subject-notebook setup added (Section 4.3): create the notebook, add sources, Configure Chat → Learning Guide.
- Quick Card: Audio/Video prompts cover all nine lines; Study Guide, Flashcards and Quiz drop Start with and Notes examples.
- An output with no file is signed on the library item's title (Section 15).
- Contradiction fixes: Spec in Step 1; weekly-loop media counts; retyped Lesson source named `…-Lesson`; Critique row and the sample-essay note; tone on the LANGUAGE line; distribution channel; matrix row D (Quran never AI-recited; Bible per church guidance); Law 7 scope; Stage 4 video sources; playbook scope; 13.3 register scope; Brief cap note.
- §9 now allows Arabic or English prompts; §21 item 9 tests the Arabic prompt wordings.

---

# Part H — Programme delivery

## 23. Research method — when you need evidence for a new claim

Use this when a trainer needs evidence for a new feature, limit or teaching claim. It is not for lesson packs. Work in the **Master notebook** (or a separate `RESEARCH-<topic>` notebook), **never in a Subject notebook**, so discovered web pages never enter a lesson set.

1. **Ask one narrow question.** "Which source types can a teacher add?" beats "Tell me about sources."
2. **Find sources.** In **Add sources**, use the option to search for or discover web sources for your question (check where your account shows it), or add pages you already know. Keep only sources that actually answer the question. Prefer, in this order: Google's help pages and official blogs, then ministry and administration documents, then everything else.
3. **Interrogate with citations.** Use the Research Brief below. Click each citation and read the passage in context.
4. **List the gaps, then verify them.** Run P6. The model can invent gaps as well as miss them.
5. **Freeze the finding.** Save the verified answer as a note: the question, the answer, the source names and the date checked. Label local decisions "Programme rule". The next trainer inherits it.

**Research Brief**
```
QUESTION: [one narrow question]
1. Answer only from the checked sources.
2. One claim per bullet, each with a citation. Quote the key sentence where the
   exact wording matters (numbers, limits, ages, dates).
3. Separate "Google documents this" from "our programme practice".
4. End with two lists: (a) what the sources do NOT cover; (b) what a person must
   verify outside this notebook, and where.
```

**Contradiction Check**
```
Where do the checked sources disagree about [topic]? Quote both passages with
citations, say which source is more authoritative and why (official help page >
official blog > third-party site), and what a teacher should do until it is resolved.
```

> A citation shows which passage an answer rests on; it doesn't prove the passage was read correctly. For any number, date, limit or age rule that teachers will act on, open the passage and compare it word for word.

## 24. Onboarding stages for the Master notebook

Don't upload this guide and ask the notebook to "implement everything" (Section 1). Work through these stages in order. **A stage is passed only by a named artefact that the next stage uses, never by a fluent answer.** At every stage: standard chat only, a citation for every point, agentic features off.

| Stage | What you do | Pass artefact |
|---|---|---|
| **0 — Setup** (not a chat prompt) | Create the Master notebook (Section 4.4): this guide plus the Section 21 pages as separate sources. **Configure Chat → Custom** with the Section 4.4 prompt → Save. | A configured Master notebook |
| **1 — Test understanding** | Check only this guide, then ask the Stage 1 prompt below | Cited answers that match the guide |
| **2 — Gaps** | Ask: *"What does this guide NOT cover about training teachers in our schools? List gaps only; do not invent them."* Verify each gap against the guide. | A verified gap list, saved as a dated note |
| **3 — One pack** | In a **new Subject notebook** (never the Master): one real lesson, the full Section 8 workflow, one output at a time. Never ask for the whole pack in one prompt. | One pack that passed the Teacher Check |
| **4 — Video, in Studio** | Not in Chat. **Studio → Video Overview → Explainer**, with the Section 6 video sources checked, the Steering Card pasted and **Review producer notes** on. The day before, never live. | A checked video, watched in full |
| **5 — Teach-back** | Ask the Stage 5 prompt below. The technician then builds live while observed. | A live build, one planted error corrected, one pack filed (Section 19) |

**Stage 1 prompt**
```
From this guide only: list the five roles in a lesson set, the parts of the core
pack, the eight laws (one line each), and the free-plan and usage limits. Cite each
point. What must never be uploaded?
```
Pass only if the answer includes, with citations:
- 100 notebooks and 50 sources (notes excluded)
- 500,000 words or 200 MB per source
- compute-based usage, refreshing every 5 hours up to a weekly limit, with daily caps on Workspace editions
- no student personal data

If it can't answer cleanly, fix the sources before going further.

**Stage 5 prompt**
```
Act as a trainer. Using only this guide, teach me step by step how to build a lesson
pack for a History lesson in Prep 2. Stop after each step and ask me to confirm
before you continue.
```

**Pacing tip:** on Workspace editions with about 3 audio and 3 video generations per day, plan at most one Deep Dive and one video per teacher per day while learning.

## 25. The training video — turning a session deck into a Video Overview

For trainers who want a narrated recap of a training session, for teachers who missed it or to watch before it.

1. Add the session deck to the **Master notebook** as `Training-Slides-YYYY-MM-DD`. A PDF export, the .pptx file or Google Slides all work as sources.
2. **Check only that source**, not this guide. Otherwise the video narrates the whole method instead of the session.
3. **Studio → Video Overview → Explainer** → pencil → paste the prompt below → turn on **Review producer notes**.

```
AUDIENCE: Egyptian school teachers who have never used Gemini Notebook, watching
together in a training room or at home.
ONE GOAL: By the end, a teacher can build one checked lesson pack.
SCOPE: Only the slides in this source, in their order.
START WITH: The problem: students lose the lesson at home, where they only have
the textbook page.
ORDER: 1) What the tool does and does not do 2) Sources, Chat, Studio 3) The lesson
set and Teacher Notes 4) The select ritual 5) The pack 6) The Teacher Check
7) Privacy and sacred-content rules 8) This week's action.
LANGUAGE: Clear, simple Arabic. Keep the on-screen English labels (Sources, Chat,
Studio, Audio Overview, Video Overview) exactly as they appear in the app.
PACE: One idea per scene; define every term the first time it is used.
END WITH: "This week: one lesson, one checked pack, filed."
```

4. **Recap:** a **Short** with one line: *"In about 60 seconds: one lesson in, one checked pack out — study guide, flashcards, quiz, and one audio or video — made and checked by the teacher."* First check that Short offers Arabic in your account; if it doesn't, use a short Explainer.
5. **Listen-ahead audio:** **Audio Overview → Deep Dive** for the full session, or **The Brief** as a reminder: *"Explain this session for a teacher new to Gemini Notebook. Focus on the lesson set, Teacher Notes, the Teacher Check and the first-week action."* Interactive Mode is English-only, so don't promise it for Arabic.
6. Generate everything the day before, and give the video a full Teacher Check.

## 26. The Prompt Builder — let ChatGPT, Claude or Gemini write the prompts

To cut teacher workload and errors, a trainer sets up one assistant with the system prompt in `prompt-builder.md` and this guide as its knowledge file. The assistant can be a ChatGPT GPT or Project, a Claude Project, or a Gemini Gem.

**How teachers use it:** the teacher sends a short form (grade, subject, term, lesson, pages, outputs, class profile). For each output, the builder returns:
- where to paste the prompt
- which sources to check
- the panel settings
- the finished prompt, with the subject's rules built in
- what to check afterwards

It can also **review** a teacher's own prompt, **diagnose** a bad output and **plan** a unit.

**Rules (P):**
- The builder writes **prompts only**. It never sees the textbook, so it must not write lesson content or solve exercises. Gemini Notebook does that from the sources, and the teacher checks the result.
- No student data goes into the builder, ever.
- Run the acceptance tests in `prompt-builder.md` before rollout and after every change. Keep the builder's rules in step with this guide.
- The Teacher Check (Section 15) still applies to every output.

## Appendix A — Teacher Quick Card (print one per teacher)

Replaces the Edition 1 "Split / Summarize / Prompt cheat sheet".

**Notebook:** one per Grade + Subject + Term (`Math-P5-T1`).
**Lesson set:** Lesson · Bridge (if needed) · Notes · Checked Summary · Spec (quizzes only). Never a whole book, and never a book plus its chapters.

**Before every question or generation:** uncheck all → check only what this output needs → read the names aloud → ask or Generate.

| Output | Check |
|---|---|
| Chat prep | Lesson (+ Bridge) |
| P5 misconceptions | Lesson + Notes (+ Bridge if used) |
| P8 exam alignment | Lesson + Spec |
| Study Guide, Mind Map, Flashcards | Lesson + Checked Summary |
| Quiz | Lesson + Checked Summary + Spec |
| Audio, Video | Lesson + Checked Summary + Notes (+ Bridge) |

**Workflow:**
1. Prepare + extraction test; Spec added (Section 4.3, step 4)
2. Definitions (P2)
3. Layered summary (P3)
4. Worked solutions (P4) + misconceptions (P5)
5. Freeze + **Convert** to source
6. Studio: Study Guide → Mind Map (if used) → Flashcards → Quiz → Audio or Video
7. Producer-notes check
8. Teacher Check + file

**Short on time?** Send the lesson form to the Prompt Builder (Section 26) and paste what it returns.

**Every Chat prompt starts with:** *From the checked sources only, for [Grade, Subject], in [language]: [task]. Cite everything. If the source doesn't give it, write "Not in the source".*

**Every Audio/Video prompt covers all nine lines:** Audience · One goal · Scope (pages, what to skip) · Start with · Order · Examples (facts from the book, examples from Notes) · Language · Pace · End with. **Study Guide, Flashcards and Quiz:** no Start with, and book examples only.

**Teacher Check:**
- 3 random citations read word for word
- 100% of numbers, formulas, dates, names, quotations, sacred texts and solutions
- the full audio and video
- sign: `…-v1-YYYY-MM-DD-checked-<code>`

**Never:**
- student names, photos, marks or voices
- AI recitation of the Quran, or images of prophets
- Debate or Critique on creed, sacred texts or religious topics
- agentic or web mode for packs
- Cinematic for Arabic packs (English-only)
- mind maps or reports on a phone
- video generated live
- a pack published without a signature

---

*Prepared for the teacher-training programme of the local education administration. Features and limits are as documented by Google and Microsoft on the pages in Section 21, checked on 21 November 2026, and may change.*
