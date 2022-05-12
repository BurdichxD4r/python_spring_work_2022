#  II вариант (алгоритм сортировки слиянием)
# Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 71 - 77.
#
# Задача.
# Перепишите процедуру  MERGE_SORT и отсортируйте последовательность
# A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13] по возрастанию


import math

def merge_sort(m, start, end):
   if end - start > 0:
       mid = (start + end) // 2 #вычисляем середину
       merge_sort(m, start, mid) # рекурсивно вызываем сортировку, "дробим" массив на максимально маленькие части
       merge_sort(m, mid+1, end)
       merge(m, start, mid, end)
   return m

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

print(merge_sort([31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13], 1, len([31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13])))