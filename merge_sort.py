"""
Oscar Nolen
ITCS 6114
"""


def merge_sort(arr):
    """Merge sort implementation."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


if __name__ == "__main__":
    # Example with a small array
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", example_arr)
    sorted_arr = merge_sort(example_arr)
    print("Sorted array:", sorted_arr)
