import json
from typing import Any, Dict, List


def get_operations_info(path: str) -> List[Dict[str, Any]]:
    """Takes as input a path to a JSON file
    and returns a list of dictionaries with data about financial transactions"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list) and all(
                    isinstance(item, dict) for item in data
                ):
                    return data
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
