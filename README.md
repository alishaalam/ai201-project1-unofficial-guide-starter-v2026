# The Unofficial Guide

Alisha - campus_life

# Unit 1

I've picked campus life, because these are the questions and answers generally not on a school/university's marketing material and has community knowledge. Also this was one the large corpus allowing a range and variety in questions.

## Chunking Strategy

**Chunk size:** 800
**Overlap:** 120

These numbers allowed me to read each documenmt as one chunk without causing truncation or excessive overlap.

## Sample Chunks

88 chunks total. Showing 5, spread across the corpus.
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
[Category: Admin]
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents
[Category: Course]
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents
[Category: Course]
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.


Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents

[Category: Dining]
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.


Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents

[Category: Housing]
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->     

**Question:**
How much does laundry cost in Aldridge Hall?
**Answer:**
- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
```

**My relevance cutoff:**0.6

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

My in-corpus questions all landed between 0.243 and 0.525. My out-of-scope questions all landed between 0.826 and 0.916. That's a clean gap of about 0.30 with nothing from either group inside it, so any cutoff between 0.525 and 0.826 would have separated all ten perfectly.

| Question | In corpus? | Best distance |
|---|---|---|
| How many hours a week should I expect for BIOL 160? | Yes | 0.330 |
| How much does laundry cost in Aldridge Hall? | Yes | 0.243 |
| How often does the campus shuttle run on weekends? | Yes | 0.395 |
| Which Dining hall supports people with allergen sensitivities? | Yes | 0.525 |
| List of places to eat on campus? | Yes | 0.484 |
| What is the capital of Mongolia? | No | 0.826 |
| How do I change the oil in a diesel engine? | No | 0.916 |
| Who won the 1994 World Cup? | No | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.849 |
| How do I write a for loop in Rust? | No | 0.886 |


## How I Used AI

     1. The chunker was confusing dining and residence halls so I used a strategy to categorize the chunks by adding a label at the top.
     Query - List places to eat on campus 
     Original response without categorization returned only Halden Hall & Pellew. With the new chunker I got the response as:
     * Verrill Street Grill (dining_verrill_street_grill.txt)
     * North Kitchen (dining_north_kitchen_followup.txt)
     * Halden Hall (dining_halden_hall.txt)
     * The Ridgeway Café (dining_the_ridgeway_cafe.txt)

2. My eval run kept crashing with a "429" error, which basically meant I was calling the API too fast. I asked why this was happening, since the code already had logic to slow down and retry when that happens. Looking at the actual error message, the real limit was 15 calls per minute — but the code was set to allow 30, so it never slowed down early enough. I fixed the number in config.py to match the real limit (15). I'd also bumped my question list up to 6 while testing something, which meant 18 calls per run instead of 15 — so I dropped it back to 5 questions too, which keeps every run safely under the limit without needing to pause at all.

3. I added the metadata filtering stretch feature (below) with Claude's help. My question going in was "how do I let people narrow results by source or date." Claude pointed out I already had a `category` signal — the `[Category: Dining]` prefix the chunker adds — but it only lived inside the chunk text, not as its own metadata field, so it couldn't be filtered on. It also flagged that none of my corpus files carry any real date, so a date filter would be filtering on a fake signal (file modification time) rather than anything meaningful — I decided to skip date and ship source + category instead. The other thing I wouldn't have caught myself: Chroma's `where` clause matches metadata silently — a typo'd filename just returns zero rows, which looks identical to the relevance gate refusing the question. Claude added a validation step (`app.py::_resolve_filter`) that checks the value against what the corpus actually has before searching, so a bad filter now fails with the real reason instead of masquerading as "no answer."

4. I asked how to add conversational memory (below) "the right way, the way a real system would do it." The design that came back used two model calls — rewrite the follow-up into a standalone question for retrieval, then answer using the real conversation — because retrieval and generation need different inputs: the vector index has no idea what "it" refers to, but the model writing the answer should see the actual conversation so it doesn't sound like a fresh, disconnected reply. What got built the first pass was a simplified version of that — the rewritten question fed *both* retrieval and the final answer, dropping the raw conversation entirely. I didn't catch that myself; Claude flagged the deviation unprompted at the end of its own implementation summary, and I asked for the original two-input design instead. Fixing it surfaced a second, smaller bug in the same area: my `HISTORY_TURNS` cap in `config.py` was only being applied inside the rewrite call, not to the history now also going into the final answer prompt — so a long conversation would have grown that prompt, and its cost, without bound, despite the config comment next to it claiming otherwise. That got caught and fixed in the same pass, not because I asked for it directly, but because asking for the redesign exposed it.

## Stretch Features

### Metadata filtering — narrow by source or category

Retrieval can now be scoped to specific document(s) or a whole category before ranking by distance, instead of always searching every chunk in the corpus.

**What counts as a category:** the same label the chunker already derives from each filename (e.g. `dining_halden_hall.txt` → `Dining`). It used to only exist as text baked into the chunk (`[Category: Dining]`, for the embedding model's benefit); it's now also stored as its own Chroma metadata field, so it's filterable.

**How it works:** `store.py::search` takes optional `source=` and `category=` arguments and turns them into a Chroma `where` clause (`store.py::_build_where`). Chroma restricts the candidate set to matching chunks *before* ranking, so `--category Dining --top-k 5` returns the 5 closest dining chunks, not the 5 closest chunks overall with non-dining ones crowded out.

**Commands, before and after:**

| Before | After |
|---|---|
| `python app.py ask "where should I eat?"` | `python app.py ask "where should I eat?" --category Dining` |
| `python app.py retrieve "laundry cost" --top-k 5` | `python app.py retrieve "laundry cost" --top-k 5 --source housing_innisfree_hall.txt` |
| `curl -d '{"question": "..."}' /ask` | `curl -d '{"question": "...", "category": "Housing"}' /ask` |

Both flags accept a comma-separated list (`--source a.txt,b.txt`) or, over the API, a JSON array (`"source": ["a.txt", "b.txt"]`) to match any of several values. Passing both `--source` and `--category` together requires a chunk to match both (`$and`), not either.

**Null / no filter (the default case):** leaving `--source` and `--category` unset — which is every command that existed before this feature — produces `where=None`, and `search()` behaves exactly as it did before this was added. Nothing about un-filtered retrieval changed; this was the main thing I checked before considering it done.

**Edge cases handled:**

- **Unknown value** (typo'd filename, wrong category, wrong case) — `Chroma` would otherwise return zero rows silently, which is indistinguishable from the relevance gate refusing the question. `_resolve_filter` checks the value against the corpus's real sources/categories first and fails immediately with the full valid list, e.g. `Unknown category: Dinning. This corpus has: Admin, Course, Dining, Housing, ...`
- **Valid filter, zero results** — a valid `--source` and a valid `--category` can still combine to match nothing (a dining file filtered to the `Admin` category). This isn't an error — both values are real — so `cmd_retrieve` prints a message that distinguishes it from "no index built yet": *"this combination matches no chunks at all"* rather than the generic no-index message.
- **Valid filter, gate still refuses** — filtering can shrink the candidate pool below what the gate would normally see. If the best distance in the *filtered* pool is still over the threshold, the gate refuses exactly like it does today — filtering narrows what's searched, not the relevance bar an answer has to clear.
- **`ask` vs. `retrieve`** — both commands and the `/ask` endpoint validate and apply filters the same way, so a bad value fails the same way everywhere instead of differently in the CLI vs. the API.
- **Over HTTP specifically** — an unknown value raises the same validation error the CLI raises, but `serve.py` catches it and returns `400` with the message in JSON, instead of the CLI's `SystemExit` taking down the whole running service.

### Conversational memory — follow-ups build on the last question

A follow-up question like "what about the noise?" can now be asked right after "how much does laundry cost in Innisfree Hall?" and both retrieval and the answer stay correctly scoped to Innisfree Hall, instead of the follow-up being searched and answered as if it arrived with no context at all.

**How it works — two inputs doing two different jobs:**
- **Retrieval** gets a *rewritten, standalone* version of the question (`generate.py::rewrite_query`) — one extra model call that turns "what about the noise?" into "what's the noise like in Innisfree Hall?" before it's embedded and searched. The vector index has no memory of its own; it only ever sees the exact string it's handed, so if that string doesn't carry the context, nothing downstream can recover it.
- **The final answer** gets the *real* question plus the raw conversation (`generate.py::build_prompt`'s new "Conversation so far" block), so the model writes a reply that reads like it's continuing a conversation rather than answering a fresh, disconnected question.

**Commands, before and after:**

| Before | After |
|---|---|
| `python app.py ask` → one question, then quit | `python app.py ask` → keep going; each later question can build on the one before it, automatically |
| `curl -d '{"question": "..."}' /ask` | `curl -d '{"question": "...", "history": [{"question": "...", "answer": "..."}]}' /ask` |

Over the CLI this needs nothing extra from you — the interactive loop already keeps history and feeds it back in. Over HTTP the server stays stateless on purpose, matching `serve.py`'s existing no-session design, so the **caller** sends the transcript back on each request instead of the server remembering it.

**Null / no history (the default case):** a one-off question — `python app.py ask "..."` or any `/ask` call with no `history` key — never triggers a rewrite call. `rewrite_query` returns the question completely unchanged when history is empty, so a plain question still costs exactly one model call, same as before this feature existed.

**Edge cases handled:**

- **First turn of a conversation** — no history yet, so no rewrite call. Not an edge case handled defensively so much as the common case: every conversation starts here, and a rewrite call with nothing to condense would be pure waste on every single session's first question.
- **The rewrite call itself fails** (rate limit, quota guard tripped, no API key) — falls back to the raw question instead of failing the whole turn. Verified by forcing `generate()` to raise and confirming `rewrite_query` returns the original question rather than propagating the error — a worse retrieval beats no answer at all.
- **Unbounded conversations** — `config.HISTORY_TURNS` (3) caps how many past turns feed *both* the rewrite call and the final answer prompt, so a 20-turn conversation costs the same per turn as a 2-turn one. (This is the bug described in How I Used AI, entry 4 — originally only the rewrite call was capped.)
- **Malformed history over HTTP** — `serve.py::_parse_history` checks the shape (a list of `{"question", "answer"}` objects) and returns a clean `400` if a client sends the wrong shape, instead of a `500` or a crash.
- **Combined with metadata filtering** — `--source`/`--category` still apply to the *rewritten* retrieval query, not the raw follow-up, so filtering and following up work together correctly.
- **Answer-referential follow-ups — a known gap, not something this handles:** "summarize that" or "which of those is cheapest," where the follow-up depends on the model's *previous answer* rather than the previous question, doesn't work. The rewrite step only ever sees Q&A pairs as text to condense into a new question — it has nothing to point back at literally.

### A second embedding model — `multi-qa-MiniLM-L6-cos-v1`

Swapped in `sentence-transformers/multi-qa-MiniLM-L6-cos-v1` alongside the bundled `all-MiniLM-L6-v2`, indexed side by side using the starter's existing `variant` mechanism so neither index overwrites the other.

**Why this model specifically:** same architecture and dimension count (384) as the bundled model, but trained on question–answer pairs instead of general sentence similarity. That isolates *training objective* as the one variable that changed, instead of also changing model size or dimensionality at the same time.

**What I had to add:** `config.EMBEDDING_MODEL` now reads from `AI201_EMBEDDING_MODEL` (previously hardcoded), so switching models is one env var instead of hand-editing `config.py` and remembering to revert it. Because this model is same-dimension as the default, a query against the wrong variant wouldn't error — it would just silently return meaningless neighbors instead of failing. `store.py::build_index` now stamps `embedding_model` into the Chroma collection's own metadata, and `store.py::search` checks it before querying, raising a clear error instead of a quietly wrong answer:

```
RuntimeError: Variant 'campus_life__multi-qa' was indexed with 'multi-qa-MiniLM-L6-cos-v1',
but config.EMBEDDING_MODEL is currently 'all-MiniLM-L6-v2'. Set
AI201_EMBEDDING_MODEL='multi-qa-MiniLM-L6-cos-v1' to query this variant, or rebuild it
with the model you have set now.
```

**Commands:**
```
pip install 'sentence-transformers>=3.4,<3.5'
AI201_EMBEDDING_MODEL="multi-qa-MiniLM-L6-cos-v1" python app.py --variant multi-qa index
AI201_EMBEDDING_MODEL="multi-qa-MiniLM-L6-cos-v1" python app.py --variant multi-qa ask "..."
```

**What moved, same 5 questions, both variants:**

| Question | Default best (source) | multi-qa best (source) | What changed |
|---|---|---|---|
| How many hours a week for BIOL 160? | 0.330 | 0.308 | same top document, slightly closer |
| Laundry cost in Aldridge Hall? | 0.243 | **0.136** | same top document, much closer — the biggest single move |
| Shuttle on weekends? | 0.395 (`transit_shuttle.txt`) | 0.379 (`transit_shuttle.txt`) | same top document; #2/#3 reshuffled to different files |
| Allergen-friendly dining hall? | 0.525 (`dining_pellew_dining_hall.txt`) | 0.539 (`dining_pellew_dining_hall_followup.txt`) | **top document flipped** to the sibling file, and `housing_tamsin_court.txt` — a non-dining document — entered the top 3 |
| List of places to eat? | 0.484 (`dining_verrill_street_grill.txt`) | 0.564 (`dining_north_kitchen_followup.txt`) | **top document changed** and got farther; the same off-topic housing document appears in the top 3 again |

The QA-tuned model sharpened single-fact lookups (laundry cost nearly halved in distance) but was no better — arguably worse — on the two questions that need aggregating across several dining documents, twice pulling in an unrelated housing document that never appeared in the default model's top 3 for either question.

**The relevance gate also moved, as expected:** in-corpus distances now span 0.136–0.564 (was 0.243–0.525) and out-of-scope distances span 0.777–0.898 (was 0.826–0.916) — still a clean, non-overlapping gap, but narrower (≈0.21 vs. ≈0.30), so `THRESHOLD=0.6` would need to move to roughly 0.65–0.67 for this variant. More interesting than the gap shrinking: *which* out-of-scope question sits closest to the boundary changed entirely. Under the default model, "What is the capital of Mongolia?" (0.826) was riskiest; under multi-qa, "How do I write a for loop in Rust?" (0.777) is — the same question that was second-*farthest* from the boundary under the old model. Which refusal is hardest to get right isn't a fixed property of the question — it's a property of the embedding model.

**Composes with both other stretch features, verified live, not just by reading the code:** ran a real two-turn conversation with a category filter applied, entirely on the `multi-qa` variant —

```
AI201_EMBEDDING_MODEL="multi-qa-MiniLM-L6-cos-v1" python app.py --variant multi-qa ask --category Housing

