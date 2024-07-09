import pytest

from src.utils import find_operations


def test_find_operations_no_match():
    operations = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "Перевод Y"
        }
    ]
    query = "Возврат"
    result = find_operations(operations, query)
    assert result == []


def test_find_operations_single_match():
    operations = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "Перевод Y"
        }
    ]
    query = "Оплата"
    result = find_operations(operations, query)
    expected = [
        {
            "id": 1,
            "description": "Оплата ABC"
        }
    ]
    assert result == expected


def test_find_operations_multiple_match():
    operations = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "Оплата Y"
        },
        {
            "id": 3,
            "description": "Перевод Y"
        }
    ]
    query = "Оплата"
    result = find_operations(operations, query)
    expected = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "Оплата Y"
        }
    ]
    assert result == expected


def test_find_operations_case_insensitive():
    operations = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "оплата XYZ"
        },
        {
            "id": 3,
            "description": "Возврат MNO"
        }
    ]
    query = "ОплАТА"
    result = find_operations(operations, query)
    expected = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "оплата XYZ"
        }
    ]
    assert result == expected


def test_find_operations_empty_query():
    operations = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "Перевод to XYZ"
        }
    ]
    query = ""
    result = find_operations(operations, query)
    expected = [
        {
            "id": 1,
            "description": "Оплата ABC"
        },
        {
            "id": 2,
            "description": "Перевод to XYZ"
        }
    ]
    assert result == expected


def test_find_operations_no_description_field():
    operations = [
        {
            "id": 1,
            "amount": "100"
        },
        {
            "id": 2, "amount": 200,
            "description": "Перевод XYZ"
        }
    ]
    query = "Перевод"
    result = find_operations(operations, query)
    expected = [
        {
            "id": 2, "amount": 200,
            "description": "Перевод XYZ"
        }
    ]
    assert result == expected


def test_find_operations_empty_operations_list():
    operations = []
    query = "Оплата"
    result = find_operations(operations, query)
    assert result == []
