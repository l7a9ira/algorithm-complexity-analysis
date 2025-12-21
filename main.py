"""
main.py

Runs controlled timing experiments for:
- Bubble Sort (O(n^2))
- Insertion Sort (O(n^2))
- Merge Sort (O(n log n))

Outputs:
- printed table of average runtimes
- matplotlib plot: runtime vs input size (with error bars)
"""

from __future__ import annotations

import os

from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.insertion_sort import insertion_sort
from src.algorithms.merge_sort import merge_sort

from src.utils.data import generate_random_array
from src.experiments.benchmark import benchmark_suite
from src.utils.plotting import plot_runtime


def build_datasets(ns: list[int], *, seed: int = 0) -> list[tuple[int, list[int]]]:
    """
    Generate one random array per n.

    Academic fairness:
    - Use a fixed seed so results are reproducible.
    - Use the same arrays for all algorithms at each n.
    """
    datasets = []
    for n in ns:
        arr = generate_random_array(n, seed=seed + n)  # vary seed with n
        datasets.append((n, arr))
    return datasets


def print_results_table(results):
    print("\n=== Benchmark Results (mean ± std, seconds) ===")
    # assume all algorithms share same ns
    alg_names = list(results.keys())
    ns = [r.n for r in results[alg_names[0]]]

    header = "n".ljust(8) + "".join(name.ljust(24) for name in alg_names)
    print(header)
    print("-" * len(header))

    for i, n in enumerate(ns):
        row = str(n).ljust(8)
        for name in alg_names:
            r = results[name][i]
            row += f"{r.mean:.6f} ± {r.stdev:.6f}".ljust(24)
        print(row)


def main():
    os.makedirs("outputs", exist_ok=True)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
    }

    # Choose input sizes.
    # Note: O(n^2) algorithms get slow fast, so keep ns moderate.
    ns = [100, 200, 400, 800, 1200, 1600]

    datasets = build_datasets(ns, seed=42)

    results = benchmark_suite(algorithms, datasets, repeats=7)
    print_results_table(results)

    plot_runtime(results, title="Sorting Runtime vs Input Size (Mean ± Std)")
    # Save figure for GitHub / report
    import matplotlib.pyplot as plt
    plt.savefig("outputs/runtime_vs_n.png", dpi=200, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
