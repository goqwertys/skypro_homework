"""
Defining functions for widgets
"""

from src.masks import mask_account, mask_card


def mask_card_or_acc_sring(input_string: str) -> str:
    """Returns masked acc or card in string"""
    # Check if string is correct
    if (
        not len(input_string.split()[-1]) in [16, 20]
        and input_string.split()[-1].isdigit()
    ):
        raise ValueError("Incorrect card or acc number")
    else:
        if input_string.split()[0] in {"Счёт", "Счет"}:
            return f"{input_string.split()[0]} {mask_account(input_string.split()[-1])}"
        else:
            return f"{" ".join(input_string.split()[:-1])} {mask_card(input_string.split()[-1])}"


def convert_iso_ddmmyyy(iso_input: str) -> str:
    """Accepts a ISO8601 string and returns string as dd.mm.yyyy"""
    # ISO 8601: 2018-07-11T02:26:18.671407
    iso_list = iso_input.split(sep="T")[0].split(sep="-")
    if len(iso_list) != 3:
        raise ValueError("Incorrect date format")
    year, mouth, date = iso_list
    return f"{date}.{mouth}.{year}"
