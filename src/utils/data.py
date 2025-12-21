from __future__ import annotations
from typing import List
import random


def generate_random_array(n: int, *, low: int = 0, high: int = 10**6, seed: int | None = None) -> List[int]:
    """
    Generate a list of n random integers in [low, high].

    Notes:
    - For fair comparisons, experiments should use the SAME generated arrays for all algorithms.
    - Optional seed ensures reproducibility.
    """
    rng = random.Random(seed)
    return [rng.randint(low, high) for _ in range(n)]