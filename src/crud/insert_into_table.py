import psycopg2
from src.connection.postgres import with_connection
from src.crud.prepare_data import PrepareForQuery


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
