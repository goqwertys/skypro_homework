import os

import pytest
import requests
from dotenv import load_dotenv

from src.external_api import get_operation_amount
from unittest.mock import Mock
from unittest.mock import patch


def test_get_operation_amount_rub(operations_info):
    operation = operations_info[0]
    assert get_operation_amount(operation) == 31957.58


@patch('requests.get')
def test_get_operation_amount_usd(mock_get, operations_info, transaction_request_data):
    operation = operations_info[1]
    mock_get.return_value.json.return_value = transaction_request_data
    assert get_operation_amount(operation) == 724703.41
    load_dotenv()
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    # f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37"
    headers = {"apikey": api_key}
    mock_get.assert_called_once_with(url, headers=headers)


def test_get_operation_amount_bad_response(transaction_request_data):
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Test exception")

        result = get_operation_amount(transaction_request_data)

        assert result == 0.0
        load_dotenv()
        api_key = os.getenv('EXCHANGE_RATES_API_KEY')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37"
        headers = {"apikey": api_key}
        mock_get.assert_called_once_with(url, headers=headers)
