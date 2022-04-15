#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

# Пример:
# mass = [1,2,17,16,30,51,2,70,3,2]

# Для числа 2 индексы двух ближайших чисел: 6 и 9

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 индексы двух ближайших чисел: 0 и 7
# Для числа 2 индексы двух ближайших чисел: 6 и 9

Mass = [int(i) for i in input().split()]
Mass_index = []
Mass_end = []
user_namber = int(input('Введите число из списка: '))
if user_namber in Mass:
    for i in range (Mass.count(user_namber)):
        Mass_index.append(Mass.index(user_namber))
        Mass.insert(Mass.index(user_namber), False)
        Mass.remove(user_namber)
    if len(Mass_index) > 1:
        for i  in range (len(Mass_index) - 1):
            Mass_end.append(Mass_index[i + 1] - Mass_index[i])
        print('Для числа', user_namber, 'индексы двух ближайших чисел:',
              Mass_index[Mass_end.index(min(Mass_end))], 'и',
              Mass_index[Mass_end.index(min(Mass_end)) + 1])
    else:
        print('Число', user_namber, 'в списке уникально и имеет индекс:', Mass_index[0])
else:
    print('Такого числа нет!')

