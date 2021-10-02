import pytest
from stuff.accum import Accumlator


@pytest.mark.accum
def test_accumulator_init(accum):
    assert accum.count == 0


@pytest.mark.accum
def test_accumulator_add_one(accum2):
    accum2.add()
    assert accum2.count == 1


@pytest.mark.accum
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accum
def test_accumulator_readonly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute"):
        accum.count = 10
