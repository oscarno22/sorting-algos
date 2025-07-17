"""
Oscar Nolen
ITCS 6114
"""

from .insertion_sort import insertion_sort_range

def mod_quick_sort(arr, threshold=20):
    """Modified quicksort using median-of-three and insertion sort for <= threshold size."""
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    quick_sort_helper(result, 0, len(result) - 1, threshold)
    return result

def quick_sort_helper(arr, left, right, threshold):
    """Recursive helper for modified quicksort"""
    if left + threshold <= right:
        # median-of-three pivot
        pivot = median_of_three(arr, left, right)

        # move pivot to right - 1
        arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]

        # start i and j for partitioning
        i = left
        j = right - 1

        while True:
            # move i right until arr[i] ≥ pivot
            while True:
                i += 1
                if arr[i] >= arr[right - 1]:
                    break

            # move j left until arr[j] ≤ pivot
            while True:
                j -= 1
                if arr[j] <= arr[right - 1]:
                    break

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        # place pivot in its final position
        arr[i], arr[right - 1] = arr[right - 1], arr[i]

        # recursive calls
        quick_sort_helper(arr, left, i - 1, threshold)
        quick_sort_helper(arr, i + 1, right, threshold)

    else:
        # use insertion sort for small partitions
        insertion_sort_range(arr, left, right)

def median_of_three(arr, left, right):
    """Returns index of median among arr[left], arr[mid], arr[right]"""
    mid = (left + right) // 2

    # ensure arr[left] <= arr[mid] <= arr[right]
    if arr[mid] < arr[left]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[right] < arr[left]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[right] < arr[mid]:
        arr[mid], arr[right] = arr[right], arr[mid]

    # return index of median (which is now at mid)
    return mid

if __name__ == "__main__":
    # sample array to test modified quicksort
    example_arr = [64, 34, 25, 12, 22, 11, 90, 18, 77, 49, 26]

    print("original array:", example_arr)
    sorted_arr = mod_quick_sort(example_arr)
    print("sorted array:", sorted_arr)
