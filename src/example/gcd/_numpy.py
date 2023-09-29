import numpy as np


def gcd_numpy(x: np.int64, y: np.int64) -> int:
    """Algorithm to calculate the greatest common divisor of two integers"""
    x, y = np.int64(x), np.int64(y)

    if type(x) is not np.int64 or type(y) is not np.int64:
        raise TypeError("x and y must be integers")
    if x < 0 or y < 0:
        raise ValueError("x and y must be ≥ 0")

    low, high = np.min([x, y]), np.max([x, y])

    _gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if _gcd < div:
                _gcd = div
        div -= 1

    return _gcd
