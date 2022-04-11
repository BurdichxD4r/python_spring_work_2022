# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

# todo: 8 Бурдейный Николай
# из условия b = a; c = b; a = c
variable_A = input('Введите переменную A: ')
variable_B = input('Введите переменную B: ')
variable_C = input('Введите переменную C: ')
print('Обмен данными: ')
independent_variable = variable_A
variable_A = variable_C
variable_C = variable_B
variable_B = independent_variable
print('Переменная A: ' + variable_A, '\n'
      'Переменная B: ' + variable_B, '\n'
      'Переменная C: ' + variable_C)