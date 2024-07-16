import logging
import os

from src.config import LOG_LEVEL
from src.external_api import get_operation_amount
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import mask_account, mask_card
from src.paths import get_project_root
from src.processing import filter_by_state, orders_info, sort_by_date, sort_by_price_in_cat
from src.utils import get_operations_info, find_operations
from src.widget import convert_iso_ddmmyyy, mask_card_or_acc_string

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


# def main() -> None:
#     logger.info("Application started...")
#     # MASK CARD
#     print("Testing mask_card():")
#     card_mask = mask_card("7000792289606361")
#     print(card_mask)
#
#     # MASK ACCOUNT
#     print("Testing mask_account():")
#     acc_mask = mask_account("73654108430135874305")
#     print(acc_mask)
#
#     strings_to_match = [
#         "Maestro 1596837868705199",
#         "Счет 64686473678894779589",
#         "MasterCard 7158300734726758",
#         "Счет 35383033474447895560",
#         "Visa Classic 6831982476737658",
#         "Visa Platinum 8990922113665229",
#         "Visa Gold 5999414228426353",
#         "Счет 73654108430135874305",
#         "Счет 736541084301358743",
#     ]
#     for line in strings_to_match:
#         try:
#             masked_data = mask_card_or_acc_string(line)
#             print(masked_data)
#         except ValueError as e:
#             print(f"An error occurred: {e}")
#
#     dates = [
#         "2024-03-16T08:00:00Z",
#         "2024-01-17T08:00:00Z",
#         "2025-12-18T08:00:00Z",
#         "1999-11-21T08:00:00Z",
#         "1998-09-24T08:00:00Z",
#         "2023-01-14T08:00:00Z",
#         "2022-02-24T08:00:00Z",
#         "2022-02T08:00:00Z",
#     ]
#     print("Testing convert_iso_ddmmyyy():")
#     for date in dates:
#         try:
#             converted_date = convert_iso_ddmmyyy(date)
#             print(converted_date)
#         except ValueError as e:
#             print(f"An error occurred: {e}")
#
#     # FILTER TEST
#     filter_test = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#     filtered_data = filter_by_state(filter_test)
#     print("filter_by_state() test\nfiltered by DEFAULT:")
#     for item in filtered_data:
#         print(item)
#     print("filter_by_state() test\nfiltered by CANCELED:")
#     filtered_data = filter_by_state(filter_test, state="CANCELED")
#     for item in filtered_data:
#         print(item)
#
#     # SORT TEST
#     print("sort_by_date() test:")
#     sort_test = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#     sorted_data = sort_by_date(sort_test)
#     for item in sorted_data:
#         print(item)
#
#     list_of_dicts = [
#         {"name": "apple", "price": 3.0, "category": "fruit", "quantity": 5},
#         {"name": "orange", "price": 4.0, "category": "fruit", "quantity": 10},
#         {"name": "potato", "price": 1.2, "category": "vegetable", "quantity": 30},
#         {"name": "mango", "price": 7.0, "category": "fruit", "quantity": 3},
#     ]
#     # TEST sort_by_price_in_cat() with no category
#     print("Testing sort_by_price_in_cat() with with no category:")
#     sorted_in_category = sort_by_price_in_cat(list_of_dicts)
#     for item in sorted_in_category:
#         print(item)
#     # TEST sort_by_price_in_cat() with specified category
#     print("Testing sort_by_price_in_cat() with specified category:")
#     sorted_in_category = sort_by_price_in_cat(list_of_dicts, "fruit")
#     for item in sorted_in_category:
#         print(item)
#
#     # List of dicts for testing:
#     list_of_dicts = [
#         {
#             "id": 1507,
#             "date": "2020-06-03T18:35:29.512364",
#             "items": [
#                 {"name": "orange", "price": 3.2, "quantity": 15},
#                 {"name": "apple", "price": 2.5, "quantity": 35},
#                 {"name": "apple", "price": 2.5, "quantity": 35},
#             ],
#         },
#         {
#             "id": 1523,
#             "date": "2020-06-30T02:08:58.425572",
#             "items": [
#                 {"name": "orange", "price": 3.2, "quantity": 15},
#                 {"name": "potato", "price": 2.5, "quantity": 50},
#                 {"name": "mango", "price": 5.5, "quantity": 3},
#             ],
#         },
#         {
#             "id": 1243,
#             "date": "2023-06-12T21:27:25.241689",
#             "items": [
#                 {"name": "orange", "price": 3.2, "quantity": 15},
#                 {"name": "potato", "price": 2.5, "quantity": 50},
#                 {"name": "mango", "price": 5.5, "quantity": 3},
#             ],
#         },
#     ]
#     orders_info_data = orders_info(list_of_dicts)
#     print("Testing orders_info():")
#     for key, value in orders_info_data.items():
#         print(f"{key}:\n{value}")
#
#     transactions = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {"name": "руб.", "code": "RUB"},
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160",
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229",
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {"name": "руб.", "code": "RUB"},
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657",
#         },
#     ]
#     print("filter_by_currency():")
#     usd_transactions = filter_by_currency(transactions, "USD")
#
#     for _ in range(2):
#         print(next(usd_transactions)["id"])
#     print("transaction_descriptions():")
#     descriptions = transaction_descriptions(transactions)
#     for _ in range(5):
#         print(next(descriptions))
#
#     for card_number in card_number_generator(1, 5):
#         print(card_number)
#     current_path = os.getcwd()
#     project_path = os.path.abspath(os.path.join(current_path, ".."))
#     filepath = os.path.join(project_path, "data", "test_operations.json")
#     for dictionary in get_operations_info(filepath):
#         for key, value in dictionary.items():
#             print(f"{key} : {value}")
#         print("#" * 16)
#
#     print("get_operations_info():")
#     print(
#         get_operations_info(
#             r"D:\Study\IT\SkyPro Homework\Develop\homework_dev\data\transactions_excel.xlsx"
#         )[:5]
#     )
#
#     print("get_operation_amount():")
#     operations = get_operations_info(
#         r"D:\Study\IT\SkyPro Homework\Develop\homework_dev\data\transactions_excel.xlsx"
#     )
#     print(get_operation_amount(operations[1]))
#     logger.info("Application finished")
# xlsx_list = [
#     {
#         'id': 650703.0,
#         'state': 'EXECUTED',
#         'date': '2023-09-05T11:30:32Z',
#         'amount': 16210.0,
#         'currency_name': 'Sol',
#         'currency_code': 'PEN',
#         'from': 'Счет 58803664561298323391',
#         'to': 'Счет 39745660563456619397',
#         'description': 'Перевод организации'
#     },
#     {
#         'id': 3598919.0,
#         'state': 'EXECUTED',
#         'date': '2020-12-06T23:00:58Z',
#         'amount': 29740.0,
#         'currency_name': 'Peso',
#         'currency_code': 'COP',
#         'from':'Discover 3172601889670065',
#         'to': 'Discover 0720428384694643',
#         'description': 'Перевод с карты на карту'},
#     {
#         'id': 593027.0,
#         'state': 'CANCELED',
#         'date': '2023-07-22T05:02:01Z',
#         'amount': 30368.0,
#         'currency_name': 'Shilling',
#         'currency_code': 'TZS',
#         'from': 'Visa 1959232722494097',
#         'to': 'Visa 6804119550473710',
#         'description': 'Перевод с карты на карту'
#     },
#     {
#         'id': 366176.0,
#         'state': 'EXECUTED',
#         'date': '2020-08-02T09:35:18Z',
#         'amount': 29482.0,
#         'currency_name': 'Rupiah',
#         'currency_code': 'IDR',
#         'from': 'Discover 0325955596714937',
#         'to': 'Visa 3820488829287420',
#         'description': 'Перевод с карты на карту'
#     },
#     {
#         'id': 5380041.0,
#         'state': 'CANCELED',
#         'date': '2021-02-01T11:54:58Z',
#         'amount': 23789.0,
#         'currency_name': 'Peso',
#         'currency_code': 'UYU',
#         'from': nan,
#         'to': 'Счет 23294994494356835683',
#         'description': 'Открытие вклада'
#     }]

