#todo: Задан файл dictionary.xml (в текущей папке).

# <dict>
#     <key>###</key>
#     <value>##</value>
# </dict>

# Написать функцию которая принимает кортеж вида  ('age', 16) и записывает его значения в файл
# Первое значение кортежа в позицию <key> второе в <value>
# Итоговый файл должен получиться:
# <dict>
# <key>'age'</key>
# <value>16</value>
# </dict>

# Задачу решить с помощью метода seek()

tuple_ = ('age', 16)
dictionary = open('dictionary.xml', 'r+')
dictionary_str = ''
for i in dictionary.readlines():
    dictionary_str += i
print(dictionary_str)
dictionary.close()





