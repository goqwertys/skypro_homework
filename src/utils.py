import json
import logging
import os
from typing import Any, Dict, List

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


def get_operations_info(path: str) -> List[Dict[str, Any]]:
    """Takes as input a path to a JSON file
    and returns a list of dictionaries with data about financial transactions"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                logger.info(f"Operations have been successfully loaded from {path}")
                return data
            logger.warning(f"The data in {path} is not in the expected format. Expected a list of dictionaries.")
            return []
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"JSON decode error in file: {path}")
        return []
