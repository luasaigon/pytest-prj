# FIXTURE
import pytest

from stuff.accum import Accumlator


@pytest.fixture()
def accum():
    print("\n======== Get accum ==============")
    yield Accumlator()
    print("\nDone test")

@pytest.fixture()
def accum2():
    print("\n======== Get accum ==============")
    yield Accumlator()
    print("\nDone test")
