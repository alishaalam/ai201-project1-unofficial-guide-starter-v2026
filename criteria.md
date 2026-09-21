# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
My five test questions aren't uniformly hard. Four of them ("BIOL 160 hours,"
"Aldridge Hall laundry," "shuttle schedule," "allergen-friendly dining hall")
each have their answer sitting in one or two source files. The fifth, "List of
places to eat on campus," needs chunks from seven separate dining documents to
be fully correct — the kind of aggregation question a single retrieval pass is
more likely to miss one of. I expect that one to be the miss, which is why 4
of 5 and not 5 of 5.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
This isn't left to the model's memory — `app.py` appends the retrieved
sources programmatically after generation (`Sources retrieved: ...`), rather
than asking the LLM to cite honestly. Every answer runs through the same
retrieval step before generation exists, so there's no code path that
produces an answer with zero sources attached. That's a property of the
pipeline, not a hope about model behavior, which is why I set this at 5 of 5.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
When I ran the calibration in Milestone 4, my five in-corpus questions landed
between 0.243 and 0.525, and my five out-of-scope questions landed between
0.826 and 0.916 — a clean gap of about 0.30 with nothing from either group
inside it. Any cutoff in that gap (I used 0.6) would have separated all ten
perfectly. I still set the target at 4 of 5 rather than 5 of 5 because that
gap was measured on only five out-of-scope questions — I don't want to claim
a perfect score on a boundary I've only tested from one side of that narrowly.

---

## 4. Something about your chunks

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->

At least 4 of 5 sampled chunks start and end on a sentence boundary — none
begins or ends mid-sentence — and no chunk mixes content from two different
source categories (e.g., part Dining, part Housing).

**Why this target:**
I set chunk size at 800 with 120 overlap specifically because most of my
documents are short enough to fit inside one chunk without truncation —
that's the whole reasoning behind the Chunking Strategy numbers in my README.
So most sampled chunks should read as one complete document. The risk is the
handful of longer documents (multi-section housing and course pages) that
exceed 800 characters and have to split — those are the ones most likely to
cut a sentence or a list, which is why I didn't set this at 5 of 5.

---

## 5. Your choice

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->
     For at least 4 of 5 in-scope questions, every important factual claim in the answer is supported by the retrieved chunks, with no invented details.

**Why this target:**
Criterion 2 checks whether an answer names a source, but naming a source does not prove that the source supports the answer. This criterion tests whether the LLM actually stays within the evidence.
Ex: "What do i learn in Math?"   
  (best distance 0.600, cutoff 0.6)

I do not have enough information in the provided documents to answer what you learn in Math, as the documents only describe the format, assessment, workload, and advice for MATH 220 Linear Algebra without detailing the specific topics or curriculum. 

Sources: `course_math_220.txt`, `course_math_220_exams.txt`, and `course_math_220_workload.txt`

Sources retrieved: course_cs_340.txt, course_hist_118.txt, course_math_220.txt, course_math_220_exams.txt, course_math_220_workload.txt

1 model calls this session, 699 tokens (608 in, 91 out)
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
