import requests
from src.parsing.parsing_json import parsing_json_data

url_multy = 'https://randomuser.me/api/?results=5'


def get_data(url):
    '''
    формирует список словарей
    '''
    req = requests.get(url)
    data_list = []
    for elem in req.json()['results']:
        data_list.append(parsing_json_data(elem))
    return data_list


    # try:

if __name__ == "__main__":
    print(get_data(url_multy))