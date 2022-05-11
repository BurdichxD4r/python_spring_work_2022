# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#  В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


message = open('message.txt', 'rt', encoding='UTF-8')
message_txt = ''.join(message.readlines())
message_txt = message_txt.lower()
message.close()
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
message_cezar = open('message_cezar.txt', 'wt')
def cezar(user_string):
    string = ''
    for i in range(len(user_string)):
        string += '*'
    for i in range(len(user_string)):
        if user_string[i] in alphabet:
            string = string.replace('*', alphabet[alphabet.index(user_string[i]) - 6], 1)
        else:
            string = string.replace('*', user_string[i], 1)
    return string
message_cezar.writelines(cezar(message_txt))
print(cezar(message_txt))
message_cezar.close()