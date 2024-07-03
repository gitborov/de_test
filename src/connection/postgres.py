import psycopg2
from src.settings import settings


# connection_temp = psycopg2.connect(dbname='postgres',
#                               user="admin",
#                               # пароль, который указали при установке PostgreSQL
#                               password="password",
#                               host="127.0.0.1",
#                               port="5433")



def with_connection(f):
    def with_connection_(*args, **kwargs):
        connection = None
        try:
            connection = psycopg2.connect(
                dbname=settings.DB,
                user=settings.USER,
                password=settings.PASSWORD,
                host=settings.HOST,
                port=settings.PORT)

            cursor = connection.cursor()
            return_val = f(cursor, *args, **kwargs)
            connection.commit()
            print('Connection is done')
            return return_val

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            # connection.commit()  # or maybe not
            connection.close()
            print('Connection is close')



    return with_connection_


# @with_connection
# def r(cursor):
#     """
#     Test function that uses our psycopg2 decorator
#     """
#     cursor.execute('select * from de_test_schema.users;')
#     return cursor.fetchall()
# #
# #
# print(r())