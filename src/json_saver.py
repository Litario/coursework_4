import json

from src.vacancy import Vacancy


class JSONSaver:
    d = [{1: 1, 2: 2, 3: 3}]

    def __init__(self, file_name):
        self.file_name = file_name

    def write_vacancies(self, vacancies: list) -> None:
        """
        Записывает лист вакансий в формате json в файл.
        :param vacancies: лист с вакансиями (экземпляр класса
        :return: None
        """

        with open(self.file_name, mode='w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_vacancies(self) -> list[Vacancy]:
        """
        Читает лист вакансий из файла json.
        :return: лист с объектами класса Vacancy
        """

        with open(self.file_name, mode='r', encoding='utf-8') as file:
            vacancies = json.load(file)

            # vacancies_list = vacancies

        vacancies_list = []
        for i in vacancies:
            vacancies_list.append(Vacancy(i['name'],
                                          i['experience'],
                                          i['salary_from'],
                                          i['salary_to'],
                                          i['salary_currency'],
                                          i['employer'],
                                          i['area'],
                                          i['schedule'],
                                          i['platform']
                                          )
                                  )

        return vacancies_list

    def del_vacancies(self):
        """Удаляет все данные из json файла"""
        with open(self.file_name, mode='w') as file:
            file.write('')
