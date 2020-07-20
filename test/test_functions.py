"""
Created by Neel Gokhale at 2020-07-19
File test_functions.py from project Project_Calculator
Built using PyCharm

"""

import functions as f
import pytest


def test_sum():
    assert f.add(7, 3) == 10
    assert f.add(-1, -1) == -2
    assert f.add(-1, 1) == 0
    assert f.add(8.9, 9.1) == 18.0


def test_subtract():
    assert f.subtract(9, 3) == 6
    assert f.subtract(-1, -9) == 8
    assert f.subtract(-2, 2) == -4
    assert f.subtract(9, 8, in_order=False) == -1


def test_multiply():
    assert f.multiply(4, 5) == 20
    assert f.multiply(-5, 3) == -15
    assert f.multiply(-4, -4) == 16
    assert f.multiply(2.5, 2) == 5.0


def test_divide():
    assert f.divide(8, 4) == 2
    assert f.divide(-2, 2) == -1
    assert f.divide(-5, -2) == 2.5
    assert f.divide(2, 5, in_order=False) == 2.5
