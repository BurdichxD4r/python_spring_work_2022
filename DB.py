import psycopg2
from bcrypt import *
user = "burdich"
password = "6223"
db_name = "TestSystem"

class DB:

    CONNECTION = None
    __instance = None

    def __call__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DB.__instance = None

    def __init__(self, user, password, db_name, connection=None):
        self.user = user
        self.password = password
        self.db_name = db_name


    def getConnecting(self):
        print(f'Соединение с БД: {self.db_name}')
        try:
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            DB.CONNECTION = connection
            print(f'Подключение к {self.db_name} прошло успешно!')
        except Exception as _ex:
            print("[INFO][ERROR] Пользователя не существует", _ex)

    def select(self):
        with self.CONNECTION.cursor() as cursor:
            cursor.execute(
                'SELECT login, hesh_psw FROM profile;'
            )
            print(f"Server version: {cursor.fetchall()}")

    def getCloseConnecting(self):
        print(f'Закрытие соединения с БД: {self.db_name}')
        DB.CONNECTION.close()
        print("[INFO] PostgreSQL connection closed")



class Profile():

    def __init__(self, login, password, name=None, surname=None, age=None, tel=None, email=None):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.age = age
        self.tel = tel
        self.email = email

    def set_profile(self, conn):
        with DB.CONNECTION.cursor() as cursor:
            cursor.execute(
                f'CREATE USER "{self.login}" WITH PASSWORD \'{self.password}\''
            )
    def get_profile(self, conn):
        return self.login, self.password


    profile = property(get_profile, set_profile)

base = DB(user, password, db_name)
base.getConnecting()
base.select()
base.getCloseConnecting()
