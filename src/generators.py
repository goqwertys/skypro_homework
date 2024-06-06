from typing import List, Iterator


def filter_by_currency(input_list: List[dict], currency: str) -> Iterator:
    """Returns an iterator that yields, one by one, the transactions that specify the given currency"""
    return (tr for tr in input_list if tr["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(input_list: List[dict]) -> Iterator:
    pass
