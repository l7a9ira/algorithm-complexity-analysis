from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple
import time
import statistics

from src.utils.validation import is_sorted_non_decreasing


SortFn = Callable[[List[int]], List[int]]


@dataclass(frozen=True)
class BenchmarkResult:
    n: int
    times_sec: List[float]

    @property
    def mean(self) -> float:
        return statistics.mean(self.times_sec)

    @property
    def stdev(self) -> float:
        # stdev requires at least 2 points; return 0.0 otherwise
        return statistics.stdev(self.times_sec) if len(self.times_sec) >= 2 else 0.0


def time_function(sort_fn: SortFn, arr: List[int], *, repeats: int = 5) -> List[float]:
    """
    Time a sorting function fairly.

    Key fairness rule:
    - Each repeat gets the SAME input values (we pass a fresh list copy each time),
      so algorithms are compared on identical data.
    """
    times: List[float] = []

    # Optional warm-up run to reduce one-time overhead impact
    _ = sort_fn(arr)

    for _ in range(repeats):
        data = arr[:]  # fresh copy
        start = time.perf_counter()
        out = sort_fn(data)
        end = time.perf_counter()

        # Validate correctness (important for academic projects)
        if not is_sorted_non_decreasing(out):
            raise ValueError(f"Sorting failed correctness check for n={len(arr)}")

        times.append(end - start)

    return times


def benchmark_suite(
    algorithms: Dict[str, SortFn],
    datasets: List[Tuple[int, List[int]]],
    *,
    repeats: int = 7
) -> Dict[str, List[BenchmarkResult]]:
    """
    Benchmark multiple algorithms on multiple dataset sizes.

    Parameters
    ----------
    algorithms: dict[name -> function]
    datasets: list of (n, array) where array is the base input for that n
    repeats: number of timing repeats per (algorithm, n)

    Returns
    -------
    results[name] = list of BenchmarkResult sorted by n
    """
    results: Dict[str, List[BenchmarkResult]] = {name: [] for name in algorithms}

    for name, fn in algorithms.items():
        for n, arr in datasets:
            times = time_function(fn, arr, repeats=repeats)
            results[name].append(BenchmarkResult(n=n, times_sec=times))

    return results