import psycopg2
from src.connection.postgres import with_connection
from src.parsing.parsing_json import (get_users_data,
									  valid_data,
									  get_contact_details,
									  get_cities_data,
									  get_locations_data,
									  get_media_data,
									  get_registration_data)

url = 'https://randomuser.me/api/'


# url_multy = 'https://randomuser.me/api/?results=5'


#
# try:
# 	connection = psycopg2.connect(dbname='postgres',
# 								  user="admin",
# 								  password="password",
# 								  host="127.0.0.1",
# 								  port="5433")
# 	cursor = connection.cursor()
#
# 	users_insert_query = f"""
# 		insert into de_test_schema.users (gender, name_title, name_first, age, nat)
# 		VALUES (%s,%s,%s,%s,%s)
# 		returning user_id
# 	"""
#
# 	cursor.execute(users_insert_query, get_data(url)[0]['users'])
# 	user_id = cursor.fetchall()[0][0]
#
# 	# print(get_data(url)[0]['contact_details'])
# 	# print(user_id)
# 	# print(get_data(url)[0]['contact_details'].insert(0, user_id))
# 	# print(list(user_id) + get_data(url)[0]['contact_details'])
#
# 	# contact_insert_query = f"""
# 	# 	insert into de_test_schema.contact_details (user_id, phone, cell)
# 	# 	VALUES (%s,%s,%s)"""
# 	# cursor.fetchall() Возвращает список с кортежем, в котором хранится id записи
# 	# cursor.execute(contact_insert_query, get_data(url)[0]['contact_details'].insert(0, cursor.fetchall()[0][0]))
#
# 	connection.commit()
#
#
# 	print("Record inserted successfully \
# 	into users table")
#
# except (Exception, psycopg2.Error) as error:
# 	print("Failed to insert record into users table", error)
#
# finally:
# 	# closing database connection.
# 	if connection:
# 		cursor.close()
# 		connection.close()
# 		print("PostgreSQL connection is closed")


# @with_connection
# def insert_into_table(cursor, data):
# 	users_insert_query = f"""
# 		insert into de_test_schema.users (gender, name_title, name_first, age, nat)
# 		VALUES (%s,%s,%s,%s,%s)
# 		returning user_id
# 	"""
#
# 	cursor.execute(users_insert_query, data)
# 	return cursor.fetchall()


class PrepareForQuery:
	def __init__(self, value):
		self.value = value

	def get_columns(self):
		columns = str(tuple(self.value.keys())).replace("'", "")
		return columns

	def get_s_string(self):
		s_string = ('%s,' * len(self.value))[:-1]
		return s_string

	def get_values(self):
		values = tuple(self.value.values())
		return values


@with_connection
def insert_data(cursor, data, scheme_name):

	users_data = PrepareForQuery(get_users_data(data))
	users_insert_query = f'''
		insert into {scheme_name}.users {users_data.get_columns()}
		values ({users_data.get_s_string()})
		returning user_id'''
	cursor.execute(users_insert_query, users_data.get_values())

	user_id = cursor.fetchall()[0][0]

	contact_data = PrepareForQuery(get_contact_details(data, user_id))
	contact_insert_query = f'''
		insert into {scheme_name}.contact_details {contact_data.get_columns()}
		values ({contact_data.get_s_string()})
		returning user_id'''
	cursor.execute(contact_insert_query, contact_data.get_values())

	media_data = PrepareForQuery(get_media_data(data, user_id))
	media_insert_query = f'''
		insert into {scheme_name}.media_data {media_data.get_columns()}
		values ({media_data.get_s_string()})
		returning user_id'''
	cursor.execute(media_insert_query, media_data.get_values())

	registration_data = PrepareForQuery(get_registration_data(data, user_id))
	registration_insert_query = f'''
		insert into {scheme_name}.registration_data {registration_data.get_columns()}
		values ({registration_data.get_s_string()})
		returning *'''
	cursor.execute(registration_insert_query, registration_data.get_values())

	temp_registration = cursor.fetchall()
	print(temp_registration)
	try:
		cities_data = PrepareForQuery(get_cities_data(data))
		cities_insert_query = f'''
			insert into {scheme_name}.cities {cities_data.get_columns()}
			values ({cities_data.get_s_string()})
			returning city_id'''
		cursor.execute(cities_insert_query, cities_data.get_values())

		city_id = cursor.fetchall()[0][0]
	except:
		q = (f'''select city_id from {scheme_name}.cities
				where '''
			 )


	locations_data = PrepareForQuery(get_locations_data(data, user_id,  city_id))
	locations_insert_query = f'''
		insert into {scheme_name}.locations {locations_data.get_columns()}
		values ({locations_data.get_s_string()})
		returning user_id'''
	cursor.execute(locations_insert_query, locations_data.get_values())

	return print(cursor.fetchall())


insert_data(data=valid_data, scheme_name='de_test_schema')
# print(get_users_data(valid_data))
print(get_cities_data(valid_data))


