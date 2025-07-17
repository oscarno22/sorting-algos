"""
Oscar Nolen
Prithvi Koka
ITCS 6114
"""

def merge_sort(arr):
    """Recursive merge sort function."""
    # arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # merge the two sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Merge two sorted arrays into a single sorted array."""
    result = []
    i = 0  # pointer for left
    j = 0  # pointer for right

    # compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # if there are remaining elements in left, append them
    while i < len(left):
        result.append(left[i])
        i += 1

    # if there are remaining elements in right, append them
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

if __name__ == "__main__":
    # Just a sample array to test the sort
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", example_arr)
    sorted_arr = merge_sort(example_arr)
    print("Sorted array:", sorted_arr)
