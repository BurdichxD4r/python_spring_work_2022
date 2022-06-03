import psycopg2
locale_host = "127.0.0.1"
user = "burdich"
password = "6223"
db_name = "testsystem"

class DB:
    __instance = None
    def __call__(self, *args, **kwargs):
        pass
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __del__(self):
        DB.__instance = None
    def __init__(self, locale_host, user, password, db_name, connection=None):
        self.locale_host = locale_host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.connection = connection
    def getConnecting(self):
        print(f'Соединение с БД: {self.db_name}')
        try:
            connection = psycopg2.connect(
                host=self.locale_host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            self.connection = connection
            print(f'Подключение к {self.db_name} прошло успешно!')
            print(self.connection)
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
    def SELECT(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(f"Server version: {cursor.fetchone()}")
    def getCloseConnecting(self):
        print(f'Закрытие соединения с БД: {self.db_name}')
        self.connection.close()
        print("[INFO] PostgreSQL connection closed")

db = DB(locale_host, user, password, db_name)
db.getConnecting()
db.SELECT()
db.getCloseConnecting()