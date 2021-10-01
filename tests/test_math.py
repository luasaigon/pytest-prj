import pytest

def test_one_plus_one():
    assert 1+1==2

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

def test_divide_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        num =  1/0
    assert 'division' in str(excinfo.value)