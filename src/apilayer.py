import json

import requests

from config.api_config import APILayer_APIKey


def get_currency_rate():
    """Получает курс валюты от API и возвращает его в виде float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {"apikey": APILayer_APIKey}
    params = {"base": 'RUB'}

    response = requests.get(url, headers=headers, params=params)
    response_data = json.loads(response.text)['rates']

    dir_file = '../data/data_currency.json'

    with open(dir_file, mode='w') as file:
        json.dump(response_data, file, indent=2)
