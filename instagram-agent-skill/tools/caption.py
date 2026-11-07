from __future__ import annotations

import re
import sys


def lint_caption(text: str) -> dict[str, object]:
    """Return transparent, simple caption checks; not an Instagram ranking model."""
    words = re.findall(r"\b[\w’'-]+\b", text)
    hashtags = re.findall(r"(?<!\w)#[\w]+", text)
    first_line = text.strip().splitlines()[0] if text.strip() else ""
    return {
        "characters": len(text),
        "words": len(words),
        "hashtags": len(hashtags),
        "first_line_characters": len(first_line),
        "has_call_to_action_hint": bool(re.search(r"\b(save|share|comment|follow|send)\b", text, re.I)),
    }


if __name__ == "__main__":
    value = " ".join(sys.argv[1:])
    print(lint_caption(value))
