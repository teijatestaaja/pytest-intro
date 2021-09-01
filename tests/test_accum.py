import pytest
from stuff.accum import Accumulator

# --------
# Fixtures
# --------

@pytest.fixture
def accum():
    return Accumulator()

# --------------------------------------------------
# Testing a class with several test cases, using
# Arrange-Act-Assert pattern, ie. classic three-step
# pattern for functional test cases.
# --------------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match="can't set attribute"):
        accum.count = 10
