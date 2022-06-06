# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg


# Ссылка на документацию
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Для подключения использовать пользователя и базу отличную от postgres

from psycopg2 import *

def create_table_postgreSQL(name_table, columns):
    connection = None
    if type(name_table) == str:
        if type(columns) == str:
            try:
                print('Соединение с базой данных!')
                connection = connect(database='TestSystem', user='burdich', password='6223')
                with connection.cursor() as cursor:
                    cursor.execute(
                        'CREATE TABLE "' + name_table + '"(' + columns + ');'
                    )
                connection.commit()
                print(f'Создание таблицы {name_table} прошло успешно!')
            except Exception as _ex:
                print(f'!ERROR! {_ex} Проверте правильность ввода названия и атрибутов таблицы\nИли быть может таюлица'
                      f'уже существует, проверь PostgreSQL')
            finally:
                print('Отключение от базы данных!')
                if connection != None:
                    connection.close()
                    print('Отключение прошло успешно!')
        else:
            raise ValueError('Неправильный формат колонок таблицы!')
    else:
        raise ValueError('Неправильный формат названия таблицы!')

create_table_postgreSQL(input('Введите название таблицы: \nПример:    CLASS\n'),
                        input('Введите код создания атрибутов таблицы (PosgreSQL): \nПример:    '
                              '"id_CLASS" SERIAL PRIMARY KEY, "TIME" BIGINT, "STATUS" BOOLEAN UNIQUE\n'))