def greetings():
    message = "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    print(message)


def input_format():
    message = """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
    print(message)
    choice = int(input("Пользователь: "))
    if choice == 1:
        return os.path.join(get_project_root(), "data", "operations.json")
    if choice == 2:
        return os.path.join(get_project_root(), "data", "transactions.csv")
    if choice == 3:
        return os.path.join(get_project_root(), "data", "transactions_excel.xlsx")
    return None


def get_status():
    message = """Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    print(message)
    while True:
        status = input("Пользователь: ")
        if status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
            print(f'Статус операции "{status}" недоступен.')
            print(message)
            continue
        else:
            return status.upper()


def get_options():
    print("Программа: Отсортировать по датам? Да/нет\n")
    user_input = input("Пользователь: ")
    if user_input == 'Да':
        is_sort_by_date = True
        print("Программа: Отсортировать по возрастанию или по убыванию?\n")
        user_input = input("Пользователь: ")
        if user_input.lower() == 'по убыванию':
            rev = True
        else:
            rev = False
    else:
        is_sort_by_date = False
        rev = None

    print("Программа: Выводить только рублевые тразакции? Да/Нет\n")
    user_input = input("Пользователь: ")
    if user_input.lower() == "да":
        is_rub_only = True
    else:
        is_rub_only = False

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    user_input = input("Пользователь: ")
    if user_input.lower() == "да":
        print("Программа: Введите слово\n")
        word = input("Пользователь:")
    else:
        word = None
    return is_sort_by_date, rev, is_rub_only, word


