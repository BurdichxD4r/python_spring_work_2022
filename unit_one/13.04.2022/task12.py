#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции match (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4

# Введите массу тела
# >1

# Ответ: 1000 кг

print('''1 - килограмм
2 — миллиграмм
3 — грамм
4 — тонна
5 — центнер''')
Type = input('Введите единицу измерения (соответствующую ей цифру): ')
Weight = float(input('Введите массу (без единицы измерения): '))
match Type:
    case '1':
        print('В киллограмах: ', Weight)
    case '2':
        print('В киллограмах: ', Weight / (10 ** 6))
    case '3':
        print('В киллограмах: ', Weight / (10 ** 3))
    case '4':
        print('В киллограмах: ', Weight * (10 ** 3))
    case '5':
        print('В киллограмах: ', Weight * (10 ** 2))