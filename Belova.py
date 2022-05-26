#todo: Модуль random
# Модуль random предоставляет функции для генерации случайных чисел, букв, случайного выбора элементов
# последовательности.

from random import *

print('\n')
#random.seed([X], version=2) - инициализация генератора случайных чисел. Если X не указан, используется системное время.
# Возможность формировать одиннаковые случайные последовательности чисел при каждом новом запуске программы.
run = 0
def seed_(number):
    global run
    global number_
    run = 1
    number_ = str(number)
    return seed(number)
#seed_(89)
print('random.seed \nубрать "#" у 17-ой строчки кода, чтобы присвоить seed' + '\n' if run == 0
      else 'random.seed(' + number_ + ')' + '\n')

#random.getstate() - внутреннее состояние генератора.
print('random.getstate')
print('Внутреннее состояние генератора:    ', getstate(), '\n')

#random.setstate(state) - восстанавливает внутреннее состояние генератора. Параметр state должен быть получен функцией
# getstate().
print('random.setstate')
state = getstate()
print('Восстанавливает внутреннее состояние генератора:    ', setstate(state), '\n')

#random.getrandbits(N) - возвращает число, которое представляет собой случайные биты.
print('random.getrandbits')
N = randint(1, 11)
print('Возвращает число, которое представляет собой случайные биты:    ', getrandbits(N), '\n\t' + 'N =', N, '\n')

#random.randrange(start, stop, step) - возвращает случайно выбранное число из последовательности.
print('random.randrange')
start = -5
stop = 5
step = 2
print('Случайно выбранное число из последовательности:    ', randrange(start, stop, step), '\n\t' + 'start =', start,
      '; stop =', stop, '; step =', step, '\n')

#random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
print('random.randint')
A = 0
B = 10
print('Случайное целое число N, A ≤ N ≤ B:    ', randint(A, B), '\n\t' + 'A =', A, '; B =', B, '\n')

#random.choice(sequence) - случайный элемент непустой последовательности.
print('random.choice')
list_ = list(randint(0, 10) for i in range(10))
print('Случайный элемент непустой последовательности:    ', choice(list_), '\n\t' + 'list_ =', list_, '\n')

#random.shuffle(sequence, [rand]) - перемешивает последовательность (изменяется сама последовательность).
# Поэтому функция не работает для неизменяемых объектов.
print('random.shuffle')
list_ = list(i for i in range(10))
list_original = list_.copy()
shuffle(list_)
print('Перемешанный список:    ', list_, '\n\t' + 'list_ =', list_original, '\n')

#random.sample(population, k) - список длиной k из последовательности population.
# k <= len(population)
print('random.sample')
population = list(i for i in range(10))
k = 5
print('Список длиной k из последовательности population:    ', sample(population, k), '\n\t' +
      'population =', population, '; k =', k, '\n')

#random.random() - случайное число от 0 до 1.
print('random.random')
print('Случайное число от 0 до 1:    ', random(), '\n')

#random.uniform(A, B) - случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A).
print('random.uniform')
A = 0
B = 10
print('Случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A):    ', uniform(A, B), '\n\t' + 'A =', A, '; B =', B,
      '\n')

#random.triangular(low, high, mode) - Возвращает случайное вещественное число в промежутке между двумя заданными
# параметрами, low ≤ N ≤ high. Mode - распределение (уточнения середины между указанными параметрами).
print('random.triangular')
low = 0
high = 10
mode = 7
print('Возвращает случайное вещественное число в промежутке между двумя заданными параметрами:    ',
      triangular(low, high, mode), '\n\t' + 'low =', low, '; high =', high, '; mode =', mode, '\n')

#random.betavariate(alpha, beta) - Возвращает случайное вещественное число в промежутке между 0 и 1, основываясь на
# Бета-распределении, которое используется в статистике. alpha>0, beta>0. Возвращает от 0 до 1.
print('random.betavariate')
nums = list()
alpha = 5
beta = 10
for i in range(10):
    temp = betavariate(alpha, beta)
    nums.append(temp)
