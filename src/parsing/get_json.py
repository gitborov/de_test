import requests
# from src.parsing.parsing_json import parsing_json_data
# from src.settings import settings
url_multy = 'https://randomuser.me/api/?results=5'


def get_data_from_api(url):
    try:
        data = requests.get(url)
        return data.json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

# if __name__ == "__main__":
#     get_data_from_api()


# print(get_data_from_api(url_multy))