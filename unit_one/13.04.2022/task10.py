# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

namber = input('Введите четырехзначное число: ')
if namber[0] == namber[3] and namber[1] == namber[2]:
    print(True)
else:
    print(False)