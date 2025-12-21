from __future__ import annotations
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort (O(n log n) in all cases).

    Idea:
    - Divide array into halves until size 0/1
    - Merge sorted halves

    Returns a NEW sorted list.
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists in O(len(left)+len(right)).
    """
    merged: List[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged 
