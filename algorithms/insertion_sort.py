"""
Oscar Nolen
ITCS 6114
"""


def insertion_sort(arr):
    """Insertion sort implementation."""
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def insertion_sort_range(arr, low, high):
    """Insertion sort for a specific range of the array (in-place)."""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key


if __name__ == "__main__":
    # Example with a small array
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", example_arr)
    sorted_arr = insertion_sort(example_arr)
    print("Sorted array:", sorted_arr)
