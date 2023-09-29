import pytest
from example import gcd


def test_gcd_basis(gcd_fn=gcd):
    assert gcd_fn(24, 18) == 6

    with pytest.raises(TypeError):
        gcd_fn(float(24), 18)
    with pytest.raises(TypeError):
        gcd_fn(24, float(18))

    with pytest.raises(ValueError):
        gcd_fn(-24, 18)
    with pytest.raises(ValueError):
        gcd_fn(24, -18)

    assert gcd_fn(18, 24) == 6
    assert gcd_fn(33, 33) == 33
    assert gcd_fn(0, 0) == 0
    assert gcd_fn(0, 5) == 0
    assert gcd_fn(3, 7) == 1
    assert gcd_fn(3, 8) == 1
    assert gcd_fn(12, 4) == 4
    assert gcd_fn(12, 5) == 1
