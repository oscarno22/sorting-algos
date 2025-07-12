import random

def generate_random_array(n, min_val=1, max_val=1000):
    """
    Generate a random array of size n for testing.
    
    Args:
        n: Size of the array
        min_val: Minimum value for random integers
        max_val: Maximum value for random integers
        
    Returns:
        List of n random integers
    """
    return [random.randint(min_val, max_val) for _ in range(n)]

def generate_sorted_array(n):
    """
    Generate a sorted array of size n for testing best case.
    
    Args:
        n: Size of the array
        
    Returns:
        List of n sorted integers
    """
    return list(range(1, n + 1))

def generate_reverse_sorted_array(n):
    """
    Generate a reverse sorted array of size n for testing worst case.
    
    Args:
        n: Size of the array
        
    Returns:
        List of n reverse sorted integers
    """
    return list(range(n, 0, -1))