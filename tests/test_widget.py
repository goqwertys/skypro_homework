import pytest
from src.widget import mask_card_or_acc_string, convert_iso_ddmmyyy


@pytest.mark.parametrize("string, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
])
def test_mask_card_or_acc_string(string, expected):
    assert mask_card_or_acc_string(string) == expected


@pytest.mark.parametrize("string", [
    "Maestro 159683786870",
    "5999414228426353",
    ""
])
def test_mask_card_or_acc_string_incorrect_number(string):
    with pytest.raises(ValueError, match="Incorrect card or acc number"):
        mask_card_or_acc_string(string)
