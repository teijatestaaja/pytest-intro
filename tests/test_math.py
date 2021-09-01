import pytest

# -----------------------------------------------
# A basic test case that passes.
# -----------------------------------------------
@pytest.mark.smoke
def test_one_plus_one():
    assert 1 + 1 == 2

# -----------------------------------------------
# A test case that shows assertion introspection.
# -----------------------------------------------
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# -----------------------------------------------
# A test case that verifies an exception.
# -----------------------------------------------
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

# -----------------------------------------------
# A test case that is parameterized.
# -----------------------------------------------
products = [
    (2, 2, 4),
    (2, 0, 0),
    (2, -2, -4)
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product

# -----------------------------------------------
# A test case that is 
# -----------------------------------------------