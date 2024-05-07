"""
Defining functions for widgets
"""
from masks import mask_card, mask_account


def get_masked_card_from_str(string: str) -> str:
    """Returns masked """
    letters = [char for char in string if not char.isdigit()]
    nums = [char for char in string if char.isalpha()]
    if len(nums) == 16:
        return f"{letters}{mask_card(str(nums))}"
    elif len(nums) == 20:
        return f"{letters}{mask_account(str(nums))}"
    else:
        return ""
