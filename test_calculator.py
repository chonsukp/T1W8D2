import pytest

from calculator import add, subtract, division, convert_to_list

def test_basics():
    assert "hello" == "hello"

def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8
    assert add(0, -2) == -2

def test_subtract():
    assert subtract(7, 2)  == 5
    assert subtract(5, -7) == 12

def test_division():
    assert division(10, 2) == 5
    # assert division(2, 0) == 2 - This will throw error

def test_division_raise_exception():
    with pytest.raises(Exception):
        division(10, 0)

def test_conver():
    assert 5 in convert_to_list(3, 4, 5)
