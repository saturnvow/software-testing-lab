import pytest

from calculator import add, subtract, multiply, divide, power, mean


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_divide_with_invalid_type():
    with pytest.raises(TypeError):
        divide("10", 2)
    with pytest.raises(TypeError):
        divide(True, 2)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 0.5) == 2


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([10]) == 10


def test_mean_empty_list():
    with pytest.raises(ValueError):
        mean([])
