import json

from src.apilayer import get_currency_rate
from work_data.constants import NONCOLOR, BLUE


class Vacancy:

    def __init__(self, name, experience, salary_from, salary_to,
                 salary_currency, employer, area, schedule, platform):
        self.__name = name
        self.__experience = experience
        self.__salary_from = salary_from
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__salary_currency: str = salary_currency
        self.__employer = employer
        self.__area = area
        self.__schedule = schedule
        self.__platform = platform
        self.rub_salary_currency()

        # self.__name = kwargs[0]
        # self.__experience = kwargs[1]
        # self.__salary_from = kwargs[2]
        # self.__salary_to = kwargs[3]
        # self.__salary_currency = kwargs[4]
        # self.__employer = kwargs[5]
        # self.__area = kwargs[6]
        # self.__schedule = kwargs[7]

    def rub_salary_currency(self):
        """Перевод в рублевую зарплату, если вакансия содержит не рублевые значения"""

        sc = self.__salary_currency

        if sc is None:
            self.__rub_salary_from = 0
            self.__rub_salary_to = 0

        else:
            dir_file = '../data/data_currency.json'
            with open(dir_file, mode='r') as file:
                currency_base: dict = json.load(file)

            currency_base.setdefault('RUR', 1)
            currency_base.setdefault('rub', 1)
            currency_base.setdefault('RUB', 1)

            if self.__salary_from is None:
                self.__rub_salary_from = 0
            else:
                self.__rub_salary_from = round((self.__salary_from / currency_base[sc]) / 50) * 50

            if self.__salary_to is None:
                self.__rub_salary_to = 0
            else:
                self.__rub_salary_to = round((self.__salary_to / currency_base[sc]) / 50) * 50

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    def __str__(self):
        STR_CS1 = '<не указано>'
        STR_CS2 = ''

        if self.__salary_currency in ('rub', 'RUR', 'RUB'):
            return (f'{BLUE}Вакансия:{NONCOLOR} {self.__name}\n'
                    f'{BLUE}Опыт работы:{NONCOLOR} {self.__experience}\n'
                    f'{BLUE}Город:{NONCOLOR} {self.__area}\n'
                    f'{BLUE}Зарплата:{NONCOLOR} от {f"{self.__salary_from:_}" if self.__salary_from else STR_CS1}'
                    f' до {f"{self.__salary_to:_}" if self.__salary_to else STR_CS1} ({self.__salary_currency})\n'
                    f'{BLUE}Платформа:{NONCOLOR} {self.__platform}')

        return (f'{BLUE}Вакансия:{NONCOLOR} {self.__name}\n'
                f'{BLUE}Опыт работы:{NONCOLOR} {self.__experience}\n'
                f'{BLUE}Город:{NONCOLOR} {self.__area}\n'

                f'{BLUE}Зарплата:{NONCOLOR} от {f"{self.__salary_from:_}" if self.__salary_from else STR_CS1}'
                f' до {f"{self.__salary_to:_}" if self.__salary_to else STR_CS1} '
                f'{f"({self.__salary_currency})" if self.__salary_from or self.__salary_to else STR_CS2}\n'

                f'{BLUE}Зарплата в рублях:{NONCOLOR} от {f"{self.__rub_salary_from:_}" if self.__salary_from else STR_CS1}'
                f' до {f"{self.__rub_salary_to:_}" if self.__salary_to else STR_CS1}\n'

                f'{BLUE}Платформа:{NONCOLOR} {self.__platform}')

        # return (f'{BLUE}Вакансия:{NONCOLOR} {self.__name}\n'
        #         f'{BLUE}Опыт работы:{NONCOLOR} {self.__experience}\n'
        #         f'{BLUE}Город:{NONCOLOR} {self.__area}\n'
        #         # f'{BLUE}Зарплата:{NONCOLOR} от {self.__salary_from}\n'
        #         f'{BLUE}Зарплата:{NONCOLOR} от {f"{self.__salary_from:_}" if self.__salary_from else STR_CS1}'
        #         f' до {f"{self.__salary_to:_}" if self.__salary_to else STR_CS1} '
        #         f'{f"({self.__salary_currency})" if self.__salary_from or self.__salary_to else STR_CS2}\n'
        #         f'{BLUE}Платформа:{NONCOLOR} {self.__platform}')

    def __lt__(self, other):
        if isinstance(other, int):
            return self.__rub_salary_from < other
        return self.__rub_salary_from < other.__rub_salary_from

    def __gt__(self, other):
        if isinstance(other, int):
            return self.__rub_salary_from > other
        return self.__rub_salary_from > other.__rub_salary_from


# vacancy = Vacancy()

# for i in vacancy.mt():
#     for k, v in i.items():
#         print(YELLOW, k, NONCOLOR, v)
#     print()
