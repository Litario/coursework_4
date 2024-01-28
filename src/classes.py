from abc import ABC, abstractmethod
from pprint import pprint

import requests

from config.api_config import SuperJob_APIKey
from work_data.constants import NONCOLOR, YELLOW


class abc_class(ABC):

    @abstractmethod
    def get_vacancies(self, value: str, per_page: int):
        pass

    @abstractmethod
    def get_filtered_vacancies(self, value: str):
        pass


class SuperJobAPI(abc_class):

    def __init__(self):
        self.__url = 'https://api.superjob.ru/2.0'
        self.__platform = 'SuperJob'

    def get_vacancies(self, value: str, count: int = 20) -> list:
        """
        Создает список вакансий по параметру запроса text API SuperJob.
        :param value: слово для фильтрации всего списка вакансий
        :return: список словарей с вакансиями
        """

        vac_url = self.__url + '/vacancies/'
        headers = {'X-Api-App-Id': SuperJob_APIKey}

        params = {'keyword': value, 'page': 0, 'count': count}
        response: dict = requests.get(url=vac_url, params=params, headers=headers).json()
        vacancies: list = response['objects']

        return vacancies

    def get_filtered_vacancies(self, value: str) -> list:
        """
        Фильтрует список вакансий.
        :param value: параметр для метода get_vacancies
        :return: список словарей с отфильтрованными вакансиями
        """

        vacancies: list = self.get_vacancies(value)

        filter_vacancies = []
        for i in vacancies:
            # a: (dict, None) = i['salary']  # переменная для упрощения кода
            vacancy = {'name': i['profession'],
                       'experience': i['experience']['title'],
                       'salary_from': i['payment_from'],
                       'salary_to': i['payment_to'],
                       'salary_currency': i['currency'],
                       'employer': {'name': i['firm_name'], 'url': i['link']},
                       'area': i['town']['title'],
                       'schedule': i['type_of_work']['title'],
                       'platform': self.__platform
                       }
            filter_vacancies.append(vacancy)

        return filter_vacancies


class HeadHunterAPI(abc_class):
    """Класс для сайта HeadHunter"""

    def __init__(self):
        self.__url = 'https://api.hh.ru'
        self.__platform = 'HeadHunter'

    def get_vacancies(self, value: str, per_page: int = 40) -> list:
        """
        Создает список вакансий по параметру запроса text API HeadHunter.
        :param per_page: количество вакансий на странице
        :param value: слово для фильтрации всего списка вакансий
        :return: список словарей с вакансиями
        """

        vac_url = self.__url + '/vacancies'
        params = {'text': value, 'per_page': per_page}
        response: dict = requests.get(url=vac_url, params=params).json()
        vacancies: list = response['items']

        return vacancies

    def get_filtered_vacancies(self, value: str) -> list:
        """
        Фильтрует список вакансий.
        :param value: параметр для метода get_vacancies
        :return: список словарей с отфильтрованными вакансиями
        """

        vacancies: list = self.get_vacancies(value)

        filter_vacancies = []
        for i in vacancies:
            a: (dict, None) = i['salary']  # переменная для упрощения кода
            vacancy = {'name': i['name'],
                       'experience': i['experience']['name'],
                       # 'salary': a,
                       'salary_from': a['from'] if (isinstance(a, dict) and a['from']) else 0,
                       'salary_to': a['to'] if isinstance(a, dict) else 0,
                       'salary_currency': a['currency'] if isinstance(a, dict) else None,
                       'employer': {'name': i['employer']['name'], 'url': i['employer']['url']},
                       'area': i['area']['name'],
                       'schedule': i['schedule']['name'],
                       'platform': self.__platform
                       }
            filter_vacancies.append(vacancy)

        return filter_vacancies


# hh_api = HeadHunterAPI()
# print(hh_api.get_vacancies('Python'))
# x = hh_api.get_filtered_vacancies('Python')
# print(x)

# for i in x:
#     for k, v in i.items():
#         print(YELLOW, k, NONCOLOR, v)
#     print()

# ic(hh_api.get_vacancies('Python'))

# sj_api = SuperJobAPI()
# print(type(sj_api.get_vacancies('Python')))
# pprint(sj_api.get_vacancies('Python'))
# print(sj_api.get_vacancies('Python')['profession'])

# x = sj_api.get_filtered_vacancies('Python')
# pprint(x)
