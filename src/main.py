from pprint import pprint

from src.classes import HeadHunterAPI
from src.json_saver import JSONSaver
from work_data.constants import NONCOLOR, YELLOW

if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver('../data/test.json')

    vacancies = hh_api.get_filtered_vacancies('Python')
    json_saver.write_vacancies(vacancies)

    bd: list = json_saver.read_vacancies()

    # pprint(bd)

    for i in bd:
        print(i)
        print()

    # for k in i:
    #     print(YELLOW, k, NONCOLOR)
    # print()

    # json_saver.del_vacancies()


