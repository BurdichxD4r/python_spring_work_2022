#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
# и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

# Пример вывода:
# Сумма 2   комбинация [(1,1)]
# Сумма 3   комбинация [(1,2),(2,1)]
# Сумма 4   комбинация [(1,3),(3,1),(2,2)]
# ........................................
# Выводы комбинаций оформить в список кортежей.


Sum_list = list(int(i) for i in (input('Введите необходимые суммы (через пробел): ').split()))
combo_list = []
def combo_side(Sum_input):
    for side_second in range(1, 7):
        for side_first in range(1, 7):
            combo = side_first + side_second
            if combo == Sum_input:
                combo_typle = (side_first, side_second)
                combo_list.append(combo_typle)
    return combo_list
for Sum in Sum_list:
    combo_side(Sum)
    print('Сумма', Sum, '   комбинация', combo_list)
    combo_list.clear()