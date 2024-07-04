# -*- coding: utf-8 -*-
from src.settings import settings
from src.crud.create_data_base import create_db
from src.parsing.get_json import get_multy_records

def main():
    # создание базы
    create_db()
    data = get_multy_records(settings.URL, settings.NUM_PAGE)
    for i in range(settings.NUM_PAGE):




if __name__ == '__main__':
    main()
