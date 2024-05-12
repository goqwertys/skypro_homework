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
