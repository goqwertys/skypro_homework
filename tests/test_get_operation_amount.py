import pytest
from src.external_api import get_operation_amount
from unittest.mock import Mock
from unittest.mock import patch


def test_get_operation_amount_rub(operations_info):
    operation = operations_info[0]
    assert get_operation_amount(operation) == 31957.58


@patch('requests.get')
def test_get_operation_amount_eur(mock_get, operations_info, transaction_request_data):
    operation = operations_info[1]
    mock_get.return_value.json.return_value = transaction_request_data
    assert get_operation_amount(operation) == 724703.41
    mock_get.assert_called_once()
