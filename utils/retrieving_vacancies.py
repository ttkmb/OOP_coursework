from utils.apis import headhunter_api, superjob_api
from Vacancy.vacancy import vacancy

def hh_vacancies(skill_name, count_vacancies):
    """
    Извлекает вакансии из HeadHunterAPI на основе предоставленного названия вакансии.
    """
    hh = headhunter_api(skill_name, count_vacancies)
    vacancies = hh.get_vacancies()
    total_vacancies = []
    for item in vacancies:
        vacancy_name = item['name']
        url = item['alternate_url']
        salary = item['salary']['from'] if 'salary' in item and item['salary'] and 'from' in item['salary'] else 'Не указана'
        salary_currency = '' if salary == 'Не указана' else item['salary']['currency']
        description = item['snippet']['responsibility'] if item['snippet'] and 'responsibility' in item['snippet'] else 'Не указана'
        experience = item['experience']['name'] if item['experience'] and 'name' in item['experience'] else 'Без опыта'
        needed = vacancy(vacancy_name, url, salary, salary_currency, description, experience)
        total_vacancies.append(needed)
    return total_vacancies

def sj_vacancies(vacancy_name, count_vacancies):
    """
    Извлекает вакансии из SuperJobAPI на основе предоставленного названия вакансии.
    """
    sj = superjob_api(vacancy_name, count_vacancies)
    vacancies = sj.get_vacancies()
    total_vacancies = []
    for item in vacancies:
        for correct_item in item:
            vacancy_name = correct_item['profession']
            url = correct_item['link']
            salary = f"{correct_item['payment_from']} - {correct_item['payment_to']}" if correct_item['payment_from'] else 'Не указана'
            salary_currency = '' if salary == 'Не указана' else correct_item['currency']
            description = correct_item['candidat']
            experience = correct_item['experience']['title']
            needed = vacancy(vacancy_name, url, salary, salary_currency, description, experience)
            total_vacancies.append(needed)
    return total_vacancies

