import os

from src.masks import mask_account, mask_card
from src.utils import get_operations_info
from src.widget import convert_iso_ddmmyyy, mask_card_or_acc_string
from src.processing import (
    filter_by_state,
    sort_by_date,
    sort_by_price_in_cat,
    orders_info,
)
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from src.external_api import get_operation_amount


def main() -> None:
    # MASK CARD
    print("Testing mask_card():")
    card_mask = mask_card("7000792289606361")
    print(card_mask)

    # MASK ACCOUNT
    print("Testing mask_account():")
    acc_mask = mask_account("73654108430135874305")
    print(acc_mask)

    strings_to_match = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "Счет 736541084301358743",
    ]
    for line in strings_to_match:
        try:
            masked_data = mask_card_or_acc_string(line)
            print(masked_data)
        except ValueError as e:
            print(f"An error occurred: {e}")

    dates = [
        "2024-03-16T08:00:00Z",
        "2024-01-17T08:00:00Z",
        "2025-12-18T08:00:00Z",
        "1999-11-21T08:00:00Z",
        "1998-09-24T08:00:00Z",
        "2023-01-14T08:00:00Z",
        "2022-02-24T08:00:00Z",
        "2022-02T08:00:00Z",
    ]
    print("Testing convert_iso_ddmmyyy():")
    for date in dates:
        try:
            converted_date = convert_iso_ddmmyyy(date)
            print(converted_date)
        except ValueError as e:
            print(f"An error occurred: {e}")

    # FILTER TEST
    filter_test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    filtered_data = filter_by_state(filter_test)
    print("filter_by_state() test\nfiltered by DEFAULT:")
    for item in filtered_data:
        print(item)
    print("filter_by_state() test\nfiltered by CANCELED:")
    filtered_data = filter_by_state(filter_test, state="CANCELED")
    for item in filtered_data:
        print(item)

    # SORT TEST
    print("sort_by_date() test:")
    sort_test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    sorted_data = sort_by_date(sort_test)
    for item in sorted_data:
        print(item)

    list_of_dicts = [
        {"name": "apple", "price": 3.0, "category": "fruit", "quantity": 5},
        {"name": "orange", "price": 4.0, "category": "fruit", "quantity": 10},
        {"name": "potato", "price": 1.2, "category": "vegetable", "quantity": 30},
        {"name": "mango", "price": 7.0, "category": "fruit", "quantity": 3},
    ]
    # TEST sort_by_price_in_cat() with no category
    print("Testing sort_by_price_in_cat() with with no category:")
    sorted_in_category = sort_by_price_in_cat(list_of_dicts)
    for item in sorted_in_category:
        print(item)
    # TEST sort_by_price_in_cat() with specified category
    print("Testing sort_by_price_in_cat() with specified category:")
    sorted_in_category = sort_by_price_in_cat(list_of_dicts, "fruit")
    for item in sorted_in_category:
        print(item)

    # List of dicts for testing:
    list_of_dicts = [
        {
            "id": 1507,
            "date": "2020-06-03T18:35:29.512364",
            "items": [
                {"name": "orange", "price": 3.2, "quantity": 15},
                {"name": "apple", "price": 2.5, "quantity": 35},
                {"name": "apple", "price": 2.5, "quantity": 35},
            ],
        },
        {
            "id": 1523,
            "date": "2020-06-30T02:08:58.425572",
            "items": [
                {"name": "orange", "price": 3.2, "quantity": 15},
                {"name": "potato", "price": 2.5, "quantity": 50},
                {"name": "mango", "price": 5.5, "quantity": 3},
            ],
        },
        {
            "id": 1243,
            "date": "2023-06-12T21:27:25.241689",
            "items": [
                {"name": "orange", "price": 3.2, "quantity": 15},
                {"name": "potato", "price": 2.5, "quantity": 50},
                {"name": "mango", "price": 5.5, "quantity": 3},
            ],
        },
    ]
    orders_info_data = orders_info(list_of_dicts)
    print("Testing orders_info():")
    for key, value in orders_info_data.items():
        print(f"{key}:\n{value}")

    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    print("filter_by_currency():")
    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(2):
        print(next(usd_transactions)["id"])
    print("transaction_descriptions():")
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)
    current_path = os.getcwd()
    project_path = os.path.abspath(os.path.join(current_path, ".."))
    filepath = os.path.join(project_path, "data", "test_operations.json")
    for dictionary in get_operations_info(filepath):
        for key, value in dictionary.items():
            print(f"{key} : {value}")
        print("#" * 16)

    print(
        get_operations_info(
            r"D:\Study\IT\SkyPro Homework\Develop\homework_dev\data\operations.json"
        )
    )

    print("get_operation_amount():")
    operations = get_operations_info(
        r"D:\Study\IT\SkyPro Homework\Develop\homework_dev\data\operations.json"
    )[:2]
    for op in operations:
        print(get_operation_amount(op))


if __name__ == "__main__":
    main()
