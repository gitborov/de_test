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
