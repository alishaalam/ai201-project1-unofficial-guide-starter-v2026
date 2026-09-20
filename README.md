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

---
# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

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
