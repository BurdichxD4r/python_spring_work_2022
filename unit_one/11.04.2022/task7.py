# todo: 7.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 7.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.

# todo: 7.1 Бурдейный Николай
namber_A = int(input('Введите целое число A: '))
print('Число A является четным: ', end='')
if namber_A % 2 ==0:
    print('True')
else:
    print('False')

# todo: 7.2 Бурдейный Николай
namber_A = int(input('Введите целое число A: '))
print('Число A является нечетным: ', end='')
if namber_A % 2 != 0:
    print('True')
else:
    print('False')