import os.path

import pytest
from src.utils import get_operations_info


def test_get_operations_info_basic(operations_info):
    filename = "test_operations.json"
    filepath = os.path.join('docs', filename)

    assert get_operations_info(filepath) == operations_info


def test_get_operations_info_invalid_json():
    filename = "test_operations_invalid_encoding.json"
    filepath = os.path.join("docs", filename)

    assert get_operations_info(filepath) == []


def test_get_operations_info_empty():
    filename = 'test_operations_empty.json'
    filepath = os.path.join('docs', filename)

    assert get_operations_info(filepath) == []
