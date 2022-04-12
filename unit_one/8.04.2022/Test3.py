# Данные две переменные:
age = 36.6
temperature = 25
# Обмениваем значения переменных заводя дополнительные переменные
x = age
age = temperature
temperature = x
print("age - ", age, '\n',
      "temperature - ", temperature)
