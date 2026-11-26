MASTER RECORD · PHASE 1 · SCHOOL CONTENT PROGRAMME
Gemini Notebook
Master Notebook Guide
One document to create the master notebook, generate the teaching video for the Phase 1 lecture,
run the research, and train the trainers.
Upload this PDF as the first source in a new notebook in Gemini Notebook (formerly NotebookLM), and
add the official pages listed in Section 8. The notebook then holds the lecture method, the prompts, and
the evidence behind every claim in the slideshow — so you, and the AI technicians you train, teach
teachers the same way, from the same record.
What this guide gives you
Section 3 — Master setup prompt: paste it into Configure Chat to give the master notebook its job.
Sections 4–5 — Video prompts and research guide: turn the Phase 1 slideshow into a narrated
Video Overview, and research new topics without inventing facts.
Sections 6–7 — Method and lecture map: how to split, summarize and prompt, and which source
backs each part of the lecture.
Section 8 — Verified source library: the official links to add as sources and to cite when a teacher
asks “says who?”
Sections 9–10 — Rules and cascade: limits, privacy, age, education access, the Microsoft 365
library, and the train-the-trainer routine.
Sections 11–12 — Staged use and retrospective: the five-stage prompt sequence, and what the
adversarial review changed.
Corrected edition — 17 November 2026. This edition replaces the first edition after a retrospective
and three adversarial reviews. The first edition's rule “one notebook per unit” is withdrawn. The rule
throughout is now: one notebook per Grade + Subject, one source per lesson, select only that
lesson source before every generation. Section 12 lists every correction.
Names in this guide. Google renamed NotebookLM to Gemini Notebook on 16 July 2026 and
describes it as the same standalone product. Teachers will see both names. In the app, keep the
English tab and button labels exactly as shown — Sources, Chat, Studio, Add sources, Audio
Overview, Video Overview, Flashcards, Quizzes, Mind Map, Reports. Source: Google Workspace Up
dates — NotebookLM is now Gemini Notebook.
Gemini Notebook Master Notebook Guide 1

1. Create the master notebook — setup steps
Do this once. Every later lecture, video and research task starts from this notebook. These are setup
steps only, excluding generation: a Video Overview alone can take more than 30 minutes (Section 4), so
no honest promise can include a finished video in a 15-minute setup.
1. Open Gemini Notebook and select Create new notebook. Name it: MASTER — Teaching Teachers
Gemini Notebook. Source: Create a notebook in Gemini Notebook.
2. Select Add sources and upload this PDF first.
3. Add the official pages from Section 8 as web sources, starting with Learn about, Add or discover new
sources, Use chat, and the Audio and Video Overview pages.
4. In the Chat panel, select Configure Chat, choose Custom, and paste the master setup prompt from
Section 3. Save.
5. Ask the test question: “List the 7 parts of a complete lesson pack — 6 generated outputs plus the
source chapter — with a citation for each part, and state the limits.” No citation means a missing
source.
6. Generate one Audio Overview and one Video Overview from Section 4 and check them in full before
use — generated output can contain inaccuracies.
Keep the master notebook clean
One master notebook for the method, and it never holds lesson chapters. Lesson packs are made in
subject notebooks — one notebook per Grade + Subject (Section 6) — never mix the two jobs.
Name every source clearly, for example Official-Help-Audio-Overview.
When Google changes a feature or a limit, replace the old source with the current help page; limits are
subject to change.
Never add student names, student work with names on it, or any personal data as a source. See
Section 9.
2. The lesson pack this programme produces
The lecture teaches one repeatable product: one lesson = one pack — 7 parts in total: 6 generated
outputs plus the original chapter. The chapter is a source, never an output. File naming is in Section 9.
Pack part Made in Student use
Audio Overview Studio → Audio Listen on the way home; replay hard parts
Overview
Video Overview (Explainer; Short is about Studio → Video Watch the idea before reading it
60 seconds) Overview
Mind Map Studio → Mind Map See how the ideas connect
Flashcards Studio → Flashcards Memorize terms, dates and formulas
Quiz Studio → Quizzes Test yourself; read the explanation for each
wrong answer
Study Guide (printable) Studio → Reports One paper sheet to revise from at home
Original chapter Sources The textbook text every part must match
Gemini Notebook Master Notebook Guide 2

