from datetime import datetime
from typing import List


def filter_by_state(input_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Returns filtered list of dicts if 'state' item contains state"""
    return [item for item in input_list if state in item.get("state")]


def sort_by_date(input_list: List[dict], rev=False) -> List[dict]:
    """Returns list of dicts sorted by 'date'"""
    return sorted(
        input_list, key=lambda x: datetime.fromisoformat(x.get("date")), reverse=rev
    )


def sort_by_price_in_cat(input_list: List[dict], cat: str | None = None) -> List[dict]:
    """Returns sorted list of dicts in specified category"""
    categories = [x.get("category", None) for x in input_list]
    if cat is None:
        list_for_sort = input_list
    elif cat in categories:
        list_for_sort = [x for x in input_list if x.get("category") == cat]
    else:
        raise ValueError("Wrong ")
    return sorted(list_for_sort, key=lambda x: x.get("price"))
