from __future__ import annotations

import sys


def retention_drops(values: list[float]) -> list[tuple[int, float]]:
    """Return adjacent drops in supplied retention percentages."""
    return [(i, values[i - 1] - values[i]) for i in range(1, len(values))]


if __name__ == "__main__":
    values = [float(value) for value in sys.argv[1:]]
    print(retention_drops(values))
