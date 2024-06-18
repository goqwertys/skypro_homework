import pytest
import os
from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def foo(x, y):
        return x + y

    foo(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "foo ok\n"


def test_log_error_console(capsys):
    @log()
    def foo_test(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        foo_test(0)
    captured = capsys.readouterr()
    expected_output = "foo_test error: ZeroDivisionError. Inputs: (0,), {}\n"
    assert captured.out.rstrip() == expected_output.rstrip()


def test_log_success_file():
    log_file = "testlog.txt"
    file_path = os.path.join("docs", log_file)

    @log(filename=file_path)
    def foo_test(x, y):
        return x + y

    foo_test(3, 4)

    with open(file_path, "r") as f:
        logs = f.read()

    expected_output = "foo_test ok\n"
    assert logs == expected_output

    os.remove(file_path)


def test_log_error_file():
    log_file = "testlog.txt"
    file_path = os.path.join("docs", log_file)

    @log(filename=file_path)
    def foo_test(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        foo_test(1, 0)

    with open(file_path, 'r') as f:
        logs = f.read()

    # f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs} "
    assert logs == "foo_test error: ZeroDivisionError. Inputs: (1, 0), {}"

    os.remove(file_path)
