#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

hello = list(input('Введите Input 1: ').split())
hello_word = list(input('Введите Input 2: ').split())
code_letter = {
    '8' : 'h',
    '5' : 'e',
    '12' : 'l',
    '15' : 'o',
    ',' : ',',
    '0' : ' ',
    '23' : 'w',
    '18' : 'r',
    '4' : 'd',
    '!' : '!'
               }
hello_str = ''
hello_word_str = ''
for key in hello:
    hello_str = hello_str + code_letter.get(key)
print(hello_str)
for key in hello_word:
    hello_word_str = hello_word_str + code_letter.get(key)
print(hello_word_str)