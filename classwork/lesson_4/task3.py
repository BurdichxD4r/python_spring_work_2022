#todo: Написать игру , где программа загадывает число от 0 до 100 (через функцию random) , а пользователь
#пытается его отгадать(через консоль). При успехе выводится поздравление в победе и результат попыток.
#По истечении 10 неудачных попыток выводится проигрышь.

#Для получения функции числа из диапазона от 0 до 100 подключать библиотеку
#import random
#random.randint(0,100)

import random
guess = random.randint(0, 100)
attempt = 0
while True:
    user_namber = int(input('Угадай число: '))
    if user_namber == guess:
        print('Поздравляю Вы победили!', '\n'
              'Всего попыток: ', attempt)
        break
    else:
        attempt += 1
        if user_namber > guess:
            print('Неправильно, твоё число больше, попробуй ещё раз!')
        else:
            print('Неправильно, твоё число меньше, попробуй ещё раз!')