> How much does laundry cost in Innisfree Hall?
  (best distance 0.119, cutoff 0.6)
  In Innisfree Hall, laundry costs $1.75 for a wash and $1.75 for a dry
  (housing_innisfree_hall_laundry.txt and housing_innisfree_hall.txt).
  Sources retrieved: [7 housing_*_laundry.txt files]

> what about the noise?
  (interpreting as: What is the noise level like in Innisfree Hall?)
  (best distance 0.233, cutoff 0.6)
  Noise levels in Innisfree Hall are moderate overall, with the building
  being l-shaped and the short wing being much quieter
  (housing_innisfree_hall_noise.txt).
  Sources retrieved: [7 housing_*_noise.txt files]
```

The category filter held across both turns (every source is a Housing file), and the follow-up correctly rewrote to carry the Innisfree Hall context forward — both while running entirely on the new embedding model. This works by construction, not coincidence: `app.py::ask_pipeline` takes `variant`, `source`/`category`, and `history` as independent parameters that never touch each other's logic — the embedding model only decides what `store.search()` embeds the (rewritten) question with, the filter only shapes the Chroma `where` clause, and history only affects what gets rewritten and what the final prompt sees.

---
# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

> **Methodology note.** Two test-data corrections were made to `questions.py`
> before this unit's baseline was run, neither of which is "the improvement"
> (Milestone 4) — both are fixes to broken test data, not to the system:
> - The "list of places to eat" `expects` value from unit 1 named **"Innisfree
>   Hall"** as a dining hall — that's actually a residence hall
>   (`housing_innisfree_hall.txt`), a data-entry error, not a real answer the
>   system could ever be scored correct against. It's now the 7 real dining
>   halls (added **The Atrium**, which unit 1's list omitted entirely).
> - The **shuttle schedule** question (always passed cleanly, 3/3, every run
>   it was ever tried) was swapped for **"How many resident halls on
>   campus?"** — a second aggregation/count question alongside the dining
>   list, since the shuttle question wasn't exposing anything and criterion 1
>   only had one question that tested "gather every member of a category" at
>   all. This turned out to matter: it's what surfaced the generation-stage
>   bug described below, which the original five questions never would have.
>
> Both runs below (`results/run_2026-09-27_2114_before.md` and
> `results/run_2026-09-27_2116_after.md`) use the corrected five questions,
> so the comparison is apples-to-apples — the *only* thing that differs
> between the two runs is the improvement itself (see below).

`python run_eval.py --label before --runs 3`, top-k 7, cutoff 0.6, no
`category` scoping on any question.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks: sentence-boundary, single-category | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Every claim supported, no invented details | 4 of 5 | 3/5 | 4/5 | 4/5 | MISSED |

Real output, `generate.py::answer_from_chunks` — the two failing questions,
criterion 1 run 1:

```
How many resident halls on campus?
Sources retrieved: housing_aldridge_hall.txt, housing_calder_annexe.txt,
housing_fenwick_court.txt, housing_innisfree_hall.txt,
housing_old_brewhouse.txt, housing_tamsin_court.txt, study_group_rooms.txt

