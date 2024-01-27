from src.classes import HeadHunterAPI, SuperJobAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from work_data.constants import NONCOLOR, YELLOW, GREEN, BLUE


## _____________________________________________________________ functions

def output_sorted_vacancies(data: list, number: int = 0, reverse=True, salary_zero_filter=False):
    n = len(data) if number == 0 else number

    if reverse:
        for i in sorted(data, reverse=reverse)[:n]:
            print(i)
            print('-' * 60)
    else:
        if salary_zero_filter:
            filtered_data: list[Vacancy] = filter(lambda v: v > 0, data)
            for i in sorted(filtered_data, reverse=reverse)[:n]:
                print(i)
                print('-' * 60)
        else:
            for i in sorted(data, reverse=reverse)[:n]:
                print(i)
                print('-' * 60)


def output_filtered_vacancies(data: list, search_word: str, key):
    filtered_vacancies_list = []

    for i in data:
        ## self.__name - class Vacancy instance attribute
        if key == 1:
            if search_word.lower() in i.name.lower():
                filtered_vacancies_list.append(i)

        ## self.__area - class Vacancy instance attribute
        elif key == 2:
            if search_word.lower() in i.area.lower():
                filtered_vacancies_list.append(i)

    if len(filtered_vacancies_list):
        for j in sorted(filtered_vacancies_list, key=lambda v: v.area):
            print(j)
            print('-' * 60)
    else:
        print('Нет ни одной вакансии, содержащей такое слово в названии.')


## _____________________________________________________________ main_code


# word_query: str = input('Введите слово, по которому будет происходить '
#                         'поиск в вакансиях:\n')
word_query: str = 'python'

# platform_query = input('Какую платформу вакансий хотите использовать:\n'
#                        '1 - HeadHunter\n'
#                        '2 - SuperJob\n'
#                        '3 - обе платформы\n'
#                        '0 - завершить работу\n')

platform_query = '1'

if platform_query == '1':
    # hh_api = HeadHunterAPI()
    hh_api = SuperJobAPI()
    json_saver = JSONSaver('../data/test.json')

    vacancies = hh_api.get_filtered_vacancies(word_query)
    json_saver.write_vacancies(vacancies)

    bd: list = json_saver.read_vacancies()  # база данных с HeadHunter
    # bd: list = json_saver.read_vacancies()  # база данных с SuperJob

    print(f"Подобрано {BLUE}{len(bd)}{NONCOLOR} вакансий\n")

    task_query: str = input(f'{YELLOW}Введите номер задачи:{NONCOLOR}\n'
                            f'{GREEN}1{NONCOLOR} - вывести список вакансий по убыванию зарплаты\n'
                            f'{GREEN}2{NONCOLOR} - вывести список вакансий по возрастанию зарплаты\n'
                            f'{GREEN}3{NONCOLOR} - вывести список вакансий, с фильтрацией по названию \n'
                            f'{GREEN}4{NONCOLOR} - вывести список вакансий, с фильтрацией по городу \n')

    if task_query in ('1', '2'):
        vn = input(f"\nВы можете ввести кол-во вакансий, для вывода.\n"
                   f"Нажмите {GREEN}Enter{NONCOLOR},"
                   f"если хотите пропустить этот пункт\n")

        vacancy_number = int(vn) if bool(vn) else 0

        if task_query == '1':
            output_sorted_vacancies(bd, vacancy_number)
        elif task_query == '2':
            salary_filter_query = input(f'\n{YELLOW}Выводить вакансии с неуказанной зарплатой (да/нет)?{NONCOLOR}\n')
            if salary_filter_query.lower() in ('да', 'yes'):
                output_sorted_vacancies(bd, vacancy_number, False)
            elif salary_filter_query.lower() in ('нет', 'no'):
                output_sorted_vacancies(bd, vacancy_number, False, True)
            else:
                print('ОШИБКА'
                      'Обратиться к разработчику')

    elif task_query == '3':
        search_word = input(f'\n{YELLOW}Введите слово для поиска в названии вакансии:{NONCOLOR}\n')
        output_filtered_vacancies(bd, search_word, 1)

    elif task_query == '4':
        city_dict_query = input(f'\n{YELLOW}Показать статистику вакансий по городам ?{NONCOLOR}\n')

        if city_dict_query.lower() in ('да', 'yes'):
            city_dict = {}
            for i in bd:
                city_dict[i.area] = city_dict.get(i.area, 0) + 1

            for k, v in sorted(city_dict.items(), key=lambda x: x[1], reverse=True):
                print(f"{k:.<20} {BLUE}{v}{NONCOLOR} вакансий")

        search_word = input(f'\n{YELLOW}Выберите город:{NONCOLOR}\n')
        output_filtered_vacancies(bd, search_word, 2)
