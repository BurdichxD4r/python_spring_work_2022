# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year = input('Введите год: ')
if int(year[-2:]) != 0:
    print(int(year[:len(year) // 2]) + 1)
else:
    print(int(year[:len(year) // 2]))

