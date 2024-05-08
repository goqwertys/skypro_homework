"""
Defining functions for widgets
"""
from masks import mask_card, mask_account


def mask_card_or_acc_sring(input_string: str) -> str:
    """Returns masked acc or card in string"""
    # Check if string is correct
    if not len(input_string.split()[-1]) in [16, 20] and input_string.split()[-1].isdigit():
        raise ValueError("Incorrect card or acc number")
    else:
        if input_string.split()[0] in {"Счёт", "Счет"}:
            return f"{input_string.split()[0]} {mask_account(input_string.split()[-1])}"
        else:
            return f"{" ".join(input_string.split()[:-1])} {mask_card(input_string.split()[-1])}"
