import os.path
from tempfile import NamedTemporaryFile
from unittest.mock import patch

from src.utils import get_operations_info


def test_get_operations_info_json(operations_info, create_test_file_json):
    filepath = create_test_file_json
    assert get_operations_info(filepath) == operations_info
    os.remove(filepath)


def test_get_operations_info_invalid_json(create_invalid_test_file):
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


def test_get_operations_info_empty_csv():
    with NamedTemporaryFile(delete=False, suffix='.csv') as f:
        filepath = f.name
    result = get_operations_info(filepath)
    assert result == []
    os.remove(filepath)


def test_get_operations_info_xlsx(create_test_file_xlsx, data_table):
    filepath = create_test_file_xlsx
    result = get_operations_info(filepath)
    assert result == data_table
    os.remove(filepath)


def test_get_operations_info_unsupported_extension():
    path = 'unsupported_file.txt'
    result = get_operations_info(path)
    assert result == []


def test_get_operations_info_empty_xlsx():
    with NamedTemporaryFile(delete=False, suffix='.xlsx') as f:
        filepath = f.name
    result = get_operations_info(filepath)
    assert result == []
    os.remove(filepath)