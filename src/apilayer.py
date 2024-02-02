import json
from pprint import pprint

import requests

from config.api_config import APILayer_APIKey
from work_data.adress import DATA_CURRENCY_PATH


def get_currency_rate():
    """Получает курс валюты от API и возвращает его в виде float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {"apikey": APILayer_APIKey}
    params = {"base": 'RUB'}

    response = requests.get(url, headers=headers, params=params)
    response_data = json.loads(response.text)['rates']

    dir_file = DATA_CURRENCY_PATH

    with open(dir_file, mode='w') as file:
        json.dump(response_data, file, indent=2)


# get_currency_rate()
