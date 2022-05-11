#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


string_code = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
string = ''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
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
print(cezar(string_code))