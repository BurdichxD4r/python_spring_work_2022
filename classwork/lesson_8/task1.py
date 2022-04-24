#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

dump = open('dump.txt', 'r', encoding='utf-8')
dump_str = ''.join(dump.readlines())
vowels_ru = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
vowels_eu = ['e', 'y', 'u', 'i', 'o', 'a', 'j']
print('Букв из Русского алфавита:')
for letter in vowels_ru:
    if dump_str.count(letter) > 0:
        print('Количество букв', letter, '-', dump_str.count(letter))
print('Букв из Английского алфавита:')
for letter in vowels_eu:
    if dump_str.count(letter) > 0:
        print('Количество букв', letter, '-', dump_str.count(letter))