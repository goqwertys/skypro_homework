import pytest
from src.external_api import get_operation_amount
from unittest.mock import Mock


def test_get_operation_amount_rub(operations_info):
    operation = operations_info[0]
    assert get_operation_amount(operation) == 31957.58
