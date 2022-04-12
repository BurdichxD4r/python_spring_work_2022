# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

namber_X = int(input('Введите переменную X: '))
namber_Y = int(input('Введите переменную Y: '))
namber_Z = int(input('Введите переменную Z: '))
if namber_X > namber_Y and namber_X > namber_Z:
    print('Наибольшее число ', namber_X)
elif namber_Y > namber_X and namber_Y > namber_Z:
    print('Наибольшее число ', namber_Y)
else:
    print('Наибольшее число ', namber_Z)