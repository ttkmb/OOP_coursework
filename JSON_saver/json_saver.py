import json
import os
from abc import abstractmethod, ABC

class file_worker(ABC):
    """
    Абстрактный класс для работы с файлами
    """
    @abstractmethod
    def create_file(self):
        pass
    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary: str, salary_currency):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_name):
        pass

class json_saver(file_worker):
    def __init__(self, file_name):
        self.file_name = file_name

    def create_file(self):
        """
        Класс для работы с JSON файлом.
        Функционал: создание файла; добавление вакансии в файл;
        удаление вакансий из файла; получение вакансий по зарплате
        """
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False)
        else:
            if os.path.getsize(self.file_name) == 0:
                with open(self.file_name, 'w', encoding='utf-8') as file:
                    json.dump([], file, ensure_ascii=False)
    def add_vacancy(self, vacancy_data):
        data = []
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                for vacancy in data:
                    if str(vacancy['vacancy_name']) == str(vacancy_data):
                        print('Такая вакансия уже есть')
                        return
        except FileNotFoundError:
            raise f'Файл {self.file_name} не найден'
        data.append(vacancy_data.to_dict())
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies_by_salary(self, salary: str, salary_currency):
        vacancies_salary = []
        with open(self.file_name, 'r') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                try:
                    needed_salary = list(map(int, vacancy['salary'].split('-')))
                    if (needed_salary[0] <= int(salary) <= needed_salary[1] and vacancy['salary_currency'].lower() == salary_currency.lower()) or (int(salary) == int(vacancy['salary']) and salary_currency.lower() == vacancy['salary_currency'].lower()):
                        vacancies_salary.append(vacancy)
                except (ValueError, IndexError, TypeError, AttributeError):
                    continue
            if not vacancies_salary:
                print('Вакансии с такой зарплатой не найдены')
        for vacancy in vacancies_salary:
            print("Название вакансии:", vacancy['vacancy_name'])
            print("Ссылка на вакансию:", vacancy['link'])
            print("Зарплата:", vacancy['salary'])
            print("Валюта:", vacancy['salary_currency'])
            print("Описание:", vacancy['description'])
        return ""
    def delete_vacancy(self, vacancy_name):
        new_vacancies = []
        found_vacancy = False
        with open(self.file_name, 'r', encoding='utf-8') as file:
            vacancies = json.loads(file.read())
        if not vacancies:
            print('Файл пуст')
            return
        else:
            for vacancy in vacancies:
                if vacancy['vacancy_name'] != vacancy_name:
                    new_vacancies.append(vacancy)
                else:
                    found_vacancy = True
        if not found_vacancy:
            print('Такой вакансии в файле нет')
            return
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(new_vacancies, file, ensure_ascii=False)

    def delete_all_vacancies(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False)

    def load_vacancies(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                print("Название вакансии:", vacancy['vacancy_name'])
                print("Ссылка на вакансию:", vacancy['link'])
                print("Зарплата:", vacancy['salary'])
                print("Валюта:", vacancy['salary_currency'])
                print("Описание:", vacancy['description'], "\n")
