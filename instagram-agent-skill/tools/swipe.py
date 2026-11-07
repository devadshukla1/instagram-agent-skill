from __future__ import annotations

import json
import sys


def summarize_posts(raw: str) -> dict[str, object]:
    """Summarize a JSON list of post records without inventing missing metrics."""
    posts = json.loads(raw)
    if not isinstance(posts, list):
        raise ValueError("Expected a JSON array of post records")
    return {"post_count": len(posts), "posts": posts}


if __name__ == "__main__":
    print(summarize_posts(" ".join(sys.argv[1:])))
