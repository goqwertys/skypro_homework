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
## Использование
1.
    ```
    python src/main.py
    ```
    На данный момент основная локика описана в main.py
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