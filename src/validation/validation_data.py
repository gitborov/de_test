from pydantic import BaseModel, EmailStr, Field
from src.parsing.get_json import get_data


class Validate(BaseModel):
    users_gender: str
    users_name_title: str
    users_name_first: str
    users_age: int
    users_nat: str

    contact_phone: str
    contact_cell: str

    media_picture: str

    registration_email: str
    registration_username: str
    registration_password: str
    registration_password_md5: str

    # location_city_id = data['location']
    location_street_name: str
    location_street_number: int
    location_postcode: str
    location_latitude: float
    location_longitude: float

    cities_city: str
    cities_state: str
    cities_country: str
    cities_timezone_offset: str
    cities_timezone_description: str


# data = get_data('https://randomuser.me/api/?results=5')[0]
# print(data)
# Validate.
