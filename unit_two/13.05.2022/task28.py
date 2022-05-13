#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
#Пример:
#render, 10,  12.05.2022 12:00
#show,    5,  12.05.2022 12:02
#render, 15,  12.05.2022 12:07

#Декоратор должен применяться для различных функций с переменным числом аргументов.
#Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import time

next_time = time.strftime('%d.%m.%Y %H:%M')

def decorator(fune):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return fune(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@decorator
def Summ_(x, y):
    return x + y

@decorator
def Diff_(x, y):
    return  x - y

Summ_(5 , 4)
Summ_(6 , 4)
Diff_(6 , 4)

print('Summ_,', str(Summ_.count) + ',', next_time)
print('Diff_,', str(Diff_.count) + ',', next_time)

with open('debug.log', 'a') as debug:
    if Summ_.count > 0 and Diff_.count > 0:
        debug.writelines('Summ_, ' + str(Summ_.count) + ' , ' + str(next_time) + '\n'
                         + 'Diff_, ' + str(Diff_.count) + ' , ' + str(next_time) + '\n')
    elif Summ_.count > 0 and Diff_.count == 0:
        debug.writelines('Summ_, ' + str(Summ_.count) + ' , ' + str(next_time) + '\n')
    elif Summ_.count == 0 and Diff_.count > 0:
        debug.writelines('Diff_, ' + str(Diff_.count) + ' , ' + str(next_time) + '\n')
    else:
        pass
debug.close()