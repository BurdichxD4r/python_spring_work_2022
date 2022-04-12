# Преобразовать переменные age и foo в число
age = "23"
foo = '23abc'
age = int(age)
foo = int(foo)
print ( age,foo)

# Преобразовать переменную age в Boolean
age = 123abc
age = bool(age)
print(age)

# Преобразовать переменную flag в Boolean
flag = 1
flag = bool(flag)
print(flag)

# Преобразовать значение в Boolean
str_one = 'Privet'
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print(str_one, str_two)

# Преобразовать 0 и 1 в Boolean
x = 1
y = 0
x = bool(x)
y = bool(y)
print(x, y)

# Преобразовать False в строку
False_=False
False_=str(False_)
print(False_)

exit(20)