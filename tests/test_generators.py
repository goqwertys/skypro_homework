import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_usd(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_filter_by_currency_rub(transactions):
    rub_transactions = filter_by_currency(transactions, "RUB")
    assert next(rub_transactions)["id"] == 873106923
    assert next(rub_transactions)["id"] == 594226727


def test_filter_by_currency_no_match(transactions):
    with pytest.raises(StopIteration):
        gbp_transactions = filter_by_currency(transactions, "GBP")
        _ = next(gbp_transactions)["id"]


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"


def test_card_number_generator_1to5():
    cn_generator = card_number_generator(1, 5)
    assert next(cn_generator) == "0000 0000 0000 0001"
    assert next(cn_generator) == "0000 0000 0000 0002"
    assert next(cn_generator) == "0000 0000 0000 0003"


def test_card_number_generator_100to200():
    cn_generator = card_number_generator(100, 200)
    assert next(cn_generator) == "0000 0000 0000 0100"
    assert next(cn_generator) == "0000 0000 0000 0101"
    assert next(cn_generator) == "0000 0000 0000 0102"


def test_card_number_generator_invalid_numbers():
    with pytest.raises(ValueError, match="Incorrect start/end values"):
        cn_generator = card_number_generator(-1, 10)
        _ = next(cn_generator)