3. Master setup prompt — paste into Configure Chat
In the master notebook, open the Chat panel, select Configure Chat, choose Custom, paste the text
below, and select Save. Google lists three conversational styles — Default for general research, Learning
Guide for educational content, and Custom for a style or role you define — plus a response-length choice.
Custom is the right choice here because the notebook has a teaching job, not a general one. Source: Use
chat in Gemini Notebook.
You are the master teaching assistant for a school programme that trains
teachers to use Gemini Notebook (formerly NotebookLM).
Your job:
1. Teach from the sources in this notebook only. Every factual claim
must carry a citation to the source passage it came from.
2. If the sources do not cover a question, say exactly that and list
what source would be needed. Never fill a gap from general knowledge.
3. Explain for a teacher who is new to AI: short sentences, one idea
per step, and always name the exact on-screen label to click
(Sources, Chat, Studio, Add sources, Audio Overview, Video Overview,
Flashcards, Quizzes, Mind Map, Reports, Configure Chat).
4. When asked to prepare teaching material, produce it in this order:
learning goal, the source passages it rests on, the steps the
teacher performs, the output students receive, and Check-3
(Section 6: three citations opened and read, the first
60 seconds of audio heard, the first 60 seconds of video seen).
5. Keep a strict line between what Google documents and what is our
local programme practice. Label local practice as "Programme rule",
never as a Google feature.
6. Never ask for, repeat, or store student personal data.
First three questions to ask the configured notebook
1. “Summarize this master record in 10 bullets, one citation per bullet.”
2. “What do my sources NOT cover about teaching Gemini Notebook to teachers? List the gaps only.”
3. “Turn Section 6 into a 20-minute mini-lesson plan for a new trainer, with timings.”
Why the grounding rule works — stated precisely. In its default mode, Chat answers from your
sources, and Google notes that a request the sources cannot support can return “Gemini Notebook
can’t answer this question.” That refusal is a feature for a school programme: it is the signal that a
source is missing, not a failure to hide. But grounding is no longer absolute: newer agentic chat
features can search the web or run code, with or without sources, on higher plans. Programme rule:
lesson packs are made in default chat only. Never use agentic or web-search mode for a pack.
Source: Use chat in Gemini Notebook. Styles are set per notebook: this Custom prompt belongs to
the master notebook only; lesson notebooks use Learning Guide (Section 6). Never prescribe both
for the same notebook.
Gemini Notebook Master Notebook Guide 3

4. Video prompt — turn the slideshow into a teaching video
A Video Overview transforms the sources in the notebook into a narrated video that explains them; it is not
a free-form video generator. Add the lecture deck as a source named Lecture-Phase1-Slides, select
only that source — not this guide, which would make the video narrate the method too — then open
Studio → Video Overview, open the customize (pencil) option, and use the prompt below.
Video Overview steering prompt — Explainer format
Create a teaching video for school teachers who have never used
Gemini Notebook. Audience: teachers in a local education
administration, watching together in a training room.
Cover, in this order, using only the slideshow source:
1. The problem: learning is lost at home, where a student has only
the textbook page.
2. What Gemini Notebook is: you add your own sources, and it answers
and creates only from them, with citations you can click to check.
3. The three panels: Sources, Chat, Studio.
4. One lesson = one pack: Audio Overview, Video Overview, Mind Map,
Flashcards, Quiz, and a printable Study Guide.
5. The live example: a Biology photosynthesis chapter becomes a pack.
6. Check-3, the rule to never upload student personal data,
and where packs live: the Microsoft 365 library,
Draft to Review to Published.
Speak in clear, formal Arabic. Keep the on-screen English labels
(Sources, Chat, Studio, Audio Overview, Video Overview) in English,
exactly as they appear in the application.
Go slowly. One idea per scene. Define every term the first time
you use it. End with the first-week action: one pack, checked, filed.
Short version — the 60-second recap
Whether Short is available on a free account is unverified. Check it in the account you will teach from
first; if it is not there, open with a short Explainer instead. Where Short is available, generate a second
video in the Short format: “Recap in about 60 seconds: one chapter in, one complete student pack out —
audio, video, mind map, flashcards, quiz, study guide — checked by a teacher and filed in the shared
library.”
Audio version — for teachers to listen to before the session
In Studio → Audio Overview: Deep Dive (two hosts, in-depth) for the full lecture as a listen-ahead, or The
Brief (one host, key takeaways in under two minutes) as a reminder. Instruction: “Explain the lecture for a
teacher new to Gemini Notebook. Focus on the pack, Check-3, and the first-week action.” Audio
Overviews can be generated in 80+ languages. Interactive Mode for audio is English-only; do not promise
it for Arabic packs. Source: Generate Audio Overview in Gemini Notebook.
Plan the time honestly. Google warns that a Video Overview can take a while — sometimes more
than 30 minutes — and that video and audio output are AI-generated and may contain inaccuracies
or audio glitches. Generate the day before, check in full, and regenerate a flawed take. The Explainer
format is the right default for teacher training. Never demo Cinematic on a free account: it is Ultra-
only (paid) and 18+, so a free teacher will not see it. Source: Generate Video Overviews in Gemini N
otebook.
Gemini Notebook Master Notebook Guide 4

