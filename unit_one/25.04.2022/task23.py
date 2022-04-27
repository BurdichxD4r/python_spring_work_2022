#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


string_code = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
string = "grznuamnzngzcgesgetuzhkuhbouaygzloxyzatrkyyeuaxkjazin"
alphabet = []
while string != '':
    alphabet.append(string[0])
    string = string.replace(string[0], '')
alphabet = alphabet + alphabet
string = "grznuamnzngzcgesgetuzhkuhbouaygzloxyzatrkyyeuaxkjazin"
string_list = list(string[:])
letter_index = 0
for letter in string_list:
    if letter in alphabet:
        string_list[letter_index] = alphabet[alphabet.index(letter) + 3]
        letter_index += 1
print(string_list)
string_ready = ''
kostil = 0
for index in range(len(string_code)):
    if string_code[index] != ' ' and "'" and  ',':
        string_ready = string_ready + string_list[index + kostil]
    else:
        string_ready = string_ready + string_code[index]
        kostil -= 1
print(string_ready)