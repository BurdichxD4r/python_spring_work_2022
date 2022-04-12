# todo: Задана поизвольная строка. Необходимо разбить ее на две части.
# Задачу решить с помощью срезов.
#
# Пример:
# str = "Hello world!"
# Ответ: Первая часть  "Hello"
# 		Вторая часть "world!"

Str = input('Введите произвольную строку: ')
if ' ' in Str:
    print(Str[:Str.find(' ')])
    print(Str[Str.find(' '):])
else:
    print(Str[:(len(Str) // 2)])
    print(Str[len(Str) // 2:])