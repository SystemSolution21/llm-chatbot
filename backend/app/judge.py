# app/judge.py


def score_answer(answer: str) -> int:
    """Score an answer on a scale from 0 to 10."""

    # simple heuristic placeholder
    if "I don't know" in answer:
        return 2
    return 8
