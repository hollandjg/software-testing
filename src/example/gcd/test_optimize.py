import pytest
from ._optimize import gcd_optimized


def test_gcd_optimized(gcd_fn=gcd_optimized):
    assert gcd_fn(24, 18) == 6

    with pytest.raises(ValueError):
        gcd_fn(24, -18)

    assert gcd_fn(18, 24) == 6
    assert gcd_fn(12, 5) == 1
