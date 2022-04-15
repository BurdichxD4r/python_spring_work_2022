#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

# Пример:
# mass = [1,2,17,16,30,51,2,70,3,2]

# Для числа 2 индексы двух ближайших чисел: 6 и 9

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 индексы двух ближайших чисел: 0 и 7
# Для числа 2 индексы двух ближайших чисел: 6 и 9

Mass = [1,2,17,54,30,89,2,1,6,2]
Mass_clone = Mass[:]
Mass_end = []
M = []
namber = int(input('Введите число: '))
x = 0
for i in range (Mass.count(namber)):
    Mass_end.append(Mass_clone.index(namber) + x)
    Mass_clone.remove(namber)
    x += 1
print(Mass_end)
