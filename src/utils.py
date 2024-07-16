import json
import logging
import os
import re
from collections import Counter
from typing import Any, Dict, List, Union

import pandas as pd

from src.config import LOG_LEVEL
from src.paths import get_project_root

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def get_operations_info(path: str) -> Union[List[Dict[str, Any]], List[Any]]:
    """Takes as input a path to a JSON, CSV, or XLSX file and returns a list of dictionaries with data about
    financial transactions."""
    extension = path.split('.')[-1].lower()

    try:
        if extension == 'json':
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                logger.info(f'Operations have been successfully loaded from {path}')
                return data
            logger.warning(f"The data in {path} is not in the expected format. Expected a list of dictionaries.")
            return []
        elif extension == 'csv':
            data = pd.read_csv(path, delimiter=';')
            result = data.to_dict(orient='records')
            logger.info(f"Operations have been successfully loaded from {path}")
            return [dict(item) for item in result]  # Ensure the result is a list of dictionaries
        elif extension == 'xlsx':
            data = pd.read_excel(path)
            result = data.to_dict(orient='records')
            logger.info(f"Operations have been successfully loaded from {path}")
            return [dict(item) for item in result]  # Ensure the result is a list of dictionaries
        else:
            logger.warning(f'{extension} file is not supported. An empty list will be returned.')
            return []
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"JSON decode error in file: {path}")
        return []
    except pd.errors.EmptyDataError:
        logger.error(f"No data found in file: {path}")
        return []
    except Exception as ex:
        logger.error(f"An error has occurred: {ex}")
        return []


def find_operations(operations: list[dict], query: str) -> list[dict]:
    """
    Returns a list of dictionaries that have the given string in tier description
    """
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return [op for op in operations if op.get('description') and pattern.search(op['description'])]


def get_operation_counts(operations: list[dict], categories: list[str]) -> dict:
    """
    Returns a dictionary where the keys are the category names and the values are the number of transactions in each
    category
    """
    # counted = Counter(op.get('description') for op in operations if op.get('description'))
    # return dict(counted)
    counted = Counter()

    for op in operations:
        description = op.get("description")
        if description and description in categories:
            counted[description] += 1

    return dict(counted)
