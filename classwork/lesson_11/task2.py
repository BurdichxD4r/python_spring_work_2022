#todo: Для каждого значения из списка mass получите
# список проверок(True или False) вхождений значений в диапазон от 1 до 100
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]

print(list(map(lambda i: 0 <= i <=100, mass)))

#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений

list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]

print(list(filter(lambda i: i % 2 == 1, list_)))