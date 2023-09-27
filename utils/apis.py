import os
from abc import abstractmethod, ABC

import requests


class ApiWorker(ABC):
    """
    Абстрактный класс для работы с API
    """
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(ApiWorker):
    def __init__(self, vacancy_name, count_vacancies):
        self.vacancy_name = vacancy_name
        self.count_vacancies = count_vacancies
    """
    Возвращает список вакансий из API HH.ru на основе предоставленного названия вакансии.
    """
    def get_vacancies(self):
        pages = int(self.count_vacancies / 1)
        vacancies = []
        params = {
            'text': self.vacancy_name,
            'page': 0,
            'per_page': 1
        }
        for page in range(pages):
            params.update({'page': page})
            request = requests.get(f'https://api.hh.ru/vacancies', params=params)
            vacancies+=(request.json()['items'])
        return vacancies



class SuperJobAPI(ApiWorker):
    def __init__(self, vacancy_name, count_vacancies):
        self.vacancy_name = vacancy_name
        self.count_vacancies = count_vacancies
    """
    Возвращает список вакансий из API SuperJob.ru на основе предоставленного названия вакансии и количества вакансий, отображаемых на странице.
    """
    def get_vacancies(self):
        pages = int(self.count_vacancies / 1)
        api_key = os.getenv('X_Api_App_Id')  # Получаем значение переменной окружения
        headers = {'X-Api-App-Id': api_key}
        params = {
            'keyword': self.vacancy_name,
            'page': 0,
            'count': 1
        }
        vacancies = []
        for page in range(pages):
            params.update({'page': page})
            response = requests.get(f'https://api.superjob.ru/2.0/vacancies', params=params, headers=headers)
            vacancies.append(response.json()['objects'])
        return vacancies
