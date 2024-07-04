import requests
# from src.parsing.parsing_json import parsing_json_data
from src.settings import settings
# url_multy = 'https://randomuser.me/api/?results=5'


def get_data_from_api(url):
    try:
        data = requests.get(url)
        return data.json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


def get_multy_records(url, n):
    multy_url = url + str(n)
    return get_data_from_api(multy_url)

print(get_multy_records(settings.URL, settings.NUM_PAGE))