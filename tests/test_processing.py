import pytest
from src.processing import filter_by_state, sort_by_date, sort_by_price_in_cat, orders_info


def test_filter_by_state_default(prefiltered_data, filtered_data_default):
    assert filter_by_state(prefiltered_data) == filtered_data_default


def test_filter_by_state_canceled(prefiltered_data, filtered_data_canceled):
    assert filter_by_state(prefiltered_data, 'CANCELED') == filtered_data_canceled


def test_filter_by_state_empty():
    assert filter_by_state([]) == []


def test_sort_by_date(presorted_data, sorted_data):
    assert sort_by_date(presorted_data) == sorted_data


def test_sort_by_date_rev(presorted_data, sorted_data):
    assert sort_by_date(presorted_data, rev=True) == sorted_data[::-1]


def test_sort_by_date_empty():
    assert sort_by_date([]) == []


def test_sort_by_price_in_cat_default(shopping_list, shopping_list_sorted_default):
    assert sort_by_price_in_cat(shopping_list) == shopping_list_sorted_default


def test_sort_by_price_in_cat_specified(shopping_list, shopping_list_sorted_fruits):
    assert sort_by_price_in_cat(shopping_list, "fruit") == shopping_list_sorted_fruits


def test_sort_by_price_in_cat_incorrect_cat(shopping_list):
    with pytest.raises(ValueError, match="Invalid category"):
        sort_by_price_in_cat(shopping_list, "fish")


def test_sort_by_price_in_cat_empty():
    assert sort_by_price_in_cat([]) == []


def test_order_info(orders_list, order_info_result):
    assert orders_info(orders_list) == order_info_result


def test_order_info_empty():
    assert orders_info([]) == {}
