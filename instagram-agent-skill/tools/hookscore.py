from __future__ import annotations

import re
import sys


PATTERNS = {
    "specificity": r"\b\d+\b",
    "direct_address": r"\b(you|your|you're|you've)\b",
    "curiosity": r"\b(why|secret|mistake|truth|stop|never|nobody|what if)\b",
    "contrast": r"\b(but|instead|without|vs\.?|rather than)\b",
    "urgency": r"\b(now|today|before|until|seconds|days)\b",
}


def score_hook(text: str) -> dict[str, object]:
    """A transparent heuristic checklist, not a prediction of reach or views."""
    points = {name: int(bool(re.search(pattern, text, re.I))) for name, pattern in PATTERNS.items()}
    word_count = len(text.split())
    brevity = int(3 <= word_count <= 12)
    total = sum(points.values()) + brevity
    return {"score": total, "max_score": 6, "signals": points, "brevity": brevity}


if __name__ == "__main__":
    print(score_hook(" ".join(sys.argv[1:])))
