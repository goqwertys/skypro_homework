from typing import List


def filter_by_currency(input_list: List[dict], curr_code:str):
    return (d for d in input_list if d["operationAmount"]["currency"]["code"] == curr_code)


def transaction_descriptions(input_list: List[dict]):
    return (d["description"] for d in input_list)