5. Research guide — how the notebook researches a new
topic
Use this sequence whenever a trainer needs evidence for a new claim, a new feature, or a new lecture. It
is written for the notebook’s own source discovery and for a human researcher working beside it; the
verification steps are identical.
The five steps
1. State the question narrowly. One question per research run: “What source types can a teacher
add?” beats “Tell me about sources.”
2. Discover sources. In Add sources, type the research question in the search box to find sources from
the web or from Workspace files, then select only the sources that actually answer it. Prefer Google’s
own help and blog pages, then the school’s official curriculum documents. Source: Add or discover ne
w sources for your notebook.
3. Interrogate with citations. Ask the research prompts below. Every answer must quote or cite the
passage it rests on; click the citation and read the passage in context before trusting it.
4. List the gaps. Run the gap prompt — then verify the answer, because the model can invent gaps as
well as hide them. A topic with verified named gaps is ready to teach honestly; a topic with hidden
gaps is not.
5. Freeze the finding. Save the verified answer as a note in the notebook, with the source names and
the date checked. Notes become part of the record the next trainer inherits.
Research prompts — copy and reuse
RESEARCH BRIEF
Question: [one narrow question]
1. Answer only from the sources selected for this question.
2. Give each claim its own bullet, with a citation to the exact
passage. Quote the key sentence where wording matters.
3. Separate "Google documents this" from "our programme practice".
4. End with two lists: (a) what the sources do NOT cover,
(b) what a human must verify outside this notebook, and where.
GAP CHECK
What do my sources NOT cover about [topic]? List only the gaps.
For each gap, name the kind of source that would close it
(official help page, curriculum document, administration decision).
Do not answer the underlying question and do not invent coverage.
CONTRADICTION CHECK
Where do my sources disagree about [topic]? Quote both passages
with citations, name which source is more authoritative and why,
and state what a teacher should do until the disagreement is resolved.
A caution that belongs in every research run: a citation shows which passage an answer rests on; it does not prove the
passage was read correctly. For any number, date, limit or rule that teachers will act on, open the cited passage and
compare it word for word.
Gemini Notebook Master Notebook Guide 5

6. Split, summarize, prompt — the method teachers learn
The canonical rule — one rule, everywhere
One notebook per Grade + Subject. One source per lesson. Select-only-one.
Notebook = one Grade + one Subject, for example Grade 3 — Biology. Never one notebook per
unit, per chapter or per lesson, and never one notebook for a whole school. Source = one lesson
chapter, trimmed to the pages actually taught, named Subject-Grade-Unit-Lesson.pdf, for example
Biology-G3-Unit2-Photosynthesis.pdf.
The select-one ritual, before every Chat question and every Studio generation: uncheck all
sources, check only the lesson source, say its name aloud, then press Generate. Forgetting this step
is the single most likely way to produce a wrong pack.
Chat and Studio are scoped differently. Chat is scoped by your prompt and the checkboxes. Studio
— Audio Overview, Video Overview, Mind Map, Flashcards, Quiz, Study Guide — is scoped by the
checkboxes only. Prompt wording alone does not scope Studio: “only Lesson 3” in a prompt will not
stop Studio generating from every selected source.
Never upload a whole textbook as a single source for one lesson, and never add both the whole book
and its chapter PDFs — duplicate passages confuse retrieval and double the citations.
Trimming is hygiene, not a Google rule: trim to the pages taught so retrieval is precise and cheap. It
does not by itself guarantee accuracy. The first edition presented “never a whole subject” as a product
rule; it is not one, and that claim is withdrawn.
Exceptions, and only these: (1) a subject with more than 50 lessons — split the notebook by term at
40 sources, not at the 50 limit; (2) end-of-term revision — select all chapter sources deliberately, and
say that is what you are doing; (3) sharing one lesson only — copy that one chapter source into a
separate share notebook.
Know the ceilings: up to 100 notebooks per account and up to 50 sources per notebook on the free
plan; each source up to 500,000 words or 200 MB for uploaded files. Paid plans raise these, so check
the current limits page before planning a large notebook. Sources: Add or discover new sources and M
anage your Gemini Notebook usage limits.
The master notebook holds method only. Lesson chapters go only in subject notebooks.
Summarize — in layers, then freeze, then Studio
1. Definitions table first — every term, with a citation per row (prompt on the next page).
2. Per section: “Summarize each section in 5 bullets, with a citation for each bullet.”
3. Then synthesis: “Merge those into one 10-bullet study guide. Definitions and steps only. No
examples that are not in the sources.”
4. Freeze it: check the citations, then save the result as a note titled Checked summary — [lesson] —
[date]. A summary is not used until it is frozen.
5. Then Studio, in this fixed order: Study Guide (Studio → Reports) → Mind Map → Audio Overview
→ Video Overview → Flashcards → Quiz. Studio is generated from the frozen checked summary plus
the chapter — never from the raw chapter alone. Video is never first and never generated live:
generate it the day before and watch it in full.
Gemini Notebook Master Notebook Guide 6

