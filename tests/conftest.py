import json
# import os

import pandas as pd
import pytest
from tempfile import NamedTemporaryFile


@pytest.fixture
def prefiltered_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filtered_data_default():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def filtered_data_canceled():
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def presorted_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_data():
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.fixture
def shopping_list():
    return [
        {"name": "apple", "price": 3.0, "category": "fruit", "quantity": 5},
        {"name": "orange", "price": 4.0, "category": "fruit", "quantity": 10},
        {"name": "potato", "price": 1.2, "category": "vegetable", "quantity": 30},
        {"name": "mango", "price": 7.0, "category": "fruit", "quantity": 3}
    ]


@pytest.fixture
def shopping_list_sorted_default():
    return [
        {'name': 'potato', 'price': 1.2, 'category': 'vegetable', 'quantity': 30},
        {'name': 'apple', 'price': 3.0, 'category': 'fruit', 'quantity': 5},
        {'name': 'orange', 'price': 4.0, 'category': 'fruit', 'quantity': 10},
        {'name': 'mango', 'price': 7.0, 'category': 'fruit', 'quantity': 3}
    ]


@pytest.fixture
def shopping_list_sorted_fruits():
    return [
        {'name': 'apple', 'price': 3.0, 'category': 'fruit', 'quantity': 5},
        {'name': 'orange', 'price': 4.0, 'category': 'fruit', 'quantity': 10},
        {'name': 'mango', 'price': 7.0, 'category': 'fruit', 'quantity': 3}
    ]


@pytest.fixture
def orders_list():
    return [
        {"id": 1507, "date": "2020-06-03T18:35:29.512364", "items": [
            {"name": "orange", "price": 3.2, "quantity": 15},
            {"name": "apple", "price": 2.5, "quantity": 35},
            {"name": "apple", "price": 2.5, "quantity": 35}
        ]},
        {"id": 1523, "date": "2020-06-30T02:08:58.425572", "items": [
            {"name": "orange", "price": 3.2, "quantity": 15},
            {"name": "potato", "price": 2.5, "quantity": 50},
            {"name": "mango", "price": 5.5, "quantity": 3}
        ]},
        {"id": 1243, "date": "2023-06-12T21:27:25.241689", "items": [
            {"name": "orange", "price": 3.2, "quantity": 15},
            {"name": "potato", "price": 2.5, "quantity": 50},
            {"name": "mango", "price": 5.5, "quantity": 3}
        ]},
    ]


@pytest.fixture
def order_info_result():
    return {
        "2020-06": {'average_order_value': 206.25, 'order_count': 2},
        "2023-06": {'average_order_value': 189.5, 'order_count': 1}
    }


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def operations_info():
    return [
        {
            'id': 441945886,
            'state': 'EXECUTED',
            'date': '2019-08-26T10:50:58.294041',
            'operationAmount': {
                'amount': '31957.58',
                'currency':
                    {
                        'name': 'руб.',
                        'code': 'RUB'
                    }
            },
            'description': 'Перевод организации',
            'from': 'Maestro 1596837868705199',
            'to': 'Счет 64686473678894779589'
        },
        {
            'id': 41428829,
            'state': 'EXECUTED',
            'date': '2019-07-03T18:35:29.512364',
            'operationAmount':
                {
                    'amount': '8221.37',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод организации',
            'from': 'MasterCard 7158300734726758',
            'to': 'Счет 35383033474447895560'
        }
    ]


@pytest.fixture
def create_test_file_json(operations_info):
    with NamedTemporaryFile(delete=False, suffix='.json', mode='w', encoding='utf-8') as f:
        json.dump(operations_info, f)
        return f.name


@pytest.fixture
def create_invalid_test_file():
    with NamedTemporaryFile(delete=False, suffix='.json') as f:
        f.write(b'invalid json')
        return f.name


@pytest.fixture
def create_empty_test_file():
    with NamedTemporaryFile(delete=False, suffix='.json') as f:
        return f.name


@pytest.fixture
def create_test_file_csv():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount.amount": "31957.58",
            "operationAmount.currency.name": "руб.",
            "operationAmount.currency.code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount.amount": "8221.37",
            "operationAmount.currency.name": "USD",
            "operationAmount.currency.code": "USD",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    df = pd.DataFrame(data)
    with NamedTemporaryFile(delete=False, suffix='.csv', mode='w', newline='') as f:
        df.to_csv(f, sep=';', index=False)
        return f.name


@pytest.fixture
def create_test_file_xlsx():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount.amount": 31957.58,
            "operationAmount.currency.name": "руб.",
            "operationAmount.currency.code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount.amount": 8221.37,
            "operationAmount.currency.name": "USD",
            "operationAmount.currency.code": "USD",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    df = pd.DataFrame(data)
    with NamedTemporaryFile(delete=False, suffix='.xlsx') as f:
        df.to_excel(f, index=False)
        return f.name


@pytest.fixture
def data_table():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount.amount": 31957.58,
            "operationAmount.currency.name": "руб.",
            "operationAmount.currency.code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount.amount": 8221.37,
            "operationAmount.currency.name": "USD",
            "operationAmount.currency.code": "USD",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]


@pytest.fixture
def transaction_request_data():
    return {
        "date": "2018-02-22",
        "historical": "",
        "info": {
            "rate": 148.972231,
            "timestamp": 1519328414
        },
        "query": {
            "amount": 8221.37,
            "from": "USD",
            "to": "RUB"
        },
        "result": 724703.41,
        "success": True
    }


@pytest.fixture
def json_file():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    with NamedTemporaryFile(delete=False, suffix='.json') as f:
        json.dump(data, f)
        return f.name


@pytest.fixture
def csv_file():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount.amount": "31957.58",
            "operationAmount.currency.name": "руб.",
            "operationAmount.currency.code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    df = pd.DataFrame(data)
    with NamedTemporaryFile(delete=False, suffix='.csv', mode='w', newline='') as f:
        df.to_csv(f, sep=';', index=False)
        return f.name


def xlsx_file():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount.amount": "31957.58",
            "operationAmount.currency.name": "руб.",
            "operationAmount.currency.code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    df = pd.DataFrame(data)
    with NamedTemporaryFile(delete=False, suffix='.xlsx') as f:
        df.to_excel(f, index=False)
        return f.name
