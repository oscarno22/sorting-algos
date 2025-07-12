"""
Oscar Nolen
ITCS 6114
"""


def heap_sort(arr):
    """Heap sort implementation using a vector-based heap."""
    if len(arr) <= 1:
        return arr

    result = []
    heap = []

    # Insert elements one at a time
    for element in arr:
        heap_insert(heap, element)

    # Extract from heap to get sorted order
    while heap:
        result.append(heap_extract_max(heap))

    # Since we extracted max elements, reverse to get ascending order
    return result[::-1]


def heap_insert(heap, element):
    """Insert an element into the heap and maintain heap property."""
    heap.append(element)
    bubble_up(heap, len(heap) - 1)


def heap_extract_max(heap):
    """Extract the maximum element from the heap."""
    if not heap:
        return None

    if len(heap) == 1:
        return heap.pop()

    max_element = heap[0]
    heap[0] = heap.pop()
    bubble_down(heap, 0)

    return max_element


def bubble_up(heap, index):
    """Bubble up element at index to maintain heap property."""
    while index > 0:
        parent_index = (index - 1) // 2
        if heap[index] <= heap[parent_index]:
            break
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        index = parent_index


def bubble_down(heap, index):
    """Bubble down element at index to maintain heap property."""
    while True:
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        # Find largest among parent and children
        if left_child < len(heap) and heap[left_child] > heap[largest]:
            largest = left_child

        if right_child < len(heap) and heap[right_child] > heap[largest]:
            largest = right_child

        # If parent is the largest, heap property is satisfied
        if largest == index:
            break

        # Swap and continue
        heap[index], heap[largest] = heap[largest], heap[index]
        index = largest


if __name__ == "__main__":
    # Example with a small array
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", example_arr)
    sorted_arr = heap_sort(example_arr)
    print("Sorted array:", sorted_arr)
