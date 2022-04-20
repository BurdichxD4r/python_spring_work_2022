# :todo Написать функцию is_ascending(list_) проверки на монотонность?
# Функция принимает список и определяет  является ли он монотонно возрастающим
# (то есть проверяет верно ли, что каждый элемент этого списка больше предыдущего).
# В качестве результата возвращайте  YES, если массив монотонно возрастает и NO в противном случае.

# Пример:
# mass = [ 2, 5, 7]

# def is_ascending(list_):
#     ваша реализация


# result = is_ascending(mass)
# print(result)
# YES

mass = [int(i) for i in input('Введите все значения списка в одну строку: ').split()]
attempt = 0
def is_ascendign(list_):
    global attempt
    bool_ = None
    for i in list_[1:]:
        if i > list_[attempt]:
            attempt += 1
            bool_ = 'YES'
            if attempt == len(list_):
                bool_ = 'YES'
                attempt = 0
                break
            continue
        else:
            bool_ = 'NO'
            attempt = 0
            break
    return bool_
result = is_ascendign(mass)
print('Является ли список монотонно возрастающим:', result)