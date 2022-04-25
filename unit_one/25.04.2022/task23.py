#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


string_code = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
string = "grznuamnzngzcgesgetuzhkuhbouaygzloxyzatrkyyeuaxkjazin"
alphabet = []
while string != '':
    alphabet.append(string[0])
    string = string.replace(string[0], '')
print(alphabet)
for letter in alphabet:
    string_code_ready = string_code.replace(letter, alphabet[alphabet.index(letter) - 1])
print(string_code_ready)