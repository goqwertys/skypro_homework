"""
Defining functions for masking data
"""


def mask_card(card_number: str) -> str:
    """Returns masked card number as string"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:5]} {card_number[5:7]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return ""


def mask_account(acc_number: str) -> str:
    """Returns masked account number as string"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        return ""