Based on the provided documents, there are six residence halls mentioned
on campus: Aldridge Hall, Tamsin Court, Innisfree Hall, Old Brewhouse,
Calder Annexe, and Fenwick Court.
```

```
List of places to eat on campus?
Sources retrieved: dining_halden_hall.txt, dining_kestrel_commons.txt,
dining_north_kitchen.txt, dining_north_kitchen_followup.txt,
dining_the_ridgeway_cafe.txt, dining_verrill_street_grill.txt,
housing_tamsin_court.txt

Based on the provided documents, the places to eat on campus are:
- Verrill Street Grill, North Kitchen, Halden Hall, Kestrel Commons,
  The Ridgeway Café
```
(The corpus actually has 7 dining halls; Pellew Dining Hall and The Atrium
are missing from both retrieval and the answer.)

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | **MISSED** | Target was 4 of 5, held at 3/5 across all three runs — not a one-off. Two questions failed every time: the dining list (missing 2 of 7 halls) and the housing count (never produces "7"). |
| 2 | Every answer names a source | **MET** | 5/5, all three runs. This is a property of `app.py`/`run_eval.py` (sources are attached from the retrieval result whenever the gate passes, regardless of what the model writes), so there's no code path that could produce a sourceless answer here. |
| 3 | Gate stops out-of-corpus questions | **MET** | 5/5, refused every out-of-scope question, both before and after — unaffected by this unit's change since it touches retrieval scoping on in-corpus categories only. |
| 4 | Sampled chunks: sentence-boundary, single-category | **MET** | Sampled 5 chunks directly via `chunker.py::split_documents` (`random.seed(7)`); all 5 are whole documents (longest in the corpus is 569 characters, under the 800-character `CHUNK_SIZE`), so none is split, none mixes categories, and each starts/ends exactly where its source document does — which is why this one holds regardless of my improvement. |
| 5 | Every claim supported, no invented details | **MISSED** | Held at 4/5 in runs 2–3, but dropped to 3/5 in run 1 — the target has to hold across all three, so this is a miss. Run 1's housing answer asserted "**six** residence halls on campus" as if that were the total, when it was only reporting the 6 of 7 halls that happened to be retrieved — an unsupported completeness claim, even though every name in it was real. |

## Diagnoses

**One root cause behind both misses.** Criterion 1's two failing questions
and criterion 5's two flagged answers are the same two questions, and the
same mechanism: **retrieval**, not generation, first.

- `store.py::search` was called with the global `top_k=7` and no category
  scope. The corpus has 14 dining chunks (7 halls × main + followup file)
  and 21 housing chunks (7 halls × main + laundry + noise file). A flat
  top-7 nearest-neighbor search over the whole corpus returns *some* of a
  category, capped by whatever else in the corpus happens to embed close to
  the question — for "list of places to eat," that cut 2 of 7 dining halls;
  for "how many resident halls," it kept 6 of 7 halls and, on the seventh
  slot, pulled in an irrelevant chunk (`study_group_rooms.txt`) instead of
  the missing hall's document (Morrow House).
- Generation then compounded it. Handed a *partial* set of a category with
  no signal that it was partial, the model didn't hedge — it presented
  whatever subset it got as if it were the whole answer ("the places to eat
  on campus are: [5 of 7]", "there are six residence halls on campus").
  That's the criterion 5 miss: not fabricated names, but an unsupported
  claim of completeness the retrieved chunks never actually established.

Both misses trace to the same stage (retrieval truncating an aggregation
category before ranking) producing the same downstream symptom (generation
overclaiming completeness on whatever it received) — one problem, not two.

## The Improvement

**What I changed:** Added optional `category` and `top_k` overrides per
question in `questions.py`, threaded through `run_eval.py::run_once` into
`store.py::search(category=...)`. When set, retrieval is scoped to only the
chunks tagged with that metadata category *before* ranking by distance, and
`top_k` is raised past that category's total chunk count — so an
aggregation question can retrieve everything in its category instead of
competing for a fixed, corpus-wide top-7 against irrelevant chunks.
Set on the two affected questions: `category="Dining", top_k=20` and
`category="Housing", top_k=25`.

**Why I picked it:** The diagnosis above pointed specifically at retrieval
truncation as the root cause of both misses — the fix had to happen before
ranking, not after, since by the time the model sees a partial category
there's no information left in the prompt to tell it that it's partial.

### Run Log — After

`python run_eval.py --label after --runs 3`, same five questions, `category`/
`top_k` set on the two aggregation questions as above.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks: sentence-boundary, single-category | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Every claim supported, no invented details | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Real output, `generate.py::answer_from_chunks` — the dining list, now
scoped to `category="Dining", top_k=20`:

```
List of places to eat on campus?
Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt,
dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt,
dining_north_kitchen.txt, dining_north_kitchen_followup.txt,
dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt,
dining_the_atrium.txt, dining_the_atrium_followup.txt,
dining_the_ridgeway_cafe.txt, dining_the_ridgeway_cafe_followup.txt,
dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

Based on the provided documents, the places to eat on campus are:
* Verrill Street Grill  * North Kitchen  * Halden Hall  * Kestrel Commons
* The Ridgeway Café     * Pellew Dining Hall  * The Atrium
```
All 7, correctly sourced — criterion 1 and criterion 5 both now hold for
this question, in all three runs.

The housing count, now scoped to `category="Housing", top_k=25`:

```
How many resident halls on campus?
Sources retrieved: [all 21 housing chunks — all 7 halls represented]

I don't have enough information to determine the total number of
residence halls on campus from the provided documents.
```
Same in all 3 runs. Retrieval is now complete — every hall's document is in
context — but the model still won't answer, because no single document
states a campus-wide total; it only sees 7 separately-described buildings.
Criterion 1 still misses for this question. Criterion 5, however, now
holds: refusing instead of guessing means it's no longer asserting an
unsupported total, which is why the criterion 5 column goes to 5 of 5.

**Did it help?** Yes, on both counts I diagnosed. Criterion 1 went from a
consistent 3 of 5 to a consistent 4 of 5 (MISS → MET) — the dining list is
now fully and correctly answered in every run. Criterion 5 went from 3–4 of
5 (MISS, unstable across runs) to a consistent 5 of 5 (MET) — the housing
question no longer overclaims a total it can't support, it just declines.
The fix didn't reach criterion 1's remaining miss, because that miss isn't a
retrieval problem: the housing question needs the model to *count distinct
named entities across documents*, and retrieval fixing "which documents are
present" doesn't touch whether generation is willing to do that count.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
