import random
import numpy as np

# todo: Задание 1
matrix = np.random.randint(-25, 25, (int(input('Введите число строк: ')), int(input('Введите число столбцов: '))))
print(matrix)


def summ_positive_matrix(list):
    summ = 0
    matrix_list = [number for numbers in list for number in numbers]
    for number in matrix_list:
        if number > 0:
            summ += number
    return summ


def summ_positive_columns(list):
    list = list.T
    summ = 0
    list_summ = []
    for numbers in list:
        for number in numbers:
            if number > 0:
                summ += number
        list_summ.append(summ)
        summ = 0
    return ', '.join(map(str, list_summ))


print('Сумма всех положительных элементов матрицы: ', summ_positive_matrix(matrix),
      '\nСумма положительных элементов в каждом столбце: ' + summ_positive_columns(matrix))


# todo: Задание 2
N = int(input('Введите число элементов списка: '))
list_ = list(random.randint(-25, 25) for n in range(N))
print(list_)


def quentity_negative(list):
    quentity = 0
    for number in list:
        if number < 0:
            quentity += 1
    return quentity


def quentity_zero(list):
    quentity = 0
    for number in list:
        if number == 0:
            quentity += 1
    return quentity


def summ_positive_list(list):
    summ = 0
    for number in list:
        if number > 0:
            summ += number
    return summ


print('Количество отрицательных чисел:', quentity_negative(list_),
      '\nКоличество чисел равных нулю:', quentity_zero(list_),
      '\nСумма всех положительных чисел:', summ_positive_list(list_))