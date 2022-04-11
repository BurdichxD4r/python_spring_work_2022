# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

# todo: 6 Бурдейный Николай
# A * x + B = 0
# A * x = -B
# x = -B / A
print('Решение линейного уравнения "A·x+B=0": ')
namber_A = float(input('Введите коэффициент A: '))
while namber_A == 0:
    namber_A = float(input('Введите коэффициент A не равный 0: '))
namber_B = float(input('Введите коэффициент B: '))
if namber_B == 0:
    print('x=0')
elif ((namber_A * 10) % 10 == 0) and ((namber_B * 10) % 10 == 0):
    namber_A = int(namber_A)
    namber_B = int(namber_B)
    print('x=' + str(-namber_B / namber_A))
else:
    print('x=' + str(-namber_B / namber_A))
