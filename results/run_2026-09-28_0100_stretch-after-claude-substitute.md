# Run log — stretch-after (Claude substitute)

> **Substitute measurement.** Gemini (gemini-3.5-flash-lite) was down
> with a sustained 503 ("high demand") for the entire session, and the
> account's free-tier daily quota (20 req/day/model) was exhausted on
> every alternate Gemini model tried. This run uses the real pipeline
> unchanged (`store.py::search`, `gate.py::check`,
> `generate.py::build_prompt`) but substitutes Claude (`claude-sonnet-5`)
> for the final generation call, via a scratch-only script not committed
> to the repo. `generate.py::GROUNDING_INSTRUCTION` — the one real,
> committed change for this stretch feature — is exactly as it is in
> the repo at this point in the run log (unmodified for "before",
> tightened for "after").

- Produced by: scratch `claude_substitute_eval.py::run_suite` (not committed)
- Model: `claude-sonnet-5` (substitute for `gemini-3.5-flash-lite`)
- Corpus: campus_life (index variant default) · top-k 7 (25/20 on the two aggregation questions) · relevance cutoff 0.6
- Runs per question: 3, caching off
- When: 2026-09-28 10:19

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| How many hours a week should I expect for BIOL 160? | pass | pass | pass |
| How much does laundry cost in Aldridge Hall? | pass | pass | pass |
| How many resident halls on campus? | pass | pass | pass |
| Which Dining hall supports people with allergen sensitivities? | pass | pass | pass |
| List of places to eat on campus? | pass | pass | pass |

---

## Real output

### How many hours a week should I expect for BIOL 160? — run 1

- Best distance: 0.3304 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

```
According to course_biol_160_workload.txt (also echoed in course_biol_160.txt), you should expect **9 to 11 hours a week** for BIOL 160 Cell Biology — noted as the heaviest first-year course by reputation, with the first month being even heavier.
```

### How many hours a week should I expect for BIOL 160? — run 2

- Best distance: 0.3304 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

```
According to course_biol_160_workload.txt (and confirmed in course_biol_160.txt), you should expect 9 to 11 hours a week for BIOL 160 — it's cited as the heaviest first-year course by reputation, with the first month being even heavier.
```

### How many hours a week should I expect for BIOL 160? — run 3

- Best distance: 0.3304 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_econ_101_workload.txt, course_engl_205_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

```
According to course_biol_160_workload.txt (and confirmed in course_biol_160.txt), you should expect 9 to 11 hours a week for BIOL 160, with the first month being heavier than the rest.
```

### How much does laundry cost in Aldridge Hall? — run 1

- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
According to housing_aldridge_hall_laundry.txt (and confirmed in housing_aldridge_hall.txt), laundry in Aldridge Hall costs $1.75 for a wash and $1.50 for a dry, using a card-only system.
```

### How much does laundry cost in Aldridge Hall? — run 2

- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
According to housing_aldridge_hall_laundry.txt (also confirmed in housing_aldridge_hall.txt), laundry costs $1.75 for a wash and $1.50 for a dry, and the machines are card only.
```

### How much does laundry cost in Aldridge Hall? — run 3

- Best distance: 0.2433 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse_laundry.txt

```
According to housing_aldridge_hall_laundry.txt (and confirmed in housing_aldridge_hall.txt), laundry costs $1.75 for a wash and $1.50 for a dry, and the machines are card only.
```

### How many resident halls on campus? — run 1

- Best distance: 0.4299 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_aldridge_hall_noise.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_calder_annexe_noise.txt, housing_fenwick_court.txt, housing_fenwick_court_laundry.txt, housing_fenwick_court_noise.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_innisfree_hall_noise.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt, housing_old_brewhouse_noise.txt, housing_tamsin_court.txt, housing_tamsin_court_laundry.txt, housing_tamsin_court_noise.txt

```
Based on the documents, there are 7 residence halls: Aldridge Hall, Tamsin Court, Innisfree Hall, Old Brewhouse, Calder Annexe, Fenwick Court, and Morrow House (from housing_aldridge_hall.txt, housing_tamsin_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_calder_annexe.txt, housing_fenwick_court.txt, and housing_morrow_house.txt).
```

### How many resident halls on campus? — run 2

- Best distance: 0.4299 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_aldridge_hall_noise.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_calder_annexe_noise.txt, housing_fenwick_court.txt, housing_fenwick_court_laundry.txt, housing_fenwick_court_noise.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_innisfree_hall_noise.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt, housing_old_brewhouse_noise.txt, housing_tamsin_court.txt, housing_tamsin_court_laundry.txt, housing_tamsin_court_noise.txt

```
Based on the documents, there are 7 residence halls: Aldridge Hall, Tamsin Court, Innisfree Hall, Old Brewhouse, Calder Annexe, Fenwick Court, and Morrow House (each described in their respective housing_*.txt files, e.g. housing_aldridge_hall.txt, housing_tamsin_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_calder_annexe.txt, housing_fenwick_court.txt, housing_morrow_house.txt).
```

### How many resident halls on campus? — run 3

- Best distance: 0.4299 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_aldridge_hall_noise.txt, housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_calder_annexe_noise.txt, housing_fenwick_court.txt, housing_fenwick_court_laundry.txt, housing_fenwick_court_noise.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_innisfree_hall_noise.txt, housing_morrow_house.txt, housing_morrow_house_laundry.txt, housing_morrow_house_noise.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt, housing_old_brewhouse_noise.txt, housing_tamsin_court.txt, housing_tamsin_court_laundry.txt, housing_tamsin_court_noise.txt

```
Based on the documents, there are 7 residence halls: Aldridge Hall, Tamsin Court, Innisfree Hall, Old Brewhouse, Calder Annexe, Fenwick Court, and Morrow House (from housing_aldridge_hall.txt, housing_tamsin_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_calder_annexe.txt, housing_fenwick_court.txt, and housing_morrow_house.txt).
```

### Which Dining hall supports people with allergen sensitivities? — run 1

- Best distance: 0.5249 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt

```
Pellew Dining Hall has a dedicated allergen-free station staffed by someone who knows the menu (dining_pellew_dining_hall.txt).
```

### Which Dining hall supports people with allergen sensitivities? — run 2

- Best distance: 0.5249 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt

```
Pellew Dining Hall has a dedicated allergen-free station staffed by someone who knows the menu (source: dining_pellew_dining_hall.txt).
```

### Which Dining hall supports people with allergen sensitivities? — run 3

- Best distance: 0.5249 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt

```
Pellew Dining Hall has a dedicated allergen-free station staffed by someone who knows the menu (dining_pellew_dining_hall.txt).
```

### List of places to eat on campus? — run 1

- Best distance: 0.4836 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
Based on the dining documents, there are 7 places to eat on campus:

1. **Verrill Street Grill** (dining_verrill_street_grill.txt) – known for its late-night burger
2. **North Kitchen** (dining_north_kitchen.txt) – rotating regional menu
3. **Halden Hall** (dining_halden_hall.txt) – soup rotation, bread baked on site
4. **Kestrel Commons** (dining_kestrel_commons.txt) – stir-fry station
5. **The Ridgeway Café** (dining_the_ridgeway_cafe.txt) – real espresso
6. **The Atrium** (dining_the_atrium.txt) – grab-and-go sandwiches
7. **Pellew Dining Hall** (dining_pellew_dining_hall.txt) – allergen-free station
```

### List of places to eat on campus? — run 2

- Best distance: 0.4836 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
Based on the documents, there are 7 places to eat on campus: Verrill Street Grill, North Kitchen, Halden Hall, Kestrel Commons, The Ridgeway Café, The Atrium, and Pellew Dining Hall (sourced from dining_verrill_street_grill.txt, dining_north_kitchen.txt, dining_halden_hall.txt, dining_kestrel_commons.txt, dining_the_ridgeway_cafe.txt, dining_the_atrium.txt, and dining_pellew_dining_hall.txt).
```

### List of places to eat on campus? — run 3

- Best distance: 0.4836 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
Based on the documents, there are 7 dining places on campus:

1. **Verrill Street Grill** (dining_verrill_street_grill.txt)
2. **North Kitchen** (dining_north_kitchen.txt)
3. **Halden Hall** (dining_halden_hall.txt)
4. **Kestrel Commons** (dining_kestrel_commons.txt)
5. **The Ridgeway Café** (dining_the_ridgeway_cafe.txt)
6. **The Atrium** (dining_the_atrium.txt)
7. **Pellew Dining Hall** (dining_pellew_dining_hall.txt)
```
