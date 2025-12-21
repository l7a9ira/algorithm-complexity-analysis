from __future__ import annotations
from typing import Dict, List
import matplotlib.pyplot as plt

from src.experiments.benchmark import BenchmarkResult


def plot_runtime(results: Dict[str, List[BenchmarkResult]], *, title: str = "Sorting Runtime vs Input Size") -> None:
    """
    Plot mean runtime vs input size for each algorithm.

    We plot:
    - x: n
    - y: mean time (seconds)
    With error bars: ±1 std (variability across repeats)
    """
    plt.figure()
    for name, series in results.items():
        series_sorted = sorted(series, key=lambda r: r.n)
        ns = [r.n for r in series_sorted]
        means = [r.mean for r in series_sorted]
        stds = [r.stdev for r in series_sorted]
        plt.errorbar(ns, means, yerr=stds, marker="o", capsize=3, label=name)

    plt.xlabel("Input size n")
    plt.ylabel("Runtime (seconds)")
    plt.title(title)
    plt.grid(True)
    plt.legend() 
