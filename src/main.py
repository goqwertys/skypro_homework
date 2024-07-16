import logging
import os

from src.config import LOG_LEVEL
from src.external_api import get_operation_amount
from src.generators import filter_by_currency
from src.paths import get_project_root
from src.processing import filter_by_state, sort_by_date
from src.utils import find_operations, get_operations_info
from src.widget import mask_card_or_acc_string

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def greetings() -> None:
    message = "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    print(message)


def input_format() -> str | None:
    message = """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
    print(message)
    choice = int(input("Пользователь: "))
    if choice == 1:
        print("Программа: Для обработки выбран JSON-файл.\n")
        return os.path.join(get_project_root(), "data", "operations.json")
    if choice == 2:
        print("Программа: Для обработки выбран CSV-файл.\n")
        return os.path.join(get_project_root(), "data", "transactions.csv")
    if choice == 3:
        print("Программа: Для обработки выбран XLSX-файл.\n")
        return os.path.join(get_project_root(), "data", "transactions_excel.xlsx")
    return None


def get_status() -> str:
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


def get_options() -> tuple:
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


def print_element(el: dict) -> None:
    logger.info(f""" Printing {el}""")

    date = el.get("date", "")
    description = el.get("description", "")
    print(f"{date} {description}")

    from_account = el.get("from")
    to_account = el.get("to")

    if from_account and isinstance(from_account, str) and to_account and isinstance(to_account, str):
        print(f"{mask_card_or_acc_string(from_account)} -> {mask_card_or_acc_string(to_account)}")
    elif to_account and isinstance(to_account, str):
        print(mask_card_or_acc_string(to_account))
    else:
        print("Account information missing")

    amount = get_operation_amount(el)
    if amount is not None:
        print(f"Сумма: {round(amount, 2)}")
    else:
        print("Amount information missing")

    print()


def main() -> None:
    logger.info("Application started...")
    greetings()

    filepath = input_format()
    if filepath is None:
        logger.error("No valid file format selected.")
        return

    logger.info(f"Opening file from: {filepath}")

    status = get_status()
    logger.info(f"User input: status: {status}")
    transactions = get_operations_info(filepath)

    if not transactions:
        logger.error("No transactions found.")
        return

    logger.info(f"Operations loaded. contains {len(transactions)}")

    data = filter_by_state(transactions, status)
    if not data:
        logger.warning("No transactions match the given status.")
        return

    logger.info(f"Operations filtered by state {status}, now contains {len(data)} elements")

    # getting parameters
    is_sort_by_day, srt_reverse, only_rub, word = get_options()
    logger.info(f"Options: Sort by day:{is_sort_by_day}, rev:{srt_reverse}, Only RUB: {only_rub}, Search for: {word}")

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
    logger.info("Printing...")
    print()
    for tr in data:
        print_element(tr)
    logger.info("Application finished")


if __name__ == "__main__":
    main()
