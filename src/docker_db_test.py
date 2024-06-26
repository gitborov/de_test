
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(dbname='postgres',
                                    user="admin",
                                  # пароль, который указали при установке PostgreSQL
                                  password="password",
                                  host="127.0.0.1",
                                  port="5433")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = '''SET search_path TO DE_test_schema;
                            create table test_table (
                            user_id serial primary key,
                            user_name varchar(30)
                            )'''
    cursor.execute(sql_create_database)
    sql_create_scheme = '''CREATE SCHEMA IF NOT EXISTS DE_test_schema'''
    # cursor.execute(sql_create_scheme)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")