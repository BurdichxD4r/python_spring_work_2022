list_for = []
for i in range(10):
    list_for.append(i ** 3)
print(list_for)

list_map = list(map(lambda x: x ** 3, range(10)))
print(list_map)

list_comprehension_1 =[x ** 3 for x in range(10)]
print(list_comprehension_1)

list_comprehension_2 = [x ** 2 for x in range(50) if x % 3 == 0]
print(list_comprehension_2)

list_comprehension_3 = [x ** 2 if True else y ** 2 for x in range(10) for y in range(10) if x % 3 == 0 and y % 3 == 0]
print(list_comprehension_3)

# _  -  последнее выданное значение
list_matrix_comprehension = [[i for i in range(3)] for _ in range(4)]
print(list_matrix_comprehension)

flat = [col for row in list_matrix_comprehension for col in row]
print(flat)

# Генерация таблицы умножения
T = [[x * y for x in range(1, 6)] for y in range(1, 6)]
for i in T:
    print(i)

# Генератор словаря
D = {num: num ** 2 for num in range(1,10)}
print(D)

items = [('c', 3), ('x', 4)]
filtered = {key for key in items}
print(filtered)
print(type(filtered))

items = [('c', 3), ('x', 4), ('z', 1)]
filtered = {key: value for (key, value) in items}
print(filtered)
print(type(filtered))
filtered = {key: value for (key, value) in filtered.items() if value > 2}
print(filtered)
print(type(filtered))

# Использование enumerate функции
names = ['Harry', 'Ron', 'Jimy', 'Luna']
index = {k: v for (k, v) in enumerate(names)}
print(index)