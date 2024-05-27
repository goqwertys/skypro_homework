import pytest
from src.masks import mask_card, mask_account


# mask_count() TESTES
@pytest.mark.parametrize("card_num, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("5000600050004000", "5000 60** **** 4000"),
    ("1234567809876543", "1234 56** **** 6543")
])
def test_mask_card_basic(card_num, expected):
    assert mask_card(card_num) == expected


@pytest.mark.parametrize("card_mum", [
    "1111",
    "12341234123412340",
    "12345678",
    "AAAABBBCCCDDD"
])
def test_mask_card_incorrect_card_number(card_mum):
    with pytest.raises(ValueError, match="Incorrect card number"):
        mask_card(card_mum)


# mask_account() TESTES
@pytest.mark.parametrize("acc_number, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
    ("11111111111111111111", "**1111")
])
def test_mask_account(acc_number, expected):
    assert mask_account(acc_number) == expected


@pytest.mark.parametrize("acc_num", [
    "736541084301358743050",
    "AAAA4108430135874305",
    "",
])
def test_mask_account_incorrect_number(acc_num):
    with pytest.raises(ValueError, match="Incorrect account number"):
        mask_account(acc_num)
