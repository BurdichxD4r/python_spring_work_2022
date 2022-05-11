#todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

# Input             	            Output
# apple	                            aple
# 25.04.2022 Good morning !!	    godmrni


string_1 = 'apple'
string_2 = '25.04.2022 Good morning !!'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
def code(text):
    text = text.lower()
    new_text = ''
    for i in range(len(text)):
        if text[i] in alphabet:
            if text[i] not in new_text:
                new_text += text[i]
    return new_text
print(code(string_1))
print(code(string_2))