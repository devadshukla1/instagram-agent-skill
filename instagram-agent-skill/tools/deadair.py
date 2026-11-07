from __future__ import annotations

import re
import sys


def find_filler(text: str) -> list[tuple[str, int]]:
    """Find common filler phrases and their character offsets for review."""
    pattern = re.compile(r"\b(um+|uh+|you know|like|basically|so yeah)\b", re.I)
    return [(match.group(0), match.start()) for match in pattern.finditer(text)]


if __name__ == "__main__":
    print(find_filler(" ".join(sys.argv[1:])))
