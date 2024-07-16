from src.utils import get_operation_counts


def test_get_operation_counts(operations_info, operation_counts, operations_categories):
    result = get_operation_counts(operations_info, operations_categories)
    assert result == operation_counts