def print_element(el: dict):
    logger.info(f""" Printing {el}""")
    print(f"{el.get("date")} {el.get("description")}")
    if el.get("from") and isinstance(el.get("from"), str):
        print(f"{mask_card_or_acc_string(el.get("from"))} -> {mask_card_or_acc_string(el.get("to"))}")
    else:
        print(mask_card_or_acc_string(el.get("to")))
    print(f"Сумма: {round(get_operation_amount(el), 2)}")
    print()


def main():
    logger.info("Application started...")
    greetings()

    filepath = input_format()
    logger.info(f"Opening file from: {filepath}")
    status = get_status()
    logger.info(f"User input: status: {status}")
    transactions = get_operations_info(filepath)
    logger.info(f"Operations loaded. contains {len(transactions)}")
    data = filter_by_state(transactions, status)
    logger.info(f"Operations filtered by state {status}, now contains {len(data)} elements")

    # getting parameters
    is_sort_by_day, srt_reverse, only_rub, word = get_options()
    logger.info(f"Parameters: Sort by day:{is_sort_by_day}, reverse:{srt_reverse}, Only RUB: {only_rub}, Search: {word}")

    # processing data
    if is_sort_by_day:
        data = sort_by_date(data, rev=srt_reverse)
        logger.info(f"data has been sorted by date, now contains {len(data)} elements")

    # print("TESTING...")
    # for i in data:
    #     print_element(i)

    if word:
        data = find_operations(data, word)
        logger.info(f"data filtered by word:{word}, now contains {len(data)} elements")

    # print("TESTING...")
    # for i in data:
    #     print_element(i)

    if only_rub:
        data = list(filter_by_currency(data, "RUB"))
        logger.info(f"data filtered by currency:'RUB', now contains {len(list(data))} elements")

    # printing...
    logger.info(f"Printing...")
    print()
    for tr in data:
        print_element(tr)
    logger.info("Application finished")


if __name__ == "__main__":
    main()
