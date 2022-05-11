# todo: III вариант (пирамидальная сортировка)
# Реализовать на Python пирамидальную сортировку представленную в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 178 - 184.
#
# Задача.
# Перепишите процедуру  MAX_HEAPIFY и напечатайте получившееся бинарное дерево
# при входном списке
A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]

def PARENT(i):
    return int(i / 2)
def LEFT(i):
    return int(i * 2)
def RIGHT(i):
    return int(i * 2 + 1)
# Свойство  невозрастающих пирамид max-heap property
# A[PARENT(i)] >= A[i]
# Свойство неубывающих пирамид (min-heap property)
# A[PARENT(i)] <= A[i]
def MAX_HEAPIFY(A, index, size):
    l = LEFT(index)
    r = RIGHT(index)
    if (l < size and A[l] > A[index]):
        largest = l
    else:
        largest = index
    if (r < size and A[r] > A[largest]):
        largest = r
    if (largest != index):
        A[largest], A[index] = A[index], A[largest]
        MAX_HEAPIFY(A, largest, size)
def BUILD_MAX_HEAP(A):
    length = len(A)
    start = PARENT(length - 1)
    while start >= 0:
        MAX_HEAPIFY(A, index=start, size=length)
        start = start - 1
def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MAX_HEAPIFY(A, index=0, size=i)

HEAPSORT(A)
print(A)
print(list(reversed(A)))