"""
Oscar Nolen
Prithvi Koka
ITCS 6114
"""

import random

def quick_sort(arr):
    """In-place quick sort implementation."""
    if len(arr) <= 1:
        return arr

    # make copy to be safe
    result = arr.copy()
    quick_sort_helper(result, 0, len(result) - 1)
    return result

def quick_sort_helper(arr, left, right):
    """Recursive quick sort between indices left and right."""
    if left >= right:
        return

    # choose a random pivot
    pivot_index = random.randint(left, right)
    pivot = arr[pivot_index]

    # partition the array and get start + end of pivot section
    h, k = partition(arr, left, right, pivot)

    # sort elements less than pivot
    quick_sort_helper(arr, left, h - 1)

    # sort elements greater than pivot
    quick_sort_helper(arr, k + 1, right)

def partition(arr, left, right, pivot):
    """rearranges elements around pivot using 3-way partitioning."""
    i = left      # current index
    h = left      # boundary for elements less than pivot
    k = right     # boundary for elements greater than pivot

    while i <= k:
        if arr[i] < pivot:
            # move to less-than region
            arr[i], arr[h] = arr[h], arr[i]
            i += 1
            h += 1
        elif arr[i] > pivot:
            # move to greater-than region
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1
        else:
            # element equal to pivot, move on
            i += 1

    return h, k  # return bounds of the middle region

if __name__ == "__main__":
    # sample array to test the sort
    example_arr = [64, 34, 25, 12, 22, 11, 90, 25, 34, 25]

    print("original array:", example_arr)
    sorted_arr = quick_sort(example_arr)
    print("sorted array:", sorted_arr)
