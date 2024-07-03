import psycopg2
from src.settings import settings
from src.connection.postgres import with_connection

connection = None
try:
    connection = psycopg2.connect(
        dbname=settings.DB,
        user=settings.USER,
        password=settings.PASSWORD,
        host=settings.HOST,
        port=settings.PORT)

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from de_test_schema.users;"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchall")
    publisher_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in publisher_records:
        print("user_id = ", row[0],  end=' ')
        print("gender = ", row[1], end=' ')
        print("name = ", row[2] + row[3], end=' ')
        print("age = ", row[4])
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
    print("PostgreSQL connection is cloooosed")


@with_connection
def r(cursor):
    """
    Test function that uses our psycopg2 decorator
    """
    cursor.execute('select * from de_test_schema.users;')
    return cursor.fetchall()
#
#
print(r())