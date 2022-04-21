#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.


def secret_word(wor):
    for i in range (len(words[wor])):
        words_secret.append('▒ ')
    return words_secret
def word_list(word_):
    for i in words[word_]:
        word.append(i)
    return word
def algoritm(e):
    for i in range(word.count(e)):
        words_secret[word.index(e)] = e + ' '
        word.insert((word.index(e)), '0')
        word.remove(e)

import random
words = ["оператор", "конструкция", "объект"]
desc_  = ["Это слово обозначает наименьшую автономную часть языка программирования",
          "Это слово обозначает какое-либо строение, устройство в языке программирования",
          "Это слово обозначает абстракцию для данных"]
attempt = 10
while len(words) !=0:
    Random = random.randint(0, len(words) - 1)
    words_secret = []
    # использование функции
    secret_word(Random)
    print(desc_[Random], '\n',
        ''.join(words_secret))
    word = []
    # использование функции
    word_list(Random)
    if attempt == 0:
        print('Вы проиграли!')
        break
    while True:
        user_letter = input('Ваша буква: ')
        if user_letter in word:
            # использование функции
            algoritm(user_letter)
            print(''.join(words_secret))
        else:
            attempt -= 1
            print('Такой буквы нет!', '\n' +
                  'Осталось попыток: ', attempt)
        if '▒ ' not in words_secret:
            print('Вы выиграли!\n\n\n')
            words.remove(words[Random])
            desc_.remove(desc_[Random])
            attempt = 10
            break
print('Вы выиграли главный приз!', '\n' +
      '!!АВТОМОБИЛЬ!!')