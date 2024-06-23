import os.path
from unittest.mock import patch

from src.utils import get_operations_info


def test_get_operations_info_basic(operations_info, create_test_file_success):
    # filename = "test_operations.json"
    # filepath = os.path.join('docs', filename)
    filepath = create_test_file_success

    assert get_operations_info(filepath) == operations_info
    os.remove(filepath)


def test_get_operations_info_invalid_json(create_invalid_test_file):
    # filename = "test_operations_invalid_encoding.json"
    # filepath = os.path.join("docs", filename)
    filepath = create_invalid_test_file

    assert get_operations_info(filepath) == []
    os.remove(filepath)


def test_get_operations_info_empty(create_empty_test_file):
    filepath = create_empty_test_file

    assert get_operations_info(filepath) == []
    os.remove(filepath)


def test_get_operations_info_file_not_found():
    path = 'fake_path/operations.json'
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = get_operations_info(path)
        assert result == []
