import pytest

from source import bonus_cash, operation_add_to_total, take_cash, operation_take_from_total, rich_tax


def test_bonus_cash():
    assert bonus_cash(500, 1) == 500
    assert bonus_cash(500, 3) == 515.0


def test_operation_add_to_total():
    assert operation_add_to_total(695, 1, 5_000) == [5000, 1]
    assert operation_add_to_total(0, 1, 5_000) == [5000, 1]
    assert operation_add_to_total(500, 1, 5_000) == [5500, 2]


def test_take_cash():
    assert take_cash(5_000) == 4925.0
    assert take_cash(100_000) == 99400
    assert take_cash(300) == 270
    assert take_cash(0) == -30


def test_operation_take_from_total():
    assert operation_take_from_total(300, 1, 10_000) == [9700, 2]
    assert operation_take_from_total(300, 1, 200) == [200, 1]
    assert operation_take_from_total(280, 1, 10_000) == [10000, 1]


def test_rich_tax():
    assert rich_tax(5_000_000) == 4500000.0
    assert rich_tax(6_000_000) == 5400000.0
    assert rich_tax(500) == 500


if __name__ == '__main__':
    pytest.main(['-vv'])
