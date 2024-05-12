from typing import List


def filter_by_state(input_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Returns filtered list of dicts if 'state' item contains state"""
    return [item for item in input_list if state in item.get("state")]
