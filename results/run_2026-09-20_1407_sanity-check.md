# Run log — sanity-check

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 7 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-20 14:07

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| How many hours a week should I expect for BIOL 160? |   |   |   |
| How much does laundry cost in Aldridge Hall? |   |   |   |
| How often does the campus shuttle run on weekends? |   |   |   |
| Which Dining hall supports people with allergen sensitivities? |   |   |   |
| List of places to eat on campus? |   |   |   |

> The Run columns are blank because `scorer.py` doesn't exist yet.
> Judge each question yourself by reading the output below, or build
> the scorer first and re-run.

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

### How many hours a week should I expect for BIOL 160? — run 1

- Best distance: 0.3304 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

```
You should expect 9 to 11 hours a week for BIOL 160 Cell Biology. 

Source: `course_biol_160.txt` (also mentioned in `course_biol_160_workload.txt`).
```

### How many hours a week should I expect for BIOL 160? — run 2

- Best distance: 0.3304 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

```
You should expect 9 to 11 hours a week for BIOL 160. 

Source: `course_biol_160.txt` (also mentioned in `course_biol_160_workload.txt`).
```

### How many hours a week should I expect for BIOL 160? — run 3

- Best distance: 0.3304 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

```
You should expect 9 to 11 hours a week for BIOL 160. 

Source: course_biol_160.txt (and course_biol_160_workload.txt)
```

### How much does laundry cost in Aldridge Hall? — run 1

- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
In Aldridge Hall, laundry costs $1.75 to wash and $1.50 to dry. 

Source: housing_aldridge_hall.txt and housing_aldridge_hall_laundry.txt
```

### How much does laundry cost in Aldridge Hall? — run 2

- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
Laundry in Aldridge Hall costs $1.75 for a wash and $1.50 for a dry. 

This information comes from *housing_aldridge_hall.txt* and *housing_aldridge_hall_laundry.txt*.
```

### How much does laundry cost in Aldridge Hall? — run 3

- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
In Aldridge Hall, laundry costs $1.75 to wash and $1.50 to dry (housing_aldridge_hall.txt and housing_aldridge_hall_laundry.txt).
```

### How often does the campus shuttle run on weekends? — run 1

- Best distance: 0.3952 (passed the gate)
- Sources retrieved: course_cs_210_workload.txt, course_stat_150_workload.txt, dining_kestrel_commons.txt, dining_verrill_street_grill.txt, money_jobs.txt, transit_shuttle.txt, transit_walking.txt

```
The campus shuttle runs every 40 minutes on weekends. (Source: transit_shuttle.txt)
```

### How often does the campus shuttle run on weekends? — run 2

- Best distance: 0.3952 (passed the gate)
- Sources retrieved: course_cs_210_workload.txt, course_stat_150_workload.txt, dining_kestrel_commons.txt, dining_verrill_street_grill.txt, money_jobs.txt, transit_shuttle.txt, transit_walking.txt

```
The campus shuttle runs every 40 minutes on weekends. 

Source: transit_shuttle.txt
```

### How often does the campus shuttle run on weekends? — run 3

- Best distance: 0.3952 (passed the gate)
- Sources retrieved: course_cs_210_workload.txt, course_stat_150_workload.txt, dining_kestrel_commons.txt, dining_verrill_street_grill.txt, money_jobs.txt, transit_shuttle.txt, transit_walking.txt

```
The campus shuttle runs every 40 minutes on weekends. 

Source: transit_shuttle.txt
```

### Which Dining hall supports people with allergen sensitivities? — run 1

- Best distance: 0.5249 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt

```
Pellew Dining Hall has a dedicated allergen-free station staffed by someone who knows the menu (from dining_pellew_dining_hall.txt).
```

### Which Dining hall supports people with allergen sensitivities? — run 2

- Best distance: 0.5249 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt

```
Pellew Dining Hall has a dedicated allergen-free station staffed by someone who knows the menu (dining_pellew_dining_hall.txt).
```

### Which Dining hall supports people with allergen sensitivities? — run 3

- Best distance: 0.5249 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt

```
Pellew Dining Hall has a dedicated allergen-free station staffed by someone who knows the menu (dining_pellew_dining_hall.txt).
```

### List of places to eat on campus? — run 1

- Best distance: 0.4836 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_kestrel_commons.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe.txt, dining_verrill_street_grill.txt, housing_tamsin_court.txt

```
Based on the provided documents, the places to eat on campus are:

* Verrill Street Grill (dining_verrill_street_grill.txt)
* North Kitchen (dining_north_kitchen.txt and dining_north_kitchen_followup.txt)
* Halden Hall (dining_halden_hall.txt)
* Kestrel Commons (dining_kestrel_commons.txt)
* The Ridgeway Café (dining_the_ridgeway_cafe.txt)
```

### List of places to eat on campus? — run 2

- Best distance: 0.4836 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_kestrel_commons.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe.txt, dining_verrill_street_grill.txt, housing_tamsin_court.txt

```
Based on the provided documents, the places to eat on campus are:

- Verrill Street Grill (from `dining_verrill_street_grill.txt`)
- North Kitchen (from `dining_north_kitchen.txt` and `dining_north_kitchen_followup.txt`)
- Halden Hall (from `dining_halden_hall.txt`)
- Kestrel Commons (from `dining_kestrel_commons.txt`)
- The Ridgeway Café (from `dining_the_ridgeway_cafe.txt`)
```

### List of places to eat on campus? — run 3

- Best distance: 0.4836 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_kestrel_commons.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe.txt, dining_verrill_street_grill.txt, housing_tamsin_court.txt

```
Based on the provided documents, the places to eat on campus are:

- Verrill Street Grill (*dining_verrill_street_grill.txt*)
- North Kitchen (*dining_north_kitchen.txt* and *dining_north_kitchen_followup.txt*)
- Halden Hall (*dining_halden_hall.txt*)
- Kestrel Commons (*dining_kestrel_commons.txt*)
- The Ridgeway Café (*dining_the_ridgeway_cafe.txt*)
```
