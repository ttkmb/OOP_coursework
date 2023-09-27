class vacancy:
    """
    Класс для представления вакансии.
    Имеет следующие поля: название вакансии, ссылка на вакансию, зарплата, валюта, описание
    """
    def __init__(self, vacancy_name: str, url: str, salary: str, salary_currency: str, description: str, expirience):
        self.vacancy_name = vacancy_name
        self.url = url
        self.salary = salary
        self.salary_currency = salary_currency
        self.description = description
        self.experience = expirience

    def __eq__(self, other):
        if isinstance(other, vacancy):
            return self.salary == other.salary
        raise TypeError('Невозможно сравнить объекты разных типов.')

    def __gt__(self, other):
        if isinstance(other, vacancy):
            return self.salary > other.salary
        raise TypeError('Невозможно сравнить объекты разных типов.')

    def __lt__(self, other):
        if isinstance(other, vacancy):
            return self.salary < other.salary
        raise TypeError('Невозможно сравнить объекты разных типов.')

    def __ge__(self, other):
        if isinstance(other, vacancy):
            return self.salary >= other.salary
        raise TypeError('Невозможно сравнить объекты разных типов.')

    def __le__(self, other):
        if isinstance(other, vacancy):
            return self.salary <= other.salary
        raise TypeError('Невозможно сравнить объекты разных типов.')


    def __str__(self):
        return (f'\nНазвание вакансии: {self.vacancy_name}\n'
                f'Cсылка на вакансию: {self.url}\n'
                f'Зарплата: {self.salary} {self.salary_currency}\n'
                f'Описание: {self.description}\n'
                f'Опыт работы: {self.experience}')


    def to_dict(self):
        return {
            'vacancy_name': self.vacancy_name,
            'link': self.url,
            'salary': self.salary,
            'salary_currency': self.salary_currency,
            'description': self.description,
            'experience': self.experience
        }