# -*- coding: utf-8 -*-

import pytest
from learning_python.skeleton import fib

__author__ = "FVO123"
__copyright__ = "FVO123"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
