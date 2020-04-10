# -*- coding: utf-8 -*-

import operator
import numpy

from learning_python.maths import add
from learning_python.maths import subtract
from learning_python.maths import multiply
from learning_python.maths import divide
from learning_python.maths import maximum
from learning_python.maths import minimum
from learning_python.maths import is_positive
from learning_python.maths import add_all
from learning_python.maths import sequential_numbers


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(3, 1) == 2


def test_multiply():
    assert multiply(3, 2) == 6


def test_divide():
    assert divide(6, 2) == 3


def test_maximum():
    assert maximum([10, 21, 4, 5]) == 21


def test_minimum():
    assert minimum([10, 20, 2, 5]) == 2


def test_is_positive_with_positive_number():
    assert operator.is_(True, is_positive(11))


def test_is_positive_with_negative_number():
    assert operator.is_(False, is_positive(-11))


def test_add_all():
    assert add_all(1, 2, 3, 4, 5, 6) == 21


def test_array_of_sequential_numbers():
    numpy.testing.assert_array_equal(sequential_numbers(72, 81), [72,
                                                                  73,
                                                                  74,
                                                                  75,
                                                                  76,
                                                                  77,
                                                                  78,
                                                                  79,
                                                                  80,
                                                                  81])
