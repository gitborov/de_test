import requests
# from src.parsing.parsing_json import parsing_json_data
# from src.settings import settings
from src.loging.configure_logging import configure_logging

url_multy = 'https://randomuser.me/api/?results='

# logger = configure_logging(r'C:\Users\SM\PycharmProjects\testing_de\logg.log')

def get_data_from_api(url: str, n: int)-> dict:
    ''' функция для получения данных из API'''

    multy_url = url + str(n)
    try:
        data = requests.get(multy_url)
        return data.json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        # logger.error('Error fetching data from API: {}'.format(e))
        raise SystemExit(e)



