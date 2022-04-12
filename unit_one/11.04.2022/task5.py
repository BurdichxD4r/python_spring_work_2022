# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

# todo: 5 Бурдейный Николай
point_A = float(input('Введите координату точки A: '))
point_B = float(input('Введите координату точки B: '))
point_C = float(input('Введите координату точки C: '))
length_AC = point_A - point_C
length_BC = point_B - point_C
if length_AC < 0:
    length_AC = length_AC * -1
if length_BC < 0:
    length_BC = length_BC * -1
if ((length_AC * 10) % 10 == 0) and ((length_BC * 10) % 10 == 0):
    length_AC = int(length_AC)
    length_BC = int(length_BC)
print('Длила отрезка AC: ', length_AC, '\n'
      'Длина отрезка BC: ', length_BC, '\n'
      'Сумма длин отрезков AC и BC: ', length_AC + length_BC)

