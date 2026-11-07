from __future__ import annotations

import statistics
import sys


def relative_performance(values: list[float]) -> dict[str, float | int | None]:
    """Compare the final value with the median baseline supplied by the user."""
    if not values:
        return {"sample_size": 0, "median": None, "last_value_multiple": None}
    baseline = statistics.median(values[:-1]) if len(values) > 1 else None
    last = values[-1]
    return {
        "sample_size": len(values) - 1,
        "median": baseline,
        "last_value_multiple": (last / baseline if baseline else None),
    }


if __name__ == "__main__":
    nums = [float(arg) for arg in sys.argv[1:]]
    print(relative_performance(nums))
