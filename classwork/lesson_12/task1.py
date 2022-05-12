#todo: Реализовать декоратор который подсчитывает время выполнения функции.
# Для этого необходимо взять время до начала запуска функции и после ее окончания.
# Проверить декоратор для различного рода алгоритмов сортировок на большом наборе данных.


import time
import random
import math
A = list()
print('Загрузка списка ...')
while len(A) < 10000:
    A.append(random.randint(0, 100))

def decorator_render(fune):
    print('Обработка списка ...')
    def w(A):
        fune(A)
    return w

@decorator_render
def insertion_sort(mas):
    for i in range(1, len(mas)):
        key = mas[i]
        j = i-1
        while j >=0 and key > mas[j] :
            mas[j+1] = mas[j]
            j -= 1
        mas[j+1] = key
start_time = time.time()
insertion_sort(A)
print('1 Вариант\nчто-то там')
print('Потребовалось секунд:', round(time.time() - start_time, 2))


def merge(A, p, q, r):
    n1 = q - p + 1 # вычисляем длину левого и правого массива - вычитаем из среднего указателя начало (добавляем 1, чтобы не пересекался с правым)
    n2 = r - q #аналогично правый - из конечного вычисляем среднийй
    L = [0] * (n1 + 1) # создаем массив их нулей чтобы заполнить соотв числами из основного массива
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p+i-1] #заполняем
    for j in range(n2):
        R[j] = A[q+j]
    L[n1] = math.inf #ставим бесконечность в конец, чтобы когда мы сравнивали массив и один из них кончился, мы бы не ломали счетчики
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p-1, r): #заходим в цикл где будем сравнивать левый и правый массивы
        if L[i] <= R[j]: #если след. число из левого массива меньше правого, ставим левое
            A[k] = L[i]
            i += 1 #увеличиваем счетчик - переходим на след. число ЛЕВОГО массива
        else:
            A[k] = R[j] #иначе добавляем правое и переходим на след число ПРАВОГО массива
            j += 1
    return A
def merge_sort(m, start, end):
   if end - start > 0:
       mid = (start + end) // 2 #вычисляем середину
       merge_sort(m, start, mid) # рекурсивно вызываем сортировку, "дробим" массив на максимально маленькие части
       merge_sort(m, mid+1, end)
       merge(m, start, mid, end)
   return m

start_time = time.time()
merge_sort(A, 1, len(A))
print('2 Вариант\nСортировка слиянием')
print('Потребовалось секунд:', round(time.time() - start_time, 2))

def PARENT(i):
    return int(i / 2)
def LEFT(i):
    return int(i * 2)
def RIGHT(i):
    return int(i * 2 + 1)
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

@decorator_render
def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MAX_HEAPIFY(A, index=0, size=i)

start_time = time.time()
HEAPSORT(A)
print('3 Вариант\nПирамидальная сортировка')
print('Потребовалось секунд:', round(time.time() - start_time, 2))