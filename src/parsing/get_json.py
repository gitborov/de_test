import requests
# from src.parsing.parsing_json import parsing_json_data
from src.settings import settings
from src.loging.configure_logging import configure_logging

# url_multy = 'https://randomuser.me/api/?results=5'

logger = configure_logging(r'C:\Users\SM\PycharmProjects\testing_de\logg.log')

def get_data_from_api(url):

    try:
        data = requests.get(url)
        return data.json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        logger.error('Error fetching data from API: {}'.format(e))
        raise SystemExit(e)


def get_multy_records(url, n):
    multy_url = url + str(n)
    logger.info('Retrieved data successfully from {}'.format(multy_url))
    return get_data_from_api(multy_url)

# print(get_multy_records(settings.URL, settings.NUM_PAGE))
if  __name__ == '__main__':
    get_multy_records(settings.URL, settings.NUM_PAGE)