from pydantic import BaseModel, EmailStr, Field, model_validator, field_validator
from src.parsing.get_json import get_data_from_api
from src.validation.password_valid import check_pass


class Validate(BaseModel):
    users_gender: str
    users_name_title: str
    users_name_first: str
    users_age: int
    users_nat: str

    contact_phone: str
    contact_cell: str

    media_picture: str

    # проверка email  через pydantyc[email]
    registration_email: EmailStr
    registration_username: str
    registration_password: str
    registration_password_md5: str
    registration_password_validation: bool = False

    @model_validator(mode='after')
    def set_password_validation(cls, values):
        values.registration_password_validation = check_pass(values.registration_password)
        return values

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


def get_valid_data_from_json(data: dict) -> dict:
    temp_valid = None
    try:
        temp_valid = Validate(**(data))
        return temp_valid.model_dump()
    except ValueError as e:
        print(e)
        # raise e

    return data

