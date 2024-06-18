import os.path

import pytest
from src.utils import get_operations_info


def test_get_operations_info_basic(operations_info):
    filename = "operations.json"
    filepath = os.path.join('docs', filename)

    assert get_operations_info(filepath) == operations_info
