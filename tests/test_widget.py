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
    "Visa Gold AAAA414228426353",
    "Счет 353830334744478955"
])
def test_mask_card_or_acc_string_incorrect_number(string):
    with pytest.raises(ValueError):
        mask_card_or_acc_string(string)


@pytest.mark.parametrize("string", [
    "Maestro159683786870",
    "Maestro 159683786870 AA",
    "Maestro 159683786870AA",
    "159683786870"
])
def test_mask_card_or_acc_string_incorrect_string(string):
    with pytest.raises(ValueError, match="Incorrect string"):
        mask_card_or_acc_string(string)


@pytest.mark.parametrize("date, expected", [
    ("2024-03-16T08:00:00Z", "16.03.2024"),
    ("2024-01-17T08:00:00Z", "17.01.2024"),
    ("2025-12-18T08:00:00Z", "18.12.2025"),
    ("1999-11-21T08:00:00Z", "21.11.1999"),
    ("1998-09-24T08:00:00Z", "24.09.1998"),
    ("2023-01-14T08:00:00Z", "14.01.2023"),
    ("2022-02-24T08:00:00Z", "24.02.2022")
])
def test_convert_iso_ddmmyyy(date, expected):
    assert convert_iso_ddmmyyy(date) == expected


# ISO 8601: 2018-07-11T02:26:18.671407

def test_incorrect_date_part_format():
    with pytest.raises(ValueError, match="Incorrect date part format"):
        convert_iso_ddmmyyy("2018-07")


def test_incorrect_year():
    with pytest.raises(ValueError, match="Incorrect year"):
        convert_iso_ddmmyyy("18-07-11T02:26:18.671407")


def test_incorrect_month():
    with pytest.raises(ValueError, match="Incorrect month"):
        convert_iso_ddmmyyy("2018-13-11T02:26:18.671407")


def test_incorrect_day():
    with pytest.raises(ValueError, match="Incorrect day"):
        convert_iso_ddmmyyy("2018-07-32T02:26:18.671407")


def test_incomplete_date():
    with pytest.raises(ValueError, match="Incorrect date part format"):
        convert_iso_ddmmyyy("2018-07T02:26:18.671407")


def test_invalid_format():
    with pytest.raises(ValueError, match="Incorrect date part format"):
        convert_iso_ddmmyyy("invalid-date")
