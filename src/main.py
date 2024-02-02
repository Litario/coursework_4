from src.apilayer import get_currency_rate
from src.classes import HeadHunterAPI
from src.classes import SuperJobAPI
from src.function import output_sorted_vacancies, output_filtered_vacancies
from src.json_saver import JSONSaver
from work_data.adress import DATA_BASE_PATH
from work_data.constants import NONCOLOR, YELLOW, GREEN, BLUE, RED

if __name__ == '__main__':

    apilayer_task = input("\nПриветствую.\n"
                          "Это скрипт для поиска и выдачи рабочих вакансий по заданным критериям.\n"
                          "\n"
                          "Хотите обновить базу данных с курсом не рублевых зарплат через сайт\n"
                          "apilayer.com (необходим APIKey) ?\n"
                          "[Нажмите Enter, чтобы пропустить вопрос]")

    if apilayer_task in ('да', 'yes'):
        ## обновление базы данных с курсами валют относительно рубля
        get_currency_rate()

    ## _______________________________________________________ выбор платформ(-ы) для парсинга вакансий
    while True:
        platform_query: str = input(f'\n{YELLOW}Выберите платформу(-ы) данных для запроса:{NONCOLOR}\n'
                                    f'{GREEN}1{NONCOLOR} - HeadHunter\n'
                                    f'{GREEN}2{NONCOLOR} - SuperJob\n'
                                    f'{GREEN}3{NONCOLOR} - HeadHunter + SuperJob\n'
                                    f'{GREEN}0{NONCOLOR} - прервать работу\n')

        hh_api = HeadHunterAPI()
        sj_api = SuperJobAPI()

        # word_query: str = input('Введите слово, по которому будет происходить '
        #                         'поиск в вакансиях:\n')
        word_query: str = 'python'

        dir_file = DATA_BASE_PATH
        json_saver = JSONSaver(dir_file)

        if platform_query == '0':
            print("Не больно то и хотелось тебе помогать.")
            break

        elif platform_query not in ('1', '2', '3'):
            print(f'{RED}Неправильно указана команда{NONCOLOR}')
            continue

        elif platform_query in ('1', '2', '3'):
            vacancies: list = [0,
                               hh_api.get_filtered_vacancies(word_query),
                               sj_api.get_filtered_vacancies(word_query),
                               hh_api.get_filtered_vacancies(word_query) + sj_api.get_filtered_vacancies(word_query)
                               ][int(platform_query)]

            ## запись базы данных в json файл
            json_saver.write_vacancies(vacancies)

            ## чтение базы данных
            bd: list = json_saver.read_vacancies()

            print(f"Подобрано {BLUE}{len(bd)}{NONCOLOR} вакансий\n")

            ## ____________________________________________________________________ выбор задачи
            flag = True
            while flag:
                flag = False

                task_query: str = input(f'{YELLOW}Введите номер задачи:{NONCOLOR}\n'
                                        f'{GREEN}1{NONCOLOR} - вывести список вакансий по убыванию зарплаты\n'
                                        f'{GREEN}2{NONCOLOR} - вывести список вакансий по возрастанию зарплаты\n'
                                        f'{GREEN}3{NONCOLOR} - вывести список вакансий, с фильтрацией по названию\n'
                                        f'{GREEN}4{NONCOLOR} - вывести список вакансий, с фильтрацией по городу\n'
                                        f'{GREEN}0{NONCOLOR} - прервать работу\n')

                if task_query == '0':
                    break

                ## __________________________________________ выбор количества вакансий для сортировки
                elif task_query in ('1', '2'):
                    vn = input(f"\nВы можете указать кол-во вакансий, для вывода.\n"
                               f"Нажмите {GREEN}Enter{NONCOLOR},"
                               f"если хотите пропустить этот пункт\n")

                    vacancy_number = int(vn) if bool(vn) else 0

                    if task_query == '1':
                        output_sorted_vacancies(bd, vacancy_number)

                    elif task_query == '2':
                        salary_filter_query = input(
                            f'\n{YELLOW}Выводить вакансии с неуказанной зарплатой (да)?{NONCOLOR}\n')

                        if salary_filter_query.lower() in ('да', 'yes'):
                            output_sorted_vacancies(bd, vacancy_number, False)
                        else:
                            output_sorted_vacancies(bd, vacancy_number, False, True)

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

                    search_word = input(f'\n{YELLOW}Выберите город:{NONCOLOR}\n').lower()
                    output_filtered_vacancies(bd, search_word, 2)

                else:
                    print(f'{RED}Неправильно указана команда{NONCOLOR}\n')
                    flag = True

        ## __________________________________________________ замыкание скрипта в основном цикле While
        action = input(f"\n{YELLOW}Хотите продолжить работу с программой (да) ?:{NONCOLOR}\n"
                       "[Нажмите Enter, чтобы закончить]\n")

        if action in ('да', 'yes'):
            continue
        else:
            break
