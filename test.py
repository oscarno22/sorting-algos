"""
Oscar Nolen
ITCS 6114
"""

import random
import argparse
import time
from typing import List
from algorithms import (
    insertion_sort, 
    merge_sort, 
    mod_quick_sort, 
    quick_sort, 
    heap_sort
)

algorithms = [
    (insertion_sort, "Insertion Sort"),
    (merge_sort, "Merge Sort"),
    (mod_quick_sort, "Modified Quick Sort"),
    (quick_sort, "Quick Sort"),
    (heap_sort, "Heap Sort"),
]


def generate_random_array(n, min_val=1, max_val=1000):
    """Generate a random array of size n for testing."""
    return [random.randint(min_val, max_val) for _ in range(n)]


def generate_sorted_array(n):
    """Generate a sorted array of size n for testing best case."""
    return List(range(1, n + 1))


def generate_reverse_sorted_array(n):
    """Generate a reverse sorted array of size n for testing worst case."""
    return List(range(n, 0, -1))


def time_algorithm(algorithm, data, algorithm_name=""):
    """Time a sorting algorithm and return the elapsed time in seconds."""
    start_time = time.perf_counter()
    result = algorithm(data)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time


def test_sorting_algorithms(test_type="all"):
    """Test all sorting algorithms with various cases and timing."""
    sizes = [1000, 2000, 3000, 4000, 5000, 10000, 40000, 50000, 60000]

    for size in sizes:
        print(f"\nTesting with array size: {size}")
        print("=" * 50)

        if test_type in ["all", "best"]:
            # Best case: sorted array
            print(f"  Best Case Tests (size {size}):")
            best_case = generate_sorted_array(size)

            for algorithm, name in algorithms:
                test_data = best_case.copy() if name != "Insertion Sort" else best_case
                result, elapsed_time = time_algorithm(algorithm, test_data, name)

                # check result
                assert result == best_case, f"{name} failed correctness test"

                print(f"    {name:20}: {elapsed_time:.6f} seconds")

        if test_type in ["all", "worst"]:
            # Worst case: reverse sorted array
            print(f"  Worst Case Tests (size {size}):")
            worst_case = generate_reverse_sorted_array(size)
            expected_result = sorted(worst_case)

            for algorithm, name in algorithms:
                test_data = worst_case.copy()
                result, elapsed_time = time_algorithm(algorithm, test_data, name)

                # check result
                assert result == expected_result, f"{name} failed correctness test"

                print(f"    {name:20}: {elapsed_time:.6f} seconds")

        if test_type in ["all", "random"]:
            # Average case: random array
            print(f"  Random Case Tests (size {size}):")
            random_array = generate_random_array(size)
            expected_result = sorted(random_array)

            for algorithm, name in algorithms:
                test_data = random_array.copy()
                result, elapsed_time = time_algorithm(algorithm, test_data, name)

                # check result
                assert result == expected_result, f"{name} failed correctness test"

                print(f"    {name:20}: {elapsed_time:.6f} seconds")

    print(f"\nAll {test_type} tests passed with timing measurements!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test sorting algorithms")
    parser.add_argument("--random", action="store_true", help="Run only random tests")
    parser.add_argument("--best", action="store_true", help="Run only best case tests")
    parser.add_argument(
        "--worst", action="store_true", help="Run only worst case tests"
    )

    args = parser.parse_args()

    # Determine which tests to run
    if args.random:
        test_type = "random"
    elif args.best:
        test_type = "best"
    elif args.worst:
        test_type = "worst"
    else:
        test_type = "all"

    print(f"Running {test_type} tests...")
    test_sorting_algorithms(test_type)
