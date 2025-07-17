"""
Oscar Nolen
ITCS 6114
"""

import random
import argparse
import time
import sys
from algorithms import (
    insertion_sort,
    merge_sort,
    mod_quick_sort,
    quick_sort,
    heap_sort,
)

algorithms = [
    (insertion_sort, "Insertion Sort"),
    (merge_sort, "Merge Sort"),
    (mod_quick_sort, "Modified Quick Sort"),
    (quick_sort, "Quick Sort"),
    (heap_sort, "Heap Sort"),
]


def generate_random_array(n, min_val=1, max_val=1000):
    """generate a random array of size n"""
    return [random.randint(min_val, max_val) for _ in range(n)]


def generate_sorted_array(n):
    """generate a sorted array of size n"""
    return list(range(1, n + 1))


def generate_reverse_sorted_array(n):
    """generate a reverse sorted array of size n"""
    return list(range(n, 0, -1))


def time_algorithm(algorithm, data):
    """time a sorting algorithm and return the elapsed time in seconds"""
    start_time = time.perf_counter()
    result = algorithm(data)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time


def write_output(message, file_handle=None, console_message=None):
    """write message to both console and file"""
    if console_message is not None and console_message != "":
        print(console_message)
        sys.stdout.flush()
    elif console_message is None:
        print(message)
        sys.stdout.flush()

    if file_handle:
        file_handle.write(message + "\n")
        file_handle.flush()


def test_sorting_algorithms(test_type="all", output_file="test_results.txt"):
    """test all sorting algorithms with different input types"""
    sizes = [1000, 2000, 3000, 4000, 5000, 10000, 40000, 50000, 60000]

    with open(output_file, "w") as f:
        header = "Sorting Algorithm Performance Test Results"
        write_output("=" * len(header), f, "")
        write_output(header, f, "")
        write_output("=" * len(header), f, "")
        write_output(f"Test Type: {test_type}", f, "")
        write_output(f"Array Sizes: {sizes}", f, "")
        write_output("", f, "")

        for size in sizes:
            size_header = f"Testing with array size: {size}"
            write_output(size_header, f, f"Testing array size: {size}")
            write_output("=" * 50, f, "")

            if test_type in ["all", "sorted"]:
                write_output(f"  Sorted Input (size {size}):", f, "  Running sorted input tests...")
                sorted_case = generate_sorted_array(size)

                for algorithm, name in algorithms:
                    test_data = sorted_case.copy()
                    result, elapsed_time = time_algorithm(algorithm, test_data)

                    try:
                        assert result == sorted_case, f"{name} failed correctness test"
                        write_output(f"    {name:20}: {elapsed_time:.6f} seconds", f, "")
                    except AssertionError as e:
                        error_msg = f"    {name:20}: FAILED - {str(e)}"
                        write_output(error_msg, f, f"    {name}: FAILED")

                write_output("", f, "  ✓ Sorted input tests completed")

            if test_type in ["all", "reverse"]:
                write_output(f"  Reverse Sorted Input (size {size}):", f, "  Running reverse sorted input tests...")
                reverse_case = generate_reverse_sorted_array(size)
                expected_result = sorted(reverse_case)

                for algorithm, name in algorithms:
                    test_data = reverse_case.copy()
                    result, elapsed_time = time_algorithm(algorithm, test_data)

                    try:
                        assert result == expected_result, f"{name} failed correctness test"
                        write_output(f"    {name:20}: {elapsed_time:.6f} seconds", f, "")
                    except AssertionError as e:
                        error_msg = f"    {name:20}: FAILED - {str(e)}"
                        write_output(error_msg, f, f"    {name}: FAILED")

                write_output("", f, "  ✓ Reverse sorted input tests completed")

            if test_type in ["all", "random"]:
                write_output(f"  Random Input (size {size}):", f, "  Running random input tests...")
                random_array = generate_random_array(size)
                expected_result = sorted(random_array)

                for algorithm, name in algorithms:
                    test_data = random_array.copy()
                    result, elapsed_time = time_algorithm(algorithm, test_data)

                    try:
                        assert result == expected_result, f"{name} failed correctness test"
                        write_output(f"    {name:20}: {elapsed_time:.6f} seconds", f, "")
                    except AssertionError as e:
                        error_msg = f"    {name:20}: FAILED - {str(e)}"
                        write_output(error_msg, f, f"    {name}: FAILED")

                write_output("", f, "  ✓ Random input tests completed")

        final_msg = f"All {test_type} tests completed! Results saved to {output_file}"
        write_output(final_msg, f, f"All tests completed! Results saved to {output_file}")
        write_output("=" * len(final_msg), f, "")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test sorting algorithms")
    parser.add_argument("--random", action="store_true", help="Run only random tests")
    parser.add_argument("--sorted", action="store_true", help="Run only sorted input tests")
    parser.add_argument("--reverse", action="store_true", help="Run only reverse sorted input tests")

    args = parser.parse_args()

    if args.random:
        test_type = "random"
    elif args.sorted:
        test_type = "sorted"
    elif args.reverse:
        test_type = "reverse"
    else:
        test_type = "all"

    print(f"Running {test_type} tests...")
    print("Results will be saved to: test_results.txt")
    test_sorting_algorithms(test_type)
