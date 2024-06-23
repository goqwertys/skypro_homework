import os
from typing import Dict, Any

import requests
from dotenv import load_dotenv


def get_operation_amount(transaction: Dict[str, Any]) -> float | None:
    """Returns the amount of given transaction in rubles. Converts it if currency is in other currency"""
    operation_amount = transaction.get("operationAmount")
    if not operation_amount or not isinstance(operation_amount, dict):
        return None

    amount = float(operation_amount.get("amount", 0.0))
    currency = operation_amount.get("currency", {}).get("code")

    if currency == "RUB":
        return amount

    load_dotenv()
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        result = data.get("result")
        if result is None:
            return None
        return float(result)

    except requests.RequestException as e:
        print(f"Error fetching exchange rate data: {e}")
        return 0.0  # Return 0.0 in case of any error
