from example import gcd_euclidean
from example.gcd.test_reference import test_gcd_basis


def test_gcd_euclid():
    test_gcd_basis(gcd_euclidean)
