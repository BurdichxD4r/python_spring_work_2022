# todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
# .
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
# .
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import random
from Pickle_json_yaml.serializer import to_json
from Pickle_json_yaml.deserializer import from_json
guess = random.randint(0, 100)
attempt = 0
save_file = 'Save_random_0_100_2.json'
def save_menu(save_file):
    global guess
    global attempt
    print('1. Новая игра\n2. Восстановить игру')
    answer = str(input())
    if answer == '1':
        pass
    elif answer == '2':
        save_list = from_json(save_file)
        guess = int(save_list[0])
        attempt = int(save_list[1])
    else:
        save_menu(save_file)
save_menu(save_file)
while True:
    print('Для сохранения игры напечатай (S)')
    user_number = input('Угадай число: ')
    if user_number == 'S':
        print('1. Продолжить игру\n2. Сохранить игру')
        user_number_save_menu = input()
        save_parameters = [str(guess), str(attempt)]
        to_json(save_file, save_parameters)
    else:
        user_number = int(user_number)
        if user_number == guess:
            print('Поздравляю Вы победили!', '\n'
                  'Всего попыток: ', attempt)
            break
        else:
            attempt += 1
            if user_number > guess:
                print('Неправильно, твоё число больше, попробуй ещё раз!')
            else:
                print('Неправильно, твоё число меньше, попробуй ещё раз!')