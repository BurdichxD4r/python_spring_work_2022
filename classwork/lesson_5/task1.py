# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр, который будет выводить отсортированные объекты по возрасту(больше введенного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Введите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

type_sorted = int(input('Введите тип сортировки: '))
if type_sorted == 1:
    age_sorted_mass = []
    user_sorted_mass = []
    for dict in users:
        age_sorted_mass.append(dict.get('age'))
        age_sorted_mass.sort()
    x = 0
    while len(users) != len(user_sorted_mass):
        for dict in users:
            if dict.get('age') == age_sorted_mass[x]:
                user_sorted_mass.append(dict)
        x += 1
    print(user_sorted_mass)
elif type_sorted == 2:
    age_sorted_mass = []
    user_sorted_mass = []
    for dict in users:
        age_sorted_mass.append(dict.get('login'))
        age_sorted_mass.sort()
    x = 0
    while len(users) != len(user_sorted_mass):
        for dict in users:
            if dict.get('login') == age_sorted_mass[x]:
                user_sorted_mass.append(dict)
        x += 1
    print(user_sorted_mass)
else:
    age_sorted_mass = []
    user_sorted_mass = []
    for dict in users:
        age_sorted_mass.append(dict.get('group'))
        age_sorted_mass.sort()
    x = 0
    while len(users) != len(user_sorted_mass):
        for dict in users:
            if dict.get('group') == age_sorted_mass[x]:
                user_sorted_mass.append(dict)
        x += 1
    print(user_sorted_mass)
