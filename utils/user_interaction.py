from json_saver.json_saver import json_saver
from utils.retrieving_vacancies import hh_vacancies, sj_vacancies


def user_interaction():
    """
    Функция для обработки взаимодействия с пользователем.
    Данная функция позволяет пользователю выполнять различные действия, связанные с поиском и сохранением вакансий.
    Он предлагает пользователю ввести желаемое действие, а затем выполняет соответствующий блок кода.
    Пользователь может выбрать поиск вакансий на разных сайтах, просмотреть сохраненные вакансии,
    удалить вакансии или выйти из программы.
    """
    json_file = json_saver('../OOP_coursework/vacancies.json')
    json_file.create_file()
    while True:
        print(
            "Введите 1 если хотите искать вакансии на сайте HH.ru\n"
            "Введите 2 если хотите искать вакансии на сайте SuperJob.ru\n"
            "Введите 3 если хотите посмотреть сохранённые вакансии\n"
            "Введите 4 если хотите удалить запись\n"
            "Введите 5 для выхода")
        user_action = int(input())
        if user_action == 1:
            user_count_vacancies = int(input('Введите желаемое количество вакансий: '))
            user_word = input('Введите ключевые навыки: ')
            vacancies = hh_vacancies(user_word.lower(), user_count_vacancies)
            for item in vacancies:
                print(item)
                print('Сохранить вакансию?')
                user_save_action = int(input('1 - Да\n'
                                             '2 - Нет\n'
                                             '3 - Отмена\n'))
                if user_save_action == 1:
                    json_file.add_vacancy(item)
                    print('Сохранение прошло успешно')
                elif user_save_action == 2:
                    continue
                elif user_save_action == 3:
                    break
        elif user_action == 2:
                user_count_vacancies = int(input('Введите желаемое количество вакансий: '))
                user_word = input('Введите ключевые навыки: ')
                vacancies = sj_vacancies(user_word.lower(), user_count_vacancies)
                for item in vacancies:
                    print(item)
                    print('Сохранить вакансию?')
                    user_save_action = int(input('1 - Да\n'
                                             '2 - Нет\n'
                                             '3 - Отмена\n'))
                    if user_save_action == 1:
                        json_file.add_vacancy(item)
                        print('Сохранение прошло успешно')
                    elif user_save_action == 2:
                        continue
                    elif user_save_action == 3:
                        break
        elif user_action == 3:
            user_input = int(input('Введите 1 если хотите увидеть все сохраненные вакансии\n'
                               'Введите 2 если хотите увидеть сохраненную вакансии, по уровню зарплаты\n'))
            if user_input == 1:
                vacancies = json_file.load_vacancies()
                print(vacancies)
            elif user_input == 2:
                user_salary_input = input('Введите уровень зарплаты: ')
                user_salary_currency_input = str(input('Введите вариант валюты: '))
                vacancies = json_file.get_vacancies_by_salary(user_salary_input.lower(), user_salary_currency_input.lower())
                for vacancy in vacancies:
                    print(vacancy)
        elif user_action == 4:
            user_choose_input = int(input('Введите 1 если хотите удалить конкретную вакансию\n'
                                     'Введите 2 если хотите удалить все вакансии\n'))
            if user_choose_input == 1:
                user_delete_input = input('Введите название вакансии, которую хотите удалить: ')
                if json_file.delete_vacancy(user_delete_input):
                    print(f'Вакансия {user_delete_input} удалена успешно')
            elif user_choose_input == 2:
                json_file.delete_all_vacancies()
                print('Все вакансии удалены')


        elif user_action == 5:
            print('Вы вышли из программы')
            break

print(user_interaction())



