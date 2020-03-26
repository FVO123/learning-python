# -*- coding: utf-8 -*-

from learning_python.maths import add
from learning_python.maths import subtract
from learning_python.maths import multiply
from learning_python.maths import divide
from learning_python.maths import maximum
from learning_python.maths import minimum


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(3, 1) == 2


def test_multiply():
    assert multiply(3, 2) == 6


def test_divide():
    assert divide(6, 2) == 3


def test_maximum():
    assert maximum([10, 20, 4, 5]) == 20


def test_minimum():
    assert minimum([10, 20, 4, 5]) == 4