print('Случайные вещественные числа, основанные на Бета-распределении:    ', nums, '\n\t' + 'alpha =', alpha,
      '; beta =', beta, '\n')

#random.expovariate(lambd) - Возвращает случайное вещественное число в промежутке между 0 и 1, или же между 0 и -1,
# когда параметр отрицательный. За основу берется Экспоненциальное распределение.
print('random.expovariate')
lambd = 4
print('Случайное вещественное число основанное на Экспоненциальном распределении:    ', expovariate(lambd),
      '\n\t' + 'lambd =', lambd, '\n')

#random.gammavariate(alpha, beta) - Возвращает случайное вещественное число, основываясь на Гамма-распределении.
# Условия на параметры alpha>0 и beta>0.
print('random.gammavariate')
alpha = 8
beta = 2.2
print('Случайное вещественное число основанное на Гамма-распределении:    ', gammavariate(alpha, beta),
      '\n\t' + 'alpha =', alpha, '; beta =', beta, '\n')

#random.gauss(mu, sigma) - случайное значение по Гауссовскому закону (формальный диапазон не
# ограничен).
# mu - математическое ожидаение (среднее значение СВ)
# sigma - среднеквадратическое отклонение
print('random.gauss')
mu = 3.5
sigma = 7.3
print('Случайное значение по Гауссовскому закону:    ', gauss(mu, sigma), '\n\t' + 'mu =', mu, '; sigma =', sigma, '\n')

#random.lognormvariate(mu, sigma) - Возвращает случайное вещественное число, основываясь на Логнормальном распределении
# (логарифм нормального распределения). Если взять натуральный логарифм этого распределения, то вы получите нормальное
# распределение со средним mu и стандартным отклонением sigma. mu может иметь любое значение, и sigma должна быть
# больше нуля.
print('random.lognormvariate')
mu = -1.45
sigma = 4
print('Случайное вещественное число основанное на Логнормальном распределении:    ', lognormvariate(mu, sigma),
      '\n\t' + 'mu =', mu, '; sigma =', sigma, '\n')

#random.normalvariate(mu, sigma) - Возвращает случайное вещественное число, основываясь на Нормальном распределении
# (нормальное распределение). mu - среднее значение, sigma - стандартное отклонение.
print('random.normalvariate')
mu = 4
sigma = 2
print('Случайное вещественное число основанное на Нормальном распределении:    ', normalvariate(mu, sigma),
      '\n\t' + 'mu =', mu, '; sigma =', sigma, '\n')

#random.vonmisesvariate(mu, kappa) - Возвращает случайное вещественное число, основываясь на распределении фон Мизеса.
# mu - средний угол, выраженный в радианах от 0 до 2π, и kappa - параметр концентрации, который должен быть больше или
# равен нулю. Если каппа равна нулю, это распределение сводится к случайному углу в диапазоне от 0 до 2π.
print('random.vonmisesvariate')
mu = 0.4
kappa = 0.8
print('Случайное вещественное число основанное на распределении фон Мизеса:    ', vonmisesvariate(mu, kappa),
      '\n\t' + 'mu =', mu, '; kappa =', kappa, '\n')

#random.paretovariate(alpha) - Возвращает случайное вещественное число, основываясь на распределении Парето.
print('random.paretovariate')
alpha = 4
print('Случайное вещественное число основанное на распределении Парето:    ', paretovariate(alpha),
      '\n\t' + 'alpha =', alpha, '\n')

#random.weibullvariate(alpha, beta) - Возвращает случайное вещественное число, основываясь на распределении Вейбулла.
print('random.weibullvariate')
alpha = 5
beta = 2
print('Случайное вещественное число основанное на распределении Вейбулла:    ', weibullvariate(alpha, beta),
      '\n\t' + 'alpha =', alpha, '; beta =', beta, '\n')