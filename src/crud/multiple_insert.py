# -*- coding: utf-8 -*-
from src.settings import settings
from src.crud.create_data_base import create_db
from src.parsing.get_json import get_multy_records
from src.parsing.parsing_json import parsing_json_data
from src.validation.validation_data import get_valid_data_from_json
from src.crud.insert_into_table import insert_data


def multiple_insert():
    # создание базы
    create_db()
    #
    # получение данных
    data = get_multy_records(settings.URL, settings.NUM_PAGE)
    for i in range(settings.NUM_PAGE):
        print('im here')
        # парсинг
        parsed_data = parsing_json_data(data['results'][i])
        # валидация
        valid_data = get_valid_data_from_json(parsed_data)
        # запись в БД
        inserted_data = insert_data(data=valid_data, scheme_name=settings.SCHEME)
