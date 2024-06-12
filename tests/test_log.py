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
    def foo(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        foo(0)
    captured = capsys.readouterr()
    expected_output = "foo error: ZeroDivisionError. Inputs: (0,), {}\n"
    assert captured.out.rstrip() == expected_output.rstrip()
