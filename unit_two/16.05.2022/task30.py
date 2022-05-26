#todo: Найти сумму элементов матрицы,
#Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:

#>>> matrix = [[1, 2, 3], [4, 5, 6]]
#>>> msum(matrix)
#21

#>>> msum(load_matrix('matrix.txt'))
#423

matrix = [[1, 2, 3], [4, 5, 6]]
def summ(list):
    summ_ = 0
    for i in list:
        summ_ += i
    return summ_

def msum(matrix):
    list_ = [number for numbers in matrix for number in numbers]
    return summ(list_)

print(msum(matrix))