"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in unit 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

Two optional keys per question, for "how many / list every X" questions:
`category` scopes retrieval to one metadata category (e.g. "Dining") before
ranking, and `top_k` (set past that category's total chunk count) then
returns all of it instead of just the closest few. Vector top-k ranks by
similarity, not by whether it found every member of a category, so an
exhaustive question loses members the moment a category has more of them
than the default top_k allows. Leave both unset for an ordinary single-fact
question — raising top_k globally instead would just as easily drown one of
those in irrelevant chunks.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in unit 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

QUESTIONS = [
    # {"question": "...", "expects": "..."},
    {"question": "How many hours a week should I expect for BIOL 160?", "expects": "9 to 11 hours"},
    {"question": "How much does laundry cost in Aldridge Hall?", "expects": "$1.75"},
    {"question": "How many resident halls on campus?", "expects": "7", "category": "Housing", "top_k": 25},
    {"question": "Which Dining hall supports people with allergen sensitivities?", "expects": "Pellew Dining Hall"},
    {"question": "List of places to eat on campus?", "expects": "Halden Hall, North Kitchen, Pellew Dining Hall, Ridgeway Cafe, Kestrel Commons, The Atrium, Verrill Street Grill", "category": "Dining", "top_k": 20},
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
