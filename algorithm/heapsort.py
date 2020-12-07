def heap_adjust(A, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    max_index = i
    if (left < size and A[max_index] < A[left]):
        max_index = left
    if (right < size and A[max_index] < A[right]):
        max_index = right
    if (max_index != i):
        temp = A[max_index]
        A[max_index] = A[i]
        A[i] = temp
        heap_adjust(A, max_index, size)


def build_heap(A, size):
    for i in range(int(size / 2), -1, -1):
        heap_adjust(A, i, size)


def heap_sorting(A):
    size = len(A)
    build_heap(A, size)
    for i in range(len(A) - 1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        heap_adjust(A, 0, i)
    return A


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(heap_sorting(arr))