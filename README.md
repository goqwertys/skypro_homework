# WIDGET
## Установка:
1. клонируйте репозиторий
     ```
    git clone https://github.com/goqwertys/skypro_homework.git
    ```
2. запустите виртуальное окружение
    ```
   poetry install
    ```
3. Установите ключи API в соответствии с 
   ```
   .env.example
   ```
## Использование
1.
    ```
    python src/main.py
    ```
    На данный момент основная локика описана в main.py
## функционал:
### 1. Функции модуля ```masks.py```:
   #### ```mask_card()```:
   ```
   masked_card = mask_card("7000792289606361")
   print(masked_card)
   >>>7000 79** **** 6361
   ```
   #### ```mask_account()```:
   ```
   acc_mask = mask_account("73654108430135874305")
   print(acc_mask)
   >>>**4305
   ```
### 2. Функции модуля ``` widget.py```


   #### ```mask_card_or_acc_string()```:
   ```
   masked_data = mask_card_or_acc_string("Maestro 1596837868705199")
   print(masked_data)
   >>>Maestro 1596 83** **** 5199
   ```

   #### ```mask_card_or_acc_string()```:
   ```
   masked_data = mask_card_or_acc_string("Счет 64686473678894779589")
   print(masked_data)
   >>>Счет **9589
   ```
   #### ```convert_iso_ddmmyyy()```:
   ```
   converted_date = convert_iso_ddmmyyy("2024-03-16T08:00:00Z")
   print(converted_date)
   >>>16.03.2024
   ```
### 3. Функции модуля ```proccessing.py```

   #### ```filter_by_state()```: 
   ```
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
   >>>{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
   >>>{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
   ```
   #### ```sort_by_date()```:
   ```
   sort_test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    sorted_data = sort_by_date(sort_test)
    for item in sorted_data:
        print(item)
   ```
   #### ```sort_by_price_in_cat()```:
   ```
   sorted_in_category = sort_by_price_in_cat(list_of_dicts)
   for item in sorted_in_category:
      print(item)
   >>>{'name': 'potato', 'price': 1.2, 'category': 'vegetable', 'quantity': 30}
   >>>{'name': 'apple', 'price': 3.0, 'category': 'fruit', 'quantity': 5}
   >>>{'name': 'orange', 'price': 4.0, 'category': 'fruit', 'quantity': 10}
   >>>{'name': 'mango', 'price': 7.0, 'category': 'fruit', 'quantity': 3}
   ```
   #### ```orders_info()```:
   ```
   list_of_dicts = [
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
    orders_info_data = orders_info(list_of_dicts)
   >>>2020-06:
   >>>{'average_order_value': 206.25, 'order_count': 2}
   >>>2023-06:
   >>>{'average_order_value': 189.5, 'order_count': 1}
   ```
### 4. Функции модуля ```generators.py```

   #### исходный список словарей:
   ```
   transactions = (
        [
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
    )
   ```
   #### ```filter_by_currency()```:
   ```
   usd_transactions = filter_by_currency(transactions, "USD")

   for _ in range(2):
       print(next(usd_transactions)["id"])
   >>>939719570
   >>>142264268
   ```
   #### ```transaction_descriptions()```:
   ```
   descriptions = transaction_descriptions(transactions)
   for _ in range(5):
       print(next(descriptions))
   >>>Перевод организации
   >>>Перевод со счета на счет
   >>>Перевод со счета на счет
   >>>Перевод с карты на карту
   >>>Перевод организации
   ```
   #### ```card_number_generator()```:
   ```
   for card_number in card_number_generator(1, 5):
      print(card_number)
   >>>0000 0000 0000 0001
   >>>0000 0000 0000 0002
   >>>0000 0000 0000 0003
   >>>0000 0000 0000 0004
   >>>0000 0000 0000 0005
   ```
### 5. Декораторы модуля ```decorators.py```

   #### ```@log()```:
   Декоратор **@log()** логирует вызов функции. По умолчанию логи распечатываются в консоль. 
   Также декоратор имеет необязательный параметр **filename** который определяет путь к файлу, в который записываются логи.
   ##### Пример использования:
   ```
   @log()
   def foo(x: int, y: int):
      return x / y
   
   
   result = foo(1, 0)
   ```
   В лог будет записано:
   ```
   foo error: ZeroDivisionError. Inputs: (1, 0), {}
   ```
### 6. Функции модуля ```utils.py```

   #### ```get_operations_info(path: str)```:
   Функция поддерживает **json**, **csv** и **xlxs** форматы
   Возвращет содержимое файла **path** в виде:
   ```
   [
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
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
]
   ```
## Тестирование
Проект использует pytest для тестирования. Убедитесь, что вы установили все зависимости, прежде чем запускать тесты.
### Запуск тестов
для запуска тестов выполните следующую команду
~~~
pytest
~~~
### Параметризованные тесты
Тесты параметризованы с использованием pytest.mark.parametrize. Это позволяет легко добавлять новые тестовые случаи и упрощает поддержку тестов.
### Примеры тестов

```
import pytest
form src.masks import mask_card


@pytest.mark.parametrize("card_num, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("5000600050004000", "5000 60** **** 4000"),
    ("1234567809876543", "1234 56** **** 6543")
])
def test_mask_card_basic(card_num, expected):
    assert mask_card(card_num) == expected
```
### Тестирование на ошибки
Также включены тесты, проверяющие корректную обработку некорректных данных.
```
import pytest
from src.widget import mask_card_or_acc_string


@pytest.mark.parametrize("string", [
    "Maestro 159683786870",
    "Visa Gold AAAA414228426353",
    "Счет 353830334744478955"
])
def test_mask_card_or_acc_string_incorrect_number(string):
    with pytest.raises(ValueError):
        mask_card_or_acc_string(string)
```
## Лицензия
раздел дополняется