



import requests
from src.validation.validation_data import Validate

url = 'https://randomuser.me/api/'
url_multy = 'https://randomuser.me/api/?results=5'

r = requests.get(url=url)


# users_gender = r.json()['results'][0]['gender']
# users_name_title = r.json()['results'][0]['name']['title']
# users_name_first = r.json()['results'][0]['name']['first']
# users_age = r.json()['results'][0]['dob']['age']
# users_nat = r.json()['results'][0]['nat']
# data_list = [users_gender, users_name_title, users_name_first, users_age, users_nat]
# print(r.json())
def parsing_users(data):
    '''функция принимает словарь с данными одного пользователя
    и формирует списки с данными, которые нужны для талблиц
    возвращает словарь, где каждый внутренный список - данные для одной таблицы '''

    data = Validate(users_gender = data['gender'],
    users_name_title = data['name']['title'],
    users_name_first = data['name']['first'],
    users_age = data['dob']['age'],
    users_nat = data['nat'],
    # users_data_list = [users_gender, users_name_title, users_name_first, users_age, users_nat]

    contact_phone = data['phone'],
    contact_cell = data['cell'],
    # contact_data_list = [contact_phone, contact_cell]

    media_picture = data['picture']['medium'],
    # media_data_list = [media_picture]

    registration_email = data['email'],
    registration_username = data['login']['username'],
    registration_password = data['login']['password'],
    registration_password_md5 = data['login']['md5'],
    # registration_data_list = [
    #     registration_email,
    #     registration_username,
    #     registration_password,
    #     registration_password_md5
    # ]

    # location_city_id = data['location']
    location_street_name = data['location']['street']['name'],
    location_street_number = data['location']['street']['number'],
    location_postcode = data['location']['postcode'],
    location_latitude = data['location']['coordinates']['latitude'],
    location_longitude = data['location']['coordinates']['longitude'],
    # location_data_list = [
    #     location_street_name,
    #     location_street_number,
    #     location_postcode,
    #     location_latitude,
    #     location_longitude
    # ]

    cities_city = data['location']['city'],
    cities_state = data['location']['state'],
    cities_country = data['location']['country'],
    cities_timezone_offset = data['location']['timezone']['offset'],
    cities_timezone_description = data['location']['timezone']['description'])
    # cities_data_list = [
    #     cities_city,
    #     cities_state,
    #     cities_country,
    #     cities_timezone_offset,
    #     cities_timezone_description
    # ]
    return data
    #     {
    #     'users': users_data_list,
    #     'contact_details': contact_data_list,
    #     'media_data': media_data_list,
    #     'registration_data': registration_data_list,
    #     'location': location_data_list,
    #     'cities': cities_data_list
    # }


# print(cities_timezone_description)
# data = {'users':
#             {'gender': (r.json()['results'][0]['gender']),
#              'name_title': (r.json()['results'][0]['name']['title']),
#              'name_first': r.json()['results'][0]['name']['first'],
#              'age': r.json()['results'][0]['dob']['age'],
#              'nat': r.json()['results'][0]['nat']
#              }
#         }


# print(data)


# print(data_list)

def get_data(url):
    '''
    формирует список словарей
    '''
    req = requests.get(url)
    data_list = []
    for elem in req.json()['results']:
        data_list.append(parsing_users(elem))
    return data_list


#
for elem in get_data(url_multy):
    print(elem.users_gender)


#
# get_multiple_users(url)

