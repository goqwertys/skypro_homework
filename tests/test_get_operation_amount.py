import os

import requests
from dotenv import load_dotenv

from src.external_api import get_operation_amount
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


def test_get_operation_amount_bad_response(operations_info):
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Test exception")

        result = get_operation_amount(operations_info[1])

        assert result == 0.0
        load_dotenv()
        api_key = os.getenv('EXCHANGE_RATES_API_KEY')
        url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37"
        headers = {"apikey": api_key}
        mock_get.assert_called_once_with(url, headers=headers)


def test_get_operation_amount_no_operation_amount():
    transaction = {}
    result = get_operation_amount(transaction)
    assert result == 0.0


def test_get_operation_amount_invalid_operation_amount():
    transaction = {
        "operationAmount": "invalid_data"
    }
    result = get_operation_amount(transaction)
    assert result == 0.0


def test_get_operation_amount_no_currency_code():
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {}
        }
    }
    result = get_operation_amount(transaction)
    assert result == 0.0


def test_get_operation_amount_no_amount():
    transaction = {
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    }
    result = get_operation_amount(transaction)
    assert result == 0.0