6. Split, summarize, prompt — prompts and the check
Prompt — four things, every time
Every prompt carries format + scope + language + what to do when the source has no answer. Put
this header on every prompt:
HEADER FOR EVERY PROMPT
From the selected source(s) only, in formal Arabic, for [grade]:
[the format below]. If the source does not define a term or give
an example, write "Not in the source" — do not invent one.
Cite every row, bullet and answer.
DEFINITIONS TABLE
List every definition in [lesson] as a table:
Term | Definition in the book | Example from the book.
Add a citation for every row. If a term is used but not defined
in the sources, list it separately under "Used but not defined".
QUIZ WITH EVIDENCE
Create a 10-question quiz from these sources only: 5 multiple
choice and 5 short answer. Provide an answer key that quotes
the source passage behind each correct answer.
STUDY GUIDE
Create a one-page study guide for [grade and lesson]: key terms
with short definitions, the sequence of steps or events, and
5 practice questions with answers. Cite the source for each part.
Set the chat style by notebook: master notebook = Custom with the Section 3 prompt; lesson notebook
= Learning Guide, which is built for educational content. Never both in the same notebook. Source: Use c
hat in Gemini Notebook.
Check-3 — the quality check, made checkable
The first edition’s “2-minute check — correct? from the book? clear?” could not actually be done in two
minutes: nobody can listen to a 10-minute audio and verify 10 quiz answers in that time. It is replaced by
Check-3:
1. Open 3 citations at random and read the source passage word for word against the output.
2. Listen to the first 60 seconds of the audio; watch the first 60 seconds of the video.
3. Sign the file: …-v1-YYYY-MM-DD-checked-[checker]. No signature, no publishing.
The maker’s check and the supervisor’s check are two separate checks. Neither replaces the other, and
no pack is published on a feeling.
Gemini Notebook Master Notebook Guide 7

