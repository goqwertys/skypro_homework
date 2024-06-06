from typing import List, Iterator, Generator


def filter_by_currency(transactions: List[dict], currency: str) -> Iterator:
    """Returns an iterator that yields, one by one, the transactions that specify the given currency"""
    return (tr for tr in transactions if tr["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(input_list: List[dict]) -> Iterator:
    """Returns a generator of description of each operation"""
    return (tr["description"] for tr in input_list)


def card_number_generator(start: int, end: int) -> Generator:
    """Generates card numbers in the format XXXX XXXX XXXX XXXX"""
    if 0 < start < int("9" * 16) and 0 < end < int("9" * 16) and end > start:
        num = start
        while num <= end:
            result = f"{"0" * (16 - len(str(num)))}{num}"
            yield " ".join([result[0:4], result[4:8], result[8:12], result[12:]])
            num += 1
