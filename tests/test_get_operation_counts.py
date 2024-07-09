from src.utils import get_operation_counts


def test_get_operation_counts():
    operations = [
        {
            "id": 1,
            "description": "01"
        },
        {
            "id": 2,
            "description": "02"
        },
        {
            "id": 3,
            "description": "01"
        }
    ]
    expected = {
        "01": 2,
        "02": 1
    }
    result = get_operation_counts(operations)
    assert result == expected
