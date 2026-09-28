import re

from rapidfuzz import fuzz

THRESHOLD = 85


def _normalize(text: str) -> str:
    text = text.lower().strip()
    text = text.replace("$", "")
    # "9 to 11" and "9-11" should compare equal, not just close.
    text = re.sub(r"(\d+)\s*(?:to|-)\s*(\d+)", r"\1-\2", text)
    return text


def _item_matches(expected_item: str, answer_norm: str) -> bool:
    expected_norm = _normalize(expected_item)

    expected_numbers = re.findall(r"\d+(?:\.\d+)?", expected_norm)
    if expected_numbers and not all(n in answer_norm for n in expected_numbers):
        return False

    return fuzz.partial_ratio(expected_norm, answer_norm) >= THRESHOLD


def judge(question, expects, answer, results) -> bool:
    """
    Judges the correctness of an answer based on the expected output.
    Same contract as an exact substring check, but uses rapidfuzz's
    partial_ratio so close paraphrases/formatting differences (e.g.
    "9-11 hours" vs "9 to 11 hours", "$1.75" vs "1.75 dollars") still
    count as correct instead of failing on an exact-string mismatch.

    Numbers in `expects` still have to appear verbatim in `answer`: a
    fuzzy ratio alone can't tell "30 minutes" from "40 minutes" apart —
    they're one character different — so a wrong number would otherwise
    still score above threshold.

    A comma-separated `expects` (a list question, e.g. "Halden Hall, North
    Kitchen, ...") is checked item by item instead of as one long string.
    `partial_ratio` on the whole list looks for one contiguous matching
    window, which a real answer never is — a bulleted list with a citation
    after each name spreads the same items across far more text, in a
    different order, so the single-window score comes out low even when
    every item is genuinely present.
    """
    answer_norm = _normalize(answer)
    items = [item.strip() for item in expects.split(",") if item.strip()]

    if len(items) > 1:
        return all(_item_matches(item, answer_norm) for item in items)

    return _item_matches(expects, answer_norm)
