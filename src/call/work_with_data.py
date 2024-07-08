# -*- coding: utf-8 -*-
import os
from src.crud.create_data_base import create_db
from src.parsing.get_json import get_data_from_api
from src.parsing.parsing_json import parsing_json_data
from src.parsing.pars_valid_data import *
from src.validation.validation_data import get_valid_data_from_json
from src.crud.insert_into_table import insert_data
from src.connection.postgres import with_connection
from src.loging.configure_logging import configure_logging
from pathlib import Path
from src.crud.read_data import read_data

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[2]
p = os.path.join(root_path, 'logg.log')
# print(p)
# print(root_path)
logger = configure_logging(p)


@with_connection
def get_city_id(cursor, name: str, scheme_name: str) -> int:
    ''' Функция для получения id города по его названию. '''
    q = f"select city_id from {scheme_name}.cities where city = '{name}'"
    cursor.execute(q)
    return cursor.fetchall()[0][0]

from prettytable import PrettyTable

class DataWork:
    ''' Большая фунция, объединяющая весь функционал. позволяет использовать только один цикл.
    Получаем данные и в цикле их парсим, валидируем и вставляем в таблицы
    '''
    def __init__(self, settings):
        self.URL = settings.URL
        self.scheme_name = settings.SCHEME

    def insert_data(self, num_page: int = 1):
        try:
        # создание базы
            create_db()
            logger.debug('Created database successfully')
        except Exception as e:
            logger.error(f'Error occurred while creating database: {e}')

        # получение данных
        data = get_data_from_api(self.URL, num_page)

        for i in range(num_page):
            # парсинг
            parsed_data = parsing_json_data(data['results'][i])
            logger.debug('Retrieved data successfully')


            # валидация
            try:
                valid_data = get_valid_data_from_json(parsed_data)
                logger.debug('Validated data successfully')
            except Exception as e:
                #если произошла ошибка валидации вставляем данные в таблицу invalid_data
                logger.error(f'Error occurred while validating data: {e}')
                invalid_data = get_invalid_data(parsed_data)
                insert_data(data=invalid_data, scheme_name=self.scheme_name)
                logger.debug('Inserted invalid data successfully to invalid_data table')
                break


            # формируем нужный словарь для каждой таблицы из валидных данных
            users_data = get_users_data(valid_data)
            user_id = insert_data(data=users_data, scheme_name=self.scheme_name)
            logger.debug(f'Inserted data successfully for user {user_id}')

            contact_data = get_contact_details(valid_data, user_id)
            insert_data(data=contact_data, scheme_name=self.scheme_name)

            media_data = get_media_data(valid_data, user_id)
            insert_data(data=media_data, scheme_name=self.scheme_name)

            registration_data = get_registration_data(valid_data, user_id)
            insert_data(data=registration_data, scheme_name=self.scheme_name)


            # в данном блоке пытаемся вставить данные о городе.Если такого города нет в базе то вставляем его и получаем id.
            # если такой город есть, то получаем ошибку и в блоке except вызываем функцию get_city_id которая по имени города получает его id
            cities_data = get_cities_data(valid_data)
            try:
                city_id = insert_data(data=cities_data, scheme_name=self.scheme_name)
                logger.debug(f'Inserted data successfully for city {city_id}')
            except Exception as e:
                if e:
                    logger.error(f'Error occurred while inserting data: {e}')
                else:
                    city_name = cities_data['cities']['city']
                    city_id = get_city_id(name=city_name, scheme_name=self.scheme_name)
                    logger.debug(f'City {city_name} already exists. ID = {city_id}')

            locations_data = get_locations_data(valid_data, user_id, city_id)
            insert_data(data=locations_data, scheme_name=self.scheme_name)

            logger.info('Inserted data successfully')


    def read_data(self, flag: bool = True):
        '''Функция для вывода данных в консоль'''
        table = PrettyTable()
        table.field_names = ['user_id', 'username', 'password', 'password_validation']

        try:
            data = read_data(schema_name=self.scheme_name, flag=flag)
            for elem in data:
                table.add_row(elem)
            print(table)
            logger.debug('Read data successfully')
        except Exception as e:
            logger.error(f'Error occurred while reading data: {e}')
