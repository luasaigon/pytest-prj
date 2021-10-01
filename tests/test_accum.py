import pytest
from stuff.accum import Accumlator

def test_accumulator_init():
    accum = Accumlator()
    assert accum.count == 0

def test_accumulator_add_one():
    accum = Accumlator()
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three():
    accum = Accumlator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_readonly():
    accum = Accumlator()
    with pytest.raises(AttributeError,match=r"can't set attribute"):
        accum.count= 10