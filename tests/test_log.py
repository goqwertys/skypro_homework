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
    def foo():
        return 1 / 0

    with pytest.raises(ZeroDivisionError):
        foo()
    captured = capsys.readouterr()
    assert captured.out == "foo error: ZeroDivisionError. Inputs: (10), {}"