7. Lecture map — which source backs each part of the
slideshow
The Phase 1 lecture runs 19 slides in about 45–60 minutes. When a teacher challenges a claim, this map
is where the trainer points — slide group first, official page second.
Lecture part Claim being taught Backing source (Section 8)
Why and Gemini Notebook is a source-grounded research assistant; S1 rename announcement;
what (slides NotebookLM is its former name; it has Sources, Chat and S2 Learn about Gemini
1–4) Studio panels Notebook
Source rules Supported source types; 500,000 words or 200 MB per source; S4 Add or discover new
(slides 5–6) up to 50 sources per notebook on the free plan sources; S8 usage limits
Select-one One notebook per Grade + Subject; uncheck all, check only the Section 6 of this guide
ritual (slide 7) lesson source before every generation; Studio is scoped by (programme method)
checkboxes only
The pack Audio Overview formats (Deep Dive, The Brief, Critique, S6 Audio Overview; S7 Video
(slides 8–12) Debate); Interactive Mode is English-only; Video Overview Overviews; S2 Learn about
formats incl. Short (free availability unverified); Mind Map,
Flashcards, Quiz, Study Guide
Live demos Biology photosynthesis pack; History timeline and debate S5 Use chat (Configure
(slides 13–15) audio; three reusable prompts Chat, Learning Guide);
Section 6 of this guide
Trust (slide Default chat answers from source data and carries in-line S5 Use chat; S6 and S7 (AI-
16) citations, and can still be wrong — hence Check-3 (Section 6): generated output warnings)
3 citations opened, first 60 seconds of audio and video
checked, file signed
Privacy and Never upload student personal data; content is not used to S9 Privacy and Terms of
filing (slides directly train foundational models unless feedback is given; Use; S12 Microsoft column
17–18) finished packs are filed Draft → Review → Published in guidance
Microsoft 365
First week Day 1 / Day 3 / Day 5 action plan; bring a first pack to the next Programme rule (local
(slide 19) session practice, not a Google
feature)
The two live demos, in brief
Biology — photosynthesis. Work in the Grade 3 — Biology subject notebook. Add the trimmed chapter
as a lesson source, uncheck all, check only that source, and say its name aloud. Configure Chat →
Learning Guide. Run the definitions table, then the layered summary, freeze the checked summary as a
note, then generate the pack in Studio in the fixed order: Study Guide (Reports), Mind Map, Audio
Overview (Deep Dive), Video Overview, Flashcards, Quiz. Finish with Check-3 and sign the file.
History. Work in the History subject notebook, with the same ritual: trimmed chapter as a lesson source,
select only that source. Ask Chat for a timeline with a citation per event. Generate an Audio Overview in
the Debate format so two hosts argue the causes, then a Quiz, following the same Studio order and
Check-3. Close by running the gap prompt live — teachers remember the moment the notebook honestly
says what it does not cover.
Gemini Notebook Master Notebook Guide 8

8. Verified source library — add these to the master
notebook
Every link below is an official Google or Microsoft page. Add S1–S11 as sources in the master notebook;
keep S12 open when you build the Microsoft 365 library. Check the limits page (S8) again before each
new cohort, because Google marks its limits as subject to change.
# Source What it supports
S1 NotebookLM is now Gemini Not The rename (16 July 2026); same standalone product, new name
ebook — Google Workspace Up rolling out across interfaces
dates
S2 Learn about Gemini Notebook What the tool is; grounded chat with in-line citations; 80+ languages;
— Gemini Notebook Help age verification and under-18 policies; Education availability
(conditional — see Section 9)
S3 Create a notebook in Gemini No Creating a notebook; adding and selecting sources in the Sources
tebook — Gemini Notebook Hel panel
p
S4 Add or discover new sources for Source types and limits: up to 500,000 words or 200 MB per source;
your notebook — Gemini Noteb up to 50 sources for free users; web and Workspace source discovery
ook Help
S5 Use chat in Gemini Notebook — Default chat is source-grounded; citations; Configure Chat styles —
Gemini Notebook Help Default, Learning Guide, Custom — and response length
S6 Generate Audio Overview in Ge Audio Overview formats incl. Deep Dive; customization prompt;
mini Notebook — Gemini Noteb background generation; 80+ languages; inaccuracy warning
ook Help
S7 Generate Video Overviews in G Video Overview generation and customization; generation can take
emini Notebook — Gemini Note more than 30 minutes; Cinematic is Ultra-only (paid) and restricted to
book Help ages 18+; Short availability on free accounts is unverified
S8 Manage your Gemini Notebook Compute-based usage limits; allowance refreshes every 5 hours up to
usage limits — Gemini Noteboo a weekly limit; plan multipliers (Plus 2x, Pro 4x, Ultra higher)
k Help
S9 Privacy and Terms of Use in Ge Content not used to directly train foundational models unless feedback
mini Notebook — Gemini Noteb is given; feedback review and 3-year retention; Workspace and
ook Help Education protections
S10 Quickstart Guide to Gemini and Included free of charge in Workspace for Education editions and
Gemini Notebook for Education available to users of all ages where the institution has Workspace for
— Google Workspace Help Education and an admin has enabled it; core-service data protections
S11 Get started with the Gemini Not Mobile app scope and its limitations: fewer source types; no chat
ebook mobile app — Gemini No configuration; cannot generate Mind Maps or Study Guides (Reports)
tebook Help
S12 Create a column in a list or librar SharePoint library columns for grouping, categorizing and tracking —
y — Microsoft Support the six columns in Section 9: Grade, Subject, Unit, Topic, Teacher,
Status
Gemini Notebook Master Notebook Guide 9

