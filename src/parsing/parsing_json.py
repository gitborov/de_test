from  src.parsing.get_json import get_data_from_api
from src.validation.validation_data import Validate
import json
url_multy = 'https://randomuser.me/api/?results=1'
url_valid_pass = 'https://randomuser.me/api/?results=1&password=special,upper,lower,number'

def parsing_json_data(data):
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

    return data_dict


# data = get_data_from_api(url_multy)['results'][0]
data = get_data_from_api(url_valid_pass)['results'][0]


def get_valid_data_from_json(data):
    temp_valid = None
    try:
        temp_valid = Validate(**parsing_json_data(data))
        return temp_valid.model_dump()
    except ValueError as e:
        print(e)
        # raise e

    return parsing_json_data(data)






def get_users_data(data):
    users_dict = {
        'gender': data.get('users_gender'),
        'name_title': data.get('users_name_title'),
        'name_first': data.get('users_name_first'),
        'age': data.get('users_age'),
        'nat': data.get('users_nat')
    }
    return users_dict

def get_contact_details(data, user_id):
    contact_details_dict = {
        'user_id': user_id,
        'phone': data.get('contact_phone'),
        'cell': data.get('contact_cell')
    }
    return contact_details_dict


def get_media_data(data, user_id):
    media_data_dict = {
        'user_id': user_id,
        'picture': data.get('media_picture')
    }
    return media_data_dict


def get_registration_data(data, user_id):
    registration_data_dict = {
        'user_id': user_id,
        'email': data.get('registration_email'),
        'username': data.get('registration_username'),
        'password': data.get('registration_password'),
        'password_md5': data.get('registration_password_md5'),
        'password_validation': data.get('registration_password_validation')
    }
    return registration_data_dict


def get_cities_data(data):
    cities_data_dict = {
        'city': data.get('cities_city'),
        'state': data.get('cities_state'),
        'country': data.get('cities_country'),
        'timezone_offset': data.get('cities_timezone_offset'),
        'timezone_description': data.get('cities_timezone_description')
    }
    return cities_data_dict


def get_locations_data(data, user_id, city_id):
    locations_data_dict = {
        'user_id': user_id,
        'city_id': city_id,
        'street_name': data.get('location_street_name'),
        'street_number': data.get('location_street_number'),
        'postcode': data.get('location_postcode'),
        'latitude': data.get('location_latitude'),
        'longitude': data.get('location_longitude')
    }
    return locations_data_dict


valid_data = get_valid_data_from_json(data)


# print(Validate(**parsing_json_data(data)).model_dump())
# print(get_registration_data(valid_data, 1))