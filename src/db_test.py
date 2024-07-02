import psycopg2
from src.settings import db

try:
    connection = psycopg2.connect(
        dbname=db.settings.DB_name,
        user=db.settings.user_name,
        password=db.settings.password,
        host=db.settings.postgres_host,
        port=db.settings.port)

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



