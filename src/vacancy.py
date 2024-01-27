from work_data.constants import NONCOLOR, YELLOW, BLUE
from classes import HeadHunterAPI


class Vacancy:

    def __init__(self, name, experience, salary_from, salary_to,
                 salary_currency, employer, area, schedule, platform):
        self.__name = name
        self.__experience = experience
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__salary_currency = salary_currency
        self.__employer = employer
        self.__area = area
        self.__schedule = schedule
        self.__platform = platform

        # self.__name = kwargs[0]
        # self.__experience = kwargs[1]
        # self.__salary_from = kwargs[2]
        # self.__salary_to = kwargs[3]
        # self.__salary_currency = kwargs[4]
        # self.__employer = kwargs[5]
        # self.__area = kwargs[6]
        # self.__schedule = kwargs[7]

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    def __str__(self):
        CS1 = '<не указано>'
        CS2 = ''
        return (f'{BLUE}Вакансия:{NONCOLOR}  {self.__name}\n'
                f'{BLUE}Опыт работы:{NONCOLOR}  {self.__experience}\n'
                f'{BLUE}Город:{NONCOLOR}  {self.__area}\n'
                # f'{BLUE}Зарплата:{NONCOLOR} от {self.__salary_from}\n'
                f'{BLUE}Зарплата:{NONCOLOR} от {self.__salary_from if self.__salary_from else CS1} '
                f'до {self.__salary_to if self.__salary_to else CS1} '
                f'{f"({self.__salary_currency})" if self.__salary_from or self.__salary_to else CS2}\n'
                f'{BLUE}Платформа:{NONCOLOR}  {self.__platform}')

    def __lt__(self, other):
        if isinstance(other, int):
            return self.__salary_from < other
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        if isinstance(other, int):
            return self.__salary_from > other
        return self.__salary_from > other.__salary_from

# vacancy = Vacancy()

# for i in vacancy.mt():
#     for k, v in i.items():
#         print(YELLOW, k, NONCOLOR, v)
#     print()
