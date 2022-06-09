#try:
#    x = 1
#    y = 0
#    a = x / y
#except ZeroDivisionError:
#    print('Возникло исключение: ошибка деления на ноль! ')
#else:
#    print('Выводится если нет ошибки')
#finally:
#    y = 0.000001
#    a = x / y
#    print(a, 'Аккуратно обрабатываем ошибку и идём дальше')
#import  numpy as np
#def divide(x, y):
#    try:
#        out = x / y
#    except:
#        try:
#            out = np.inf * x / abs(x)
#        except:
#            out = np.nan
#    finally:
#        return out
#print(divide(1, 0))
#
#class NameTooShortError(ValueError):
#    pass
#def validate(name):
#    if len(name) < 10:
#        raise NameTooShortError
#try:
#    name = input('Введите имя: ')
#    validate(name)
#    print(name)
#except NameTooShortError:
#    print('Имя слишком короткое!')
#
#class NegValException(Exception):
#    def __init__(self, number):
#        super().__init__(f'Neg val:  {number}')
#        self.number = number
#try:
#    val = int(input('input positive number: '))
#    if val < 0:
#        raise NegValException(val)
#except NegValException as e:
#    print(e)


# classwork
#class View:
#    def render(self):
#        pass
#class ListView(View):
#    def rander(self, data):
#        #логика вывода данных пользователю в консоль
#        pass
#class QuestionView(View):
#    def rander(self, data):
#        tamplate = '' #логика вывода
#        print(tamplate)
#
#class TestSystem:
#    pass
#MVC реализация всех этажей
#M - DB; Profile; Test
#V - Auth; TestSystem
#C - ListView; QuestionView; View

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
psycopg2.connect()
class DB(user_name, password, name, host, port):
    def __init__(self):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.host = host
        self.port = port
    def get_connect(self):
        try:
            conn = psycopg2.connect(user=user_name, password=password, host=host, port=port)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            sql_create_database = 'create database postgres_db'
            cursor.execute(sql_create_database)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
db = DB('burdich', '6223', 'testsystem', "127.0.0.1", "5432")
