#todo: Реализуйте функцию которая возвращает копию списка
def identity(nums):
    return [x for x in nums]
print(identity([1, 2, 3, 4, 5]))

#Пример вызова:
#>>> identity([1, 2, 3, 4, 5])
#[1, 2, 3, 4, 5]
#>>> identity([])
#[]

#todo: Реализуйте функцию которая возвращает степень числа каждого элемента
def power_(nums, pow):
    return [i * pow for i in nums]
print(power_([1, 2, 3, 4, 5],2))

#Пример вызова:
#>> > power_([1, 2, 3, 4, 5],2)
#[2, 4, 6, 8, 10]
#>> > power_([1, 2, 3, 4, 5],3)
#[0, 3, 6, 9, 12, 15]



#todo: Реализуйте функцию которая возвращает только четные значения
def evens(nums):
    return [i for i in nums if i % 2 == 0]
print(evens([1, 2, 3, 4, 5]))

#Пример вызова:
#>>> evens([1, 2, 3, 4, 5])
#[2, 4]
#>>> evens([1, 3, 5])
#[]
#>>> evens([-2, -4, -7])
#[-2, -4]


#todo: Верните список с размерностью слов в том случае если они не исключение
# параметр exception принимает слово которое не нужно подсчитывать
def words_not_the(sentence, exception):
    return [len(i) for i in list(sentence.split()) if i != exception]
print(words_not_the('the quick brown fox jumps over the lazy dog', 'the'))

#Пример вызова:
#>>> words_not_the('the quick brown fox jumps over the lazy dog', 'the' )
#[5, 5, 3, 5, 4, 4, 3]


#todo: Верните список гласных букв
def vowels(word):
    alhabet_vowels = ['e', 'y', 'u', 'i', 'o', 'a', 'j']
    return [x for x in word if x in alhabet_vowels]
print(vowels('mathematics'))

#>>> vowels('mathematics')
#['a', 'e', 'a', 'i']



#todo: Задан массив [ 'one', 'two', 'three' ] с помощью спискового генератора преобразовать в словарь
# вида { 1:'one', 2:'two', 3:'three' }

list_task = ['one', 'two', 'three']
index = {k: v for (k, v) in enumerate(list_task, 1)}
print(index)
