"""
Defining functions for masking data
"""
import logging
import os

from paths import get_project_root
from config import LOG_LEVEL

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def mask_card(card_number: str) -> str:
    """Returns masked card number as string"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        raise ValueError("Incorrect card number")


def mask_account(acc_number: str) -> str:
    """Returns masked account number as string"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        raise ValueError("Incorrect account number")
