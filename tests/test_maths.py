# -*- coding: utf-8 -*-

from learning_python.maths import add
from learning_python.maths import subtract
from learning_python.maths import multiply


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(3, 1) == 2


def test_multiply():
    assert multiply(3, 2) == 6
