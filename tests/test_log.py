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
