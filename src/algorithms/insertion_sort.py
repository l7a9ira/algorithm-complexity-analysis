from __future__ import annotations
from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort (O(n^2) average/worst).

    Idea:
    - Grow a sorted prefix.
    - Insert next element into its correct position in the prefix.

    Returns a NEW sorted list (does not mutate the input).
    """
    a = arr[:]
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        # Shift larger elements to the right until the correct position is found
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a
