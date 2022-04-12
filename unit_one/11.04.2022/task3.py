##todo: Самостоятельная работа

# Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения с остатком.

##todo: 3 Бурдейнйы Николай

user_namber_1 = float(input('Введите первое число: '))
user_namber_2 = float(input('Введите второе число: '))
if ((user_namber_1 * 10) % 10 == 0) and ((user_namber_2 * 10) % 10 == 0):
      user_namber_1 = int(user_namber_1)
      user_namber_2 = int(user_namber_2)
print('Сумма введённых чисел: ', user_namber_1 + user_namber_2, '\n'
      'Разность введённых чисел: ', user_namber_1 - user_namber_2, '\n'
      'Частное введённых чисел: ', user_namber_1 / user_namber_2, '\n'
      'Произведение введённых чисел: ', user_namber_1 * user_namber_2, '\n'
      'Целочисленное деление введённых чисел: ', user_namber_1 // user_namber_2, '\n'
      'Остаток от деления введённых чисел: ', user_namber_1 % user_namber_2, '\n'
      'Возведение в степень введёных чисел: ', user_namber_1 ** user_namber_2)
