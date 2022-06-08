# todo: Написать авторизацию пользователя в систему.
# Приложение в начале должно предлагать меню
# 1. Вход
# 2. Регистрация
#
#
# 1. При выборе пункта "Вход" пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
# При вводе данных авторизации, система проверяет есть ли данный
# пользователь в БД (логин) если нет то предлагает зарегистрироваться.
# Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
# приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
# выбора билетов для тестирования(пока заглушка).
#
# 2. При выборе "Регистрация" пользователю необходимо ввести новый
# логин, пароль, фио, почту, телефон, группу. После система заводит
# запись в БД если пользователя под данным логином нет. Если такой пользователь
# уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
# в виде хеша + соль.
#
# По хешированию прочитать статью
# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
# для хеширования пароля воспользоваться библиотекой bcrypt

from psycopg2 import *
from bcrypt import *


class DB:

    CONNECTION = None
    __instance = None
    __user = "burdich"
    __password = "6223"
    _db_name = "TestSystem"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DB.__instance = None

    def __init__(self, db_name, connection=None):
        self.db_name = db_name

    @classmethod
    def login(cls):
        connection = connect(
            user=cls.__user,
            password=cls.__password,
            database=cls._db_name
        )
        print('1. Войти\n2. Зарегистрироваться')
        number = int(input())
        if number == 1:
            print('Вход!')
            login = str(input('Введите логин:\n'))
            password = str(input('Введите пароль:\n'))
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT login, hesh_psw FROM profile;'
                )
                list_logins = cursor.fetchall()
                for _login in list_logins:
                    if login in _login[0:]:
                        if password == checkpw(password.encode(), _login[1]):
                            print('Вы вошли!')
                            cls.__user = login
                            cls.__password = password
                        else:
                            print('Неверный пароль!')
                    else:
                        print('Неверный логин!')
        elif number == 2:
            print('Регистрация!')


    def getConnecting(self):
        print(f'Соединение с БД: {self._db_name}')
        try:
            connection = connect(
                user=self.user,
                password=self.password,
                database=self._db_name
            )
            DB.CONNECTION = connection
            print(f'Подключение к {self._db_name} прошло успешно!')
        except Exception as _ex:
            print("[INFO][ERROR]", _ex)

#print(hashpw('123'.encode(), gensalt()))
#hash = hashpw('123'.encode(), gensalt())
#valid = checkpw('12'.encode(), hash)
#print(valid)
db = DB(DB._db_name)
db.login()


