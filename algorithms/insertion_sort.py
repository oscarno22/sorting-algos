"""
Oscar Nolen
Prithvi Koka
ITCS 6114
"""

def insertion_sort(arr):
    """Insertion sort implementation."""
    # arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # go through each element starting from index 1
    for i in range(1, len(arr)):
        j = i
        # move the current element leftward until it's in correct spot
        while j > 0 and arr[j - 1] > arr[j]:
            # swap if the left neighbor is bigger
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

def insertion_sort_range(arr, low, high):
    """Insertion sort for a specific range of the array (in-place)."""
    # start from low + 1 and sort up to high
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1

        # shift elements greater than key one spot to the right
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key in its correct position
        arr[j + 1] = key

if __name__ == "__main__":
    # Just a sample array to test the sort
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", example_arr)
    sorted_arr = insertion_sort(example_arr)
    print("Sorted array:", sorted_arr)
