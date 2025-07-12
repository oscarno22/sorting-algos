"""
Oscar Nolen
ITCS 6114
"""

import random
from typing import List


def generate_random_array(n, min_val=1, max_val=1000):
    """Generate a random array of size n for testing."""
    return [random.randint(min_val, max_val) for _ in range(n)]


def generate_sorted_array(n):
    """Generate a sorted array of size n for testing best case."""
    return List(range(1, n + 1))


def generate_reverse_sorted_array(n):
    """Generate a reverse sorted array of size n for testing worst case."""
    return List(range(n, 0, -1))
