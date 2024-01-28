from src.vacancy import Vacancy


def output_sorted_vacancies(data: list[Vacancy], vacancy_number: int = 0,
                            sorting=True, salary_zero_filter=False):
    """
    Выводит отсортированный лист вакансий.
    :param data: список вакансий
    :param vacancy_number: количество вакансий для вывода
    :param sorting: по убыванию / по возрастанию
    :param salary_zero_filter: фильтр на вакансии с не указанной зарплатой
    :return: None
    """

    n = len(data) if vacancy_number == 0 else vacancy_number

    if sorting:
        for i in sorted(data, reverse=sorting)[:n]:
            print(i)
            print('-' * 60)
    else:
        if salary_zero_filter:
            filtered_data: list[Vacancy] = filter(lambda v: v > 0, data)
            for i in sorted(filtered_data, reverse=sorting)[:n]:
                print(i)
                print('-' * 60)
        else:
            for i in sorted(data, reverse=sorting)[:n]:
                print(i)
                print('-' * 60)


def output_filtered_vacancies(data: list[Vacancy], search_word: str, key=1):
    """
    Выводит отяильтрованный список вакансий.
    :param data: список вакансий
    :param search_word: слово для поиска
    :param key: поиск по вакансиям / городам
    :return: None
    """

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
        STR_CS1 = 'Нет ни одной вакансии, содержащей такое слово в названии.'
        STR_CS2 = 'Неправильно указан город. Рекомендуем посмотреть статистику вакансий по городам.'
        print((0, STR_CS1, STR_CS2)[key])
