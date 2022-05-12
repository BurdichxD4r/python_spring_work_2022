#todo: I вариант (алгоритм сортировки вставками)
'''
Реализовать на Python алгоритм сортировки вставками представленный в псевдокоде
в учебнике “Introduction to Algorithms”  на стр. 57 - 63.

Задача.
Перепишите процедуру INSERTION_SORT и отсортируйте последовательность
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7] по убыванию.
'''
def insertion_sort(mas):
    for i in range(1, len(mas)):
        key = mas[i]
        j = i-1
        while j >=0 and key > mas[j] :
            mas[j+1] = mas[j]
            j -= 1
        mas[j+1] = key

A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7]
insertion_sort(A)
print ("Sorted array is:")
for i in range(len(A)):
    print (A[i])
