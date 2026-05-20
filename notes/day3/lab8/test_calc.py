# test_calc.py

from calc import find_sum, find_diff


def test_find_sum():

    actual = find_sum(10, 20)

    expected = 30

    assert actual == expected


def test_find_diff():

    actual = find_diff(50, 20)

    expected = 30

    assert actual == expected