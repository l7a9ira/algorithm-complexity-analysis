from __future__ import annotations
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort (O(n^2) average/worst).

    Idea:
    - Repeatedly sweep through the list.
    - Swap adjacent out-of-order elements.
    - After each pass, the largest remaining element "bubbles" to the end.

    Returns a NEW sorted list (does not mutate the input).
    """
    a = arr[:]  # copy to keep experiments fair and non-destructive
    n = len(a)

    for i in range(n):
        swapped = False
        # last i elements already in correct place
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        # Optimization for best-case nearly-sorted arrays (still O(n^2) worst-case)
        if not swapped:
            break

    return a