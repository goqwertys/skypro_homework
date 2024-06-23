import pytest
from src.external_api import get_operation_amount
from unittest.mock import Mock
from unittest.mock import patch


def test_get_operation_amount_rub(operations_info):
    operation = operations_info[0]
    assert get_operation_amount(operation) == 31957.58


@patch('requests.get')
def test_get_operation_amount_eur(mock_get, operations_info):
    operation = operations_info[1]
    mock_get.return_value.json.return_value = {
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
    assert get_operation_amount(operation) == 724703.41
    mock_get.assert_called_once()
