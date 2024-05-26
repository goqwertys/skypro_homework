"""
Defining functions for widgets
"""

from src.masks import mask_account, mask_card


def mask_card_or_acc_string(input_string: str) -> str:
    """Returns masked acc or card in string"""
    # Check if sting is correct
    parts = input_string.split()
    if len(parts) < 2 or not parts[-1].isdigit():
        raise ValueError("Incorrect string")

    if input_string.split()[0] in {"Счёт", "Счет"}:
        return f"{input_string.split()[0]} {mask_account(input_string.split()[-1])}"
    else:
        return f"{" ".join(input_string.split()[:-1])} {mask_card(input_string.split()[-1])}"


def convert_iso_ddmmyyy(iso_input: str) -> str:
    """Accepts a ISO8601 string and returns string as dd.mm.yyyy"""
    date_part = iso_input.split(sep="T")[0]
    iso_list = date_part.split(sep="-")
    if len(iso_list) != 3:
        raise ValueError("Incorrect date part format")
    year, month, day = iso_list
    if not (len(year) == 4 and year.isdigit()):
        raise ValueError("Incorrect year")
    if not (len(month) == 2 and month.isdigit() and 1 <= int(month) <= 12):
        raise ValueError("Incorrect month")
    if not (len(day) == 2 and day.isdigit() and 1 <= int(day) <= 31):
        raise ValueError("Incorrect day")
    return f"{day}.{month}.{year}"
