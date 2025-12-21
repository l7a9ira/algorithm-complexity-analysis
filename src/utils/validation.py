from __future__ import annotations
from typing import List


def is_sorted_non_decreasing(arr: List[int]) -> bool:
    """Check if array is sorted in non-decreasing order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))