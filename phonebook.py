# 55.  Создать телефонный справочник с возможностью
# импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик
# для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import os 

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    with open(filename, 'r+t', encoding='utf-8') as wrtbl:
       #l = wrtbl.readlines()
       lins_count = len(wrtbl.readlines())
       wrtbl.write(f"{lins_count + 1};{name};{phone}\n")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, 'r', encoding= 'utf-8') as data:
        resolt = data.read()
    return resolt    


def search_user(data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Вхождений не найдено'

def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding = 'utf-8') as data:
            data.write("")


INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
"""
DATASOURCE = 'phone.txt'

check_directory(DATASOURCE)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input()
        phone = input()
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
    elif mode == 3:
        earch = input('Введите строку для поиска: ')
        print(search_user(search, DATA_SOURCE))
        exit()