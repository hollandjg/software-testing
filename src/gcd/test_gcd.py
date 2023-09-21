import pytest
from gcd import gcd


def test_smoke():
    assert type(gcd(1, 2)) is int
