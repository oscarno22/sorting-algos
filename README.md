# Sorting Algorithms

**Author:** Oscar Nolen  
**Course:** ITCS 6114  
**Project:** Comparison-based Sorting Algorithms

## Project Structure

```
project_1/
├── insertion_sort.py      # Insertion sort implementation
├── merge_sort.py          # Merge sort implementation  
├── quick_sort.py          # Standard quicksort implementation
├── mod_quick_sort.py      # Modified quicksort with median-of-three pivot
├── heap_sort.py           # Heap sort implementation
├── algorithms.py          # Combined module for all algorithms
├── test.py                # Main test suite with timing
└── README.md              # Test suite instructions
```

## Implemented Algorithms

1. **Insertion Sort** - Simple comparison-based sorting
2. **Merge Sort** - Divide and conquer recursive sorting
3. **Quick Sort** - In-place partitioning with random element as pivot
4. **Modified Quick Sort** - Hybrid approach with median-of-three pivot and insertion sort for small subarrays (size <=20)
5. **Heap Sort** - Vector-based heap with one-at-a-time insertion

## Running the Tests

### Prerequisites

- Python (3.12 preferred)

### Basic Usage

```bash
# Run all tests (best case, worst case, and random case)
python test.py

# Run only random case tests
python test.py --random

# Run only best case tests (sorted arrays)
python test.py --best

# Run only worst case tests (reverse sorted arrays)
python test.py --worst
```

Results are outputted to `test_results.txt`.

### Test Configuration

The test suite runs with the following array sizes:
- 1,000, 2,000, 3,000, 4,000, 5,000, 10,000, 40,000, 50,000, 60,000 elements

### Test Cases

1. **Best Case**: Pre-sorted arrays (ascending order)
2. **Worst Case**: Reverse-sorted arrays (descending order)
3. **Random Case**: Randomly generated arrays with values 1-1000

## Individual Algorithm Testing

Each algorithm file can be run independently for quick verification:

```bash
python insertion_sort.py
python merge_sort.py
python quick_sort.py
python mod_quick_sort.py
python heap_sort.py
```
