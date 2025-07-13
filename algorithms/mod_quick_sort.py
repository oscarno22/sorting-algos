"""
Oscar Nolen
ITCS 6114
"""

from .insertion_sort import insertion_sort_range


def mod_quick_sort(arr, threshold=20):
    """Modified quicksort using median-of-three pivot and insertion sort for small subarrays."""
    if len(arr) <= 1:
        return arr

    # Create a copy to avoid modifying the original array
    result = arr.copy()
    quick_sort_helper(result, 0, len(result) - 1, threshold)
    return result


def quick_sort_helper(arr, low, high, threshold):
    """Recursive helper function for modified quicksort."""
    if low < high:
        # If subarray is small, use insertion sort
        if high - low + 1 <= threshold:
            insertion_sort_range(arr, low, high)
        else:
            # Use median-of-three pivot and partition
            pivot_index = partition(arr, low, high)

            # Recursively sort elements before and after partition
            quick_sort_helper(arr, low, pivot_index - 1, threshold)
            quick_sort_helper(arr, pivot_index + 1, high, threshold)


def median_of_three(arr, low, mid, high):
    """Find the median of three elements and return its index."""
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low
    else:
        return high


def partition(arr, low, high):
    """Partition function using median-of-three as pivot."""
    # Find median of three elements
    mid = (low + high) // 2
    median_index = median_of_three(arr, low, mid, high)

    # Move median to the end to use as pivot
    arr[median_index], arr[high] = arr[high], arr[median_index]

    # Use the same partitioning logic as standard quicksort
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
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
    sorted_arr = mod_quick_sort(example_arr)
    print("Sorted array (mod quicksort):", sorted_arr)
