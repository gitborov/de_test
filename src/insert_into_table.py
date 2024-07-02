import psycopg2
from get_json_data import get_data
from src.connection.postgres import with_connection

url = 'https://randomuser.me/api/'
# url_multy = 'https://randomuser.me/api/?results=5'

# print(get_data(url)[0]['users'])


try:
	connection = psycopg2.connect(dbname='postgres',
								  user="admin",
								  password="password",
								  host="127.0.0.1",
								  port="5433")
	cursor = connection.cursor()

	users_insert_query = f""" 
		insert into de_test_schema.users (gender, name_title, name_first, age, nat)
		VALUES (%s,%s,%s,%s,%s)
		returning user_id
	"""

	cursor.execute(users_insert_query, get_data(url)[0]['users'])
	user_id = cursor.fetchall()[0][0]

	# print(get_data(url)[0]['contact_details'])
	# print(user_id)
	# print(get_data(url)[0]['contact_details'].insert(0, user_id))
	# print(list(user_id) + get_data(url)[0]['contact_details'])

	# contact_insert_query = f"""
	# 	insert into de_test_schema.contact_details (user_id, phone, cell)
	# 	VALUES (%s,%s,%s)"""
	# cursor.fetchall() Возвращает список с кортежем, в котором хранится id записи
	# cursor.execute(contact_insert_query, get_data(url)[0]['contact_details'].insert(0, cursor.fetchall()[0][0]))

	connection.commit()


	print("Record inserted successfully \
	into users table")

except (Exception, psycopg2.Error) as error:
	print("Failed to insert record into users table", error)

finally:
	# closing database connection.
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")


@with_connection
def insert_into_table(cursor, data):
	users_insert_query = f""" 
		insert into de_test_schema.users (gender, name_title, name_first, age, nat)
		VALUES (%s,%s,%s,%s,%s)
		returning user_id
	"""

	cursor.execute(users_insert_query, data)
	return cursor.fetchall()

data = get_data(url)[0]['users']

print(insert_into_table(data))