import json


def get_operations_info(path: str) -> list[dict]:
    """Takes as input a path to a JSON file and returns a list of dictionaries with data about financial transactions"""
    try:
        with open(path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return data


