def parsing_json_data(data):
    '''функция принимает словарь с данными одного пользователя
    и формирует списки с данными, которые нужны для талблиц
    возвращает словарь, где каждый внутренный список - данные для одной таблицы '''

    data_dict = {
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
        'location_postcode': data['location']['postcode'],
        'location_latitude': data['location']['coordinates']['latitude'],
        'location_longitude': data['location']['coordinates']['longitude'],

        'cities_city': data['location']['city'],
        'cities_state': data['location']['state'],
        'cities_country': data['location']['country'],
        'cities_timezone_offset': data['location']['timezone']['offset'],
        'cities_timezone_description': data['location']['timezone']['description'],
    }

    return data_dict
    # return {
    #     'users': users_data_list,
    #     'contact_details': contact_data_list,
    #     'media_data': media_data_list,
    #     'registration_data': registration_data_list,
    #     'location': location_data_list,
    #     'cities': cities_data_list
    # }
