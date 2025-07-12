import time
from util import generate_random_array

def merge_sort(arr):
    """
    Merge sort implementation using divide and conquer approach.
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
        
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right array
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def test_merge_sort(n):
    """
    Test merge sort with different array sizes and types.
    
    Args:
        n: Size of the array to test
    """
    print(f"\nTesting merge sort with array size: {n}")
    
    # Test with random array
    random_arr = generate_random_array(n)
    print(f"Original random array (first 10): {random_arr[:10]}")
    
    start_time = time.time()
    sorted_arr = merge_sort(random_arr.copy())
    end_time = time.time()
    
    print(f"Sorted array (first 10): {sorted_arr[:10]}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    
    # Verify if the array is sorted
    is_sorted = all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1))
    print(f"Is correctly sorted: {is_sorted}")

# Example usage and testing
if __name__ == "__main__":
    # Example with a small array
    example_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Example array:", example_arr)
    sorted_example = merge_sort(example_arr)
    print("Sorted array:", sorted_example)
    
    # Test with different array sizes
    test_sizes = [10, 100, 1000, 10000]
    for size in test_sizes:
        test_merge_sort(size)