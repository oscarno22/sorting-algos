"""
Oscar Nolen
ITCS 6114
"""

import random


def quick_sort(arr):
    """Quick sort implementation (in-place)."""
    if len(arr) <= 1:
        return arr

    # Create a copy to avoid modifying the original array
    result = arr.copy()
    quick_sort_helper(result, 0, len(result) - 1)
    return result


def quick_sort_helper(arr, low, high):
    """Recursive helper function for quicksort."""
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort_helper(arr, low, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """Partition function using a random element as pivot."""
    # Choose a random element as pivot and swap it with the last element
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # Now proceed with the last element as pivot (which is now random)
    pivot = arr[high]

    # Index of smaller element (indicates the right position of pivot)
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Example with a small array
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", example_arr)

    # Test with last element as pivot (default)
    sorted_arr = quick_sort(example_arr)
    print("Sorted array (last pivot):", sorted_arr)
