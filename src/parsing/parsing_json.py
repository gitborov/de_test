from  src.parsing.get_json import get_data_from_api
from src.loging.configure_logging import configure_logging

# logger = configure_logging(r'C:\Users\SM\PycharmProjects\testing_de\logg.log')


def parsing_json_data(data: dict) -> dict:
    '''функция принимает словарь с данными одного пользователя
    и формирует списки с данными, которые нужны для талблиц
    возвращает словарь, где каждый внутренный список - данные для одной таблицы '''

    data_dict = {
        # use get for parsing
        'users_gender': data['gender'],
        'users_name_title': data['name']['title'],
        'users_name_first': data['name']['first'],
        'users_age': data['dob']['age'],
        'users_nat': data['nat'],

        'contact_phone': data['phone'],
        'contact_cell': data['cell'],

        'media_picture': data['picture']['medium'],

        'registration_email': data['email'],
        'registration_username': data['login']['username'],
        'registration_password': data['login']['password'],
        'registration_password_md5': data['login']['md5'],

        # location_city_id = data['location']
        'location_street_name': data['location']['street']['name'],
        'location_street_number': data['location']['street']['number'],
        'location_postcode': str(data['location']['postcode']),
        'location_latitude': data['location']['coordinates']['latitude'],
        'location_longitude': data['location']['coordinates']['longitude'],

        'cities_city': data['location']['city'],
        'cities_state': data['location']['state'],
        'cities_country': data['location']['country'],
        'cities_timezone_offset': data['location']['timezone']['offset'],
        'cities_timezone_description': data['location']['timezone']['description'],
    }
    # logger.info('Data parsed successfully')
    return data_dict


# data = get_data_from_api(url_multy)['results'][0]
# data = get_data_from_api(url_valid_pass)['results'][0]

