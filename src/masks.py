"""
Defining functions for masking data
"""
import logging
import os

from src.paths import get_project_root
from src.config import LOG_LEVEL

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
        masked_card = f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
        logger.info(f"Masked card number: {masked_card}")
        return masked_card
    else:
        logger.error(f"Incorrect card number {card_number}")
        raise ValueError("Incorrect card number")


def mask_account(acc_number: str) -> str:
    """Returns masked account number as string"""
    if acc_number.isdigit() and len(acc_number) == 20:
        masked_acc = f"{'*' * 2}{acc_number[-4::]}"
        logger.info(f"Masked account number: {masked_acc}")
        return masked_acc
    else:
        logger.error(f"Incorrect account number: {acc_number}")
        raise ValueError("Incorrect account number")
