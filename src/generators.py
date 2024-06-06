from typing import List, Iterator


def filter_by_currency(input_list: List[dict], currency: str) -> Iterator:
    return (tr for tr in input_list if tr["operationAmount"]["currency"]["code"] == currency)
