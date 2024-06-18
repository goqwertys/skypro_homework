import pytest


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
def operations_info():
    return [
        {'id': 441945886,
         'state': 'EXECUTED',
         'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
         'to': 'Счет 64686473678894779589'},
        {'id': 41428829,
         'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364',
         'operationAmount': {'amount': '8221.37',
                             'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации',
         'from': 'MasterCard 7158300734726758',
         'to': 'Счет 35383033474447895560'}
    ]
