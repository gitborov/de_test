import psycopg2
from src.connection.postgres import with_connection


class PrepareForQuery:
	'''Обрабатывает вложенный словарь типа
	{'users':
		{'gender': 'male',
		'name': 'John',
		'age': 30
		}}
	 ключ - название таблицы а знвачение - словарь с данными для вставки'''

	def __init__(self, value: dict):
		#добавил атрибут name, чтобы получить название таблицы
		#и затем в методах использовать его, чтобы получать данные из вложенного словаря
		self.value = value
		self.name = str(tuple(self.value.keys())[0])

	def get_columns(self):
		#получаем названия столбцов
		columns = str(tuple(self.value[self.name].keys())).replace("'", "")
		return columns

	def get_s_string(self):
		#получаем строку типа %s,%s,%s, где длина строки = количеству столбцов
		s_string = ('%s,' * len(self.value[self.name]))[:-1]
		return s_string

	def get_values(self):
		#получаем значения для вставки
		values = tuple(self.value[self.name].values())
		return values


@with_connection
def insert_data(cursor, data: dict, scheme_name: str):
	'''Функция для добавления данных в таблицу принимает словарь с данными и название схемы
		используе класс PrepareForQuery для подготовки данных.
		возвращает id добавленного пользователя'''
	inserted_data = PrepareForQuery(data)
	users_insert_query = f'''
		insert into {scheme_name}.{inserted_data.name} {inserted_data.get_columns()}
		values ({inserted_data.get_s_string()})
		returning *'''
	cursor.execute(users_insert_query, inserted_data.get_values())
	user_id = cursor.fetchall()[0][0]
	return user_id



#прошлая версия кода с множественным insert
# from src.parsing.pars_valid_data import (get_users_data,
# 										 get_contact_details,
# 										 get_cities_data,
# 										 get_locations_data,
# 										 get_media_data,
# 										 get_registration_data)

#
# class PrepareForQuery:
# '''Обрабатывает словарь типа
# 		{'gender': 'male',
# 		'name': 'John',
# 		'age': 30
# 		}'''
# 	def __init__(self, value):
# 		self.value = value
#
# 	def get_columns(self):
# 		columns = str(tuple(self.value.keys())).replace("'", "")
# 		return columns
#
# 	def get_s_string(self):
# 		s_string = ('%s,' * len(self.value))[:-1]
# 		return s_string
#
# 	def get_values(self):
# 		values = tuple(self.value.values())
# 		return values
#
#
# @with_connection
# def insert_data(cursor, data: dict, scheme_name: str):
#
# 	users_data = PrepareForQuery(get_users_data(data))
# 	users_insert_query = f'''
# 		insert into {scheme_name}.users {users_data.get_columns()}
# 		values ({users_data.get_s_string()})
# 		returning user_id'''
# 	cursor.execute(users_insert_query, users_data.get_values())
#
# 	user_id = cursor.fetchall()[0][0]
#
# 	contact_data = PrepareForQuery(get_contact_details(data, user_id))
# 	contact_insert_query = f'''
# 		insert into {scheme_name}.contact_details {contact_data.get_columns()}
# 		values ({contact_data.get_s_string()})
# 		returning user_id'''
# 	cursor.execute(contact_insert_query, contact_data.get_values())
#
# 	media_data = PrepareForQuery(get_media_data(data, user_id))
# 	media_insert_query = f'''
# 		insert into {scheme_name}.media_data {media_data.get_columns()}
# 		values ({media_data.get_s_string()})
# 		returning user_id'''
# 	cursor.execute(media_insert_query, media_data.get_values())
#
# 	registration_data = PrepareForQuery(get_registration_data(data, user_id))
# 	registration_insert_query = f'''
# 		insert into {scheme_name}.registration_data {registration_data.get_columns()}
# 		values ({registration_data.get_s_string()})
# 		returning *'''
# 	cursor.execute(registration_insert_query, registration_data.get_values())
#
# 	cities_data = PrepareForQuery(get_cities_data(data))
# 	cities_insert_query = f'''
# 		insert into {scheme_name}.cities {cities_data.get_columns()}
# 		values ({cities_data.get_s_string()})
# 		returning city_id'''
# 	cursor.execute(cities_insert_query, cities_data.get_values())
#
# 	city_id = cursor.fetchall()[0][0]
#
# 	locations_data = PrepareForQuery(get_locations_data(data, user_id,  city_id))
# 	locations_insert_query = f'''
# 		insert into {scheme_name}.locations {locations_data.get_columns()}
# 		values ({locations_data.get_s_string()})
# 		returning user_id'''
# 	cursor.execute(locations_insert_query, locations_data.get_values())





