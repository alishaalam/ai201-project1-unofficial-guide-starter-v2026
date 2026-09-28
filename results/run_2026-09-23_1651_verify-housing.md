# Run log — verify-housing

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 7 · relevance cutoff: 0.6
- Runs per question: 1, caching off
- When: 2026-09-23 16:51

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 |
|---|---|
| How many resident halls on campus? | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.826 | refused |
| How do I change the oil in a diesel engine? | 0.916 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.849 | refused |
| How do I write a for loop in Rust? | 0.886 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### How many resident halls on campus? — run 1

- Best distance: 0.4299 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_aldridge_hall_noise.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_calder_annexe_noise.txt, housing_fenwick_court.txt, housing_fenwick_court_laundry.txt, housing_fenwick_court_noise.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_innisfree_hall_noise.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt, housing_old_brewhouse_noise.txt, housing_tamsin_court.txt, housing_tamsin_court_laundry.txt, housing_tamsin_court_noise.txt

```
I don't have enough information to determine the total number of residence halls on campus.
```
