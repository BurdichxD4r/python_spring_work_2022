#todo: Напишите лямбду функцию которая возвращает максимальное число из 2 переданных
# аргументов

#todo: Напишите лямбду функцию которая возвращает разную степень числа

lambda_test_one = lambda x, y: x if x > y else y
print('Большее из двух чисел:', lambda_test_one(int(input('Введите первое число: ')),
                                                int(input('Введите второе число: '))))

lambda_test_two = lambda x, y: x ** y
print('Результат возведения в степень:',
      lambda_test_two(int(input('Ведите число которое необходимо возвести в степень: ')),
                      int(input('Введите число степени: '))))