9. Limits, privacy, age — and the Microsoft 365 library
Limits a trainer must state plainly
Free plan: up to 100 notebooks per account, 50 sources per notebook, each source up to 500,000
words or 200 MB. Paid plans raise these.
Usage is compute-based: prompt complexity, the models and features used, the number of sources,
and chat length all count. The allowance refreshes every 5 hours until the weekly limit is reached, and
there is no fixed number of Audio or Video Overviews per day. Google publishes no per-feature cost
ranking, so the first edition’s claim that “a Video Overview costs far more than a quiz” is withdrawn:
check the Studio cost bar before generating, and Settings → Usage. Do not stack heavy generations
live in front of a class. Source: Manage your Gemini Notebook usage limits.
On mobile, expect less: the app supports fewer source types, does not support chat configuration, and
cannot generate Mind Maps or Study Guides (Reports). Trainers prepare notebooks and packs on a
computer. Source: Gemini Notebook mobile app help.
Privacy — the rules that protect students
Never upload student personal data. No names, photos, marks with names, or identifiable student
work. Curriculum chapters and teacher-made material only. This is a programme rule, and it is
absolute.
Google states that content in Gemini Notebook will not be used to directly train its foundational AI
models unless you choose to provide feedback. Feedback shares the associated prompts, sources
and outputs for review, retained for up to 3 years, disconnected from the account.
For Workspace and Workspace for Education accounts, uploads, queries and responses are not
reviewed by human reviewers even when feedback is given, and are not used to train AI models.
Prefer managed accounts over personal accounts for school material. Source: Privacy and Terms of U
se in Gemini Notebook.
Age and education access
Verify age in the Google Account before access. Stricter content policies apply under 18, and some
features are 18+ only — Cinematic Video Overviews (also Ultra-only), Deep Research, Slide Decks
and Infographics. None is needed for a Phase 1 pack.
For Workspace for Education users, Gemini Notebook is available to users of all ages, and the Gemini
app and Gemini Notebook are included free of charge in Workspace for Education editions as core
services under the Education terms — but only where the institution actually has Workspace for
Education and an admin has turned access on. This administration runs its library on Microsoft
365, so treat that as a precondition to arrange and verify, not a promise to repeat. Sources: Learn abo
ut Gemini Notebook and Education Quickstart Guide.
Teachers create and check every pack. Students in Phase 1 only consume published packs; they
need no notebook access of their own.
The Microsoft 365 library — where packs live
One SharePoint document library is the single source of truth, with three states: Draft → Review →
Published. Phase 1 roles: the excellent teacher creates and performs the maker’s Check-3, the
supervisor performs a separate Check-3 (Section 6), and only the publisher moves a pack to Published.
Add six columns — Grade, Subject, Unit, Topic, Teacher, Status — because columns are how a library
groups, categorizes and tracks its contents, and what makes a pack findable across schools. Name every
file in Latin script with hyphens only: Grade-Subject-Unit-Topic-Teacher-v1-YYYY-MM-DD-checked-
[checker]. Source: Create a column in a list or library — Microsoft Support.
Gemini Notebook Master Notebook Guide 10

10. Train the trainer — the cascade that keeps this alive
You teach AI technicians; technicians teach teachers; teachers make packs. The cascade only works if
every level teaches from this same master record, so each technician keeps a copy of the master
notebook and this guide.
A technician is ready to teach when they can, live and unaided
☐ Create a Grade + Subject notebook, add a trimmed chapter as a lesson source, name the source
correctly, and perform the select-one ritual without prompting.
☐ Set Configure Chat correctly by notebook: Learning Guide in a lesson notebook, Custom with the
Section 3 prompt in the master notebook.
☐ Run the layered summary, freeze the checked summary as a note, run all three Section 6 prompts,
and perform Check-3 aloud.
☐ Generate a full pack in Studio and state the honest timings, including that video can take more than 30
minutes.
☐ Run the gap prompt and explain a refusal as missing evidence, not failure.
☐ State the privacy rules, the free-plan limits, and the age rules without notes.
☐ File a finished pack in the Microsoft 365 library under the correct Grade, Subject, Unit, Topic, Teacher
and Status, with the versioned, checked filename.
☐ Build a complete pack live while observed, and correct one deliberate error planted by the assessor. A
fluent explanation alone does not pass.
The technician’s 60-minute session, mirroring the lecture
1. Minutes 0–5: play the Short Video Overview from Section 4 if Short was verified in the teaching
account; otherwise open with a short Explainer.
2. Minutes 5–15: what the tool is, the three panels, source-grounding and citations.
3. Minutes 15–35: the Biology demo, end to end, teachers following on their own laptops.
4. Minutes 35–45: the History demo, the gap prompt, and Check-3.
5. Minutes 45–55: hands-on — each teacher starts a pack from one chapter they teach.
6. Minutes 55–60: filing, roles, and the first-week commitment: one pack, checked and filed.
Keeping the record current
Before each new cohort, re-open S2, S4 and S8 and confirm the names, source types and limits still
match what the app shows. Replace stale sources in the master notebook and regenerate the
overviews if a feature has visibly changed.
Record every local decision — a new role, a new column, a new naming rule — as a dated note in the
master notebook, labelled “Programme rule”, so the next trainer can tell Google’s product from your
programme at a glance.
If this guide and the live app disagree, the live app and Google’s current help pages win. Update this
guide; do not teach around the difference.
Prepared for the Phase 1 teacher-training programme of the local education administration. Product names, features and
limits are as documented by Google and Microsoft on the pages listed in Section 8 at the time of writing and are subject to
change by those providers.
Gemini Notebook Master Notebook Guide 11

11. Staged use — never “implement everything”
Do not upload this guide and tell the notebook to “implement what is in it.” Gemini Notebook is not an
agent that runs tasks: it answers from its sources, and audio, video and the other pack parts are separate
Studio generations a person starts. One large instruction produces one generic summary and no checked
pack. Work through the stages in order instead. No stage is passed by a good answer; each stage is
passed only by a named artefact the next stage uses. At every stage: default chat only, a citation for
each point, and the canonical structure from Section 6.
Stage 0 — Setup first (not a chat prompt)
Paste the Section 3 prompt into Configure Chat → Custom in the master notebook and save, before
chatting. Upload the Section 8 pages as separate sources; do not rely on this guide alone. Artefact: a
configured master notebook.
Stage 1 — Test it understands
Select only this guide as a source, then ask: “From the Master Guide only, list the 7 parts of a lesson pack
and the limits. Give a citation for each point. What must never be uploaded?” Pass artefact: 7 cited parts,
limits stated as compute-based with a 5-hour refresh to a weekly cap, and 100 notebooks in total. If it
cannot answer cleanly, stop — do not go to video.
Stage 2 — Research and gaps
Ask: “What does the guide NOT cover about teaching this lecture? List the gaps only.” Verify each listed
gap against the guide; the model can invent gaps. Artefact: a verified gap list.
Stage 3 — Build one pack, one output at a time
In a new subject notebook — never the master — add one real chapter, trimmed and correctly named,
select only that source, and work in the Section 6 order: definitions, per-section summary, synthesis,
freeze the checked summary as a note, then Studio in the fixed order. Never ask for all 7 parts in one
prompt. Artefact: one complete pack that has passed Check-3.
Stage 4 — Video, in Studio, not in chat
Click Studio → Video Overview, choose Explainer, select only the Lecture-Phase1-Slides source, and
paste the Section 4 steering prompt. Generate the day before, watch in full, never live. Artefact: a checked
video file.
Stage 5 — Teach-back for technicians
Ask the notebook to teach the method back step by step, stopping after each step for confirmation. Pass
artefact: the technician then builds a pack live while observed, corrects one deliberate error, and files one
pack with a versioned, checked filename (Section 10).
Gemini Notebook Master Notebook Guide 12

12. Retrospective — what the adversarial review changed
Before this edition, the guide, the cheat sheet, the staged prompts and the lecture were reviewed against
each other and against Google’s and Microsoft’s current pages, and attacked as a busy teacher would
actually use them. Every point below was wrong, overstated or inconsistent in the first edition.
| Point reviewed | What was wrong | What this edition does instead |
| -------------- | -------------- | ------------------------------ |
Split rule “One notebook per unit, never a whole One notebook per Grade + Subject, one
subject” — not a Google rule, and source per lesson, three named exceptions
|     | unworkable: dozens of notebooks a year. | only (Sections 6, 11). |
| --- | --------------------------------------- | ---------------------- |
Studio scoping The guide implied a prompt could scope Chat = prompt + checkboxes; Studio =
Studio. It cannot. checkboxes only. Select-one ritual printed
wherever generation is taught.
Whole book + prompt “Add the whole book and point to the lesson” Whole-book sources for lessons are
gives a fair chat answer and a wrong Studio prohibited; the book and its chapters are
|     | pack. | never both added. |
| --- | ----- | ----------------- |
Video sources Section 4 selected the slides and this guide, Video is generated from the slides source
|     | so the video would narrate the method too. | only. |
| --- | ------------------------------------------ | ----- |
Grounding claim “Chat only uses your sources” stated as Default chat only for packs; agentic and
|     | absolute; agentic features can go beyond | web-search modes are named and |
| --- | ---------------------------------------- | ------------------------------ |
|     | sources.                                 | excluded.                      |
Cinematic / Short Cinematic given as merely 18+; Short Cinematic: Ultra-only, paid, 18+, never
assumed available to open every session. demoed on free accounts. Short: verify in
the teaching account first; Explainer is the
fallback.
Limits and cost 100-notebook limit missing; “video costs far 100 notebooks / 50 sources stated; no per-
more than a quiz” invented. feature cost ranking exists — check the
Studio cost bar and Settings → Usage.
Setup time “Create the master notebook in 15 minutes”, Section 1 is setup steps only, with
|     | while video alone can take 30+ minutes. | generation time stated separately and |
| --- | --------------------------------------- | ------------------------------------- |
honestly.
Quality check A “2-minute check” no one could actually Check-3: 3 citations read word for word, first
perform on a full pack. 60 seconds of audio and video, signed
filename. Maker and supervisor checks are
separate.
Summaries and Studio order Studio generated from the raw chapter; Layered summary frozen as a named note
three documents gave three different Studio first; one fixed Studio order everywhere:
orders; Study Guide placed in Chat in one, Study Guide (Reports), Mind Map, Audio,
|     | Reports in another. | Video, Flashcards, Quiz. |
| --- | ------------------- | ------------------------ |
Chat style Learning Guide and Custom both Master notebook = Custom; lesson
prescribed, with no rule for which notebook notebook = Learning Guide; never both in
|     | gets which. | one notebook. |
| --- | ----------- | ------------- |
Pack count and naming Pack counted as 6 in one place and 7 in 7 parts = 6 outputs + 1 chapter, everywhere.
another; three naming patterns; four library One source name pattern, one versioned
|     | columns in one document, six in another. | checked filename, six library columns. |
| --- | ---------------------------------------- | -------------------------------------- |
Gemini Notebook Master Notebook Guide 13

12. Retrospective — continued
| Point reviewed | What was wrong | What this edition does instead |
| -------------- | -------------- | ------------------------------ |
Lecture map Slides 5–6 counted in two lecture parts at Why and what = slides 1–4; source rules =
|     | once. | slides 5–6; no overlap. Map renumbered for |
| --- | ----- | ------------------------------------------ |
the corrected 19-slide deck (new slide 7, the
select-one ritual).
Mobile and age Mobile limits understated; 18+ features listed Mobile cannot generate Mind Maps or Study
incompletely; Interactive Mode language Guides; Deep Research, Slide Decks and
|     | unstated. | Infographics are also 18+; Interactive Mode |
| --- | --------- | ------------------------------------------- |
is English-only.
Education access “Free, for all ages” repeated as a promise, Stated as a precondition: Workspace for
although this administration runs Microsoft Education in place and admin-enabled,
|     | 365. | verified before anyone relies on it. |
| --- | ---- | ------------------------------------ |
Prompts and gaps Prompts named format and scope but not Every prompt carries the four-part header
language or the missing-answer case; gap including “Not in the source”; gap lists must
|     | answers trusted at face value. | themselves be verified. |
| --- | ------------------------------ | ----------------------- |
Still to verify live, in the account you will teach from: (1) whether Short Video Overview appears
on that account; (2) whether Studio in the current app offers any prompt-based scoping beyond
source selection — until a live test proves otherwise, teach checkboxes-only; (3) that Workspace for
Education access exists and is enabled, if the programme intends to rely on it. Everything else in this
edition was checked against the sources in Section 8 on 17 November 2026.
Gemini Notebook Master Notebook Guide 14
