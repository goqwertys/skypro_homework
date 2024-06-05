from typing import List, Generator


def filter_by_currency(input_list: List[dict], curr_code:str):
    return (d for d in input_list if d["operationAmount"]["currency"]["code"] == curr_code)


def transaction_descriptions(input_list: List[dict]) -> Generator:
    return (d["description"] for d in input_list)


def card_number_generator(start: int = 0, end: int = 9999999999999999) -> Generator:
    number = start
    while number <= end:
        digits = f"{"0" * (16 - len(str(number)))}{number}"
        yield f"{digits[:4]} {digits[4:8]} {digits[8:12]} {digits[12:]}"
        number += 1
