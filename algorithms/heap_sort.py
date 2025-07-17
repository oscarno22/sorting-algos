"""
Oscar Nolen
ITCS 6114
"""

def heap_sort(arr):
    """Heap sort using vector-based heap."""
    if len(arr) <= 1:
        return arr

    heap = [None]  # dummy value at index 0
    result = []

    # insert each item into heap
    for val in arr:
        heap_insert(heap, val)

    # remove items from the heap to get sorted order
    while len(heap) > 1:
        result.append(heap_remove_min(heap))

    return result


def heap_insert(heap, val):
    """Insert value into heap and restore heap order"""
    heap.append(val)  # insert at end
    i = len(heap) - 1  # current index

    # bubble up
    while i > 1 and heap[i // 2] > heap[i]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i = i // 2


def heap_remove_min(heap):
    """Remove and return min element from heap"""
    if len(heap) <= 1:
        return None

    # root is at index 1
    min_val = heap[1]

    # move last element to root and shrink heap
    heap[1] = heap[-1]
    heap.pop()
    n = len(heap) - 1
    i = 1

    # bubble down
    while i * 2 <= n:
        left = i * 2
        right = i * 2 + 1
        smallest = i

        if left <= n and heap[left] < heap[smallest]:
            smallest = left
        if right <= n and heap[right] < heap[smallest]:
            smallest = right

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest

    return min_val


if __name__ == "__main__":
    example_arr = [64, 34, 25, 12, 22, 11, 90]

    print("original array:", example_arr)
    sorted_arr = heap_sort(example_arr)
    print("sorted array:", sorted_arr)
