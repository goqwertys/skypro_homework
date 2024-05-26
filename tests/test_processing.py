import pytest
from src.processing import filter_by_state


def test_filter_by_state_default(prefiltered_data, filtered_data_default):
    assert filter_by_state(prefiltered_data) == filtered_data_default


def test_filter_by_state_canceled(prefiltered_data, filtered_data_canceled):
    assert filter_by_state(prefiltered_data, 'CANCELED') == filtered_data_canceled


def test_filter_by_state_empty():
    assert filter_by_state([]) == []
