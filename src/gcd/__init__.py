from typing import Literal, Any, Optional

import numpy as np


def main(a: int, b: int):
    print(gcd(a, b))


def gcd(x: int, y: int) -> int:
    """Algorithm to calculate the greatest common divisor of two integers"""

    if type(x) is not int or type(y) is not int:
        raise TypeError("x and y must be integers")
    if x < 0 or y < 0:
        raise ValueError("x and y must be ≥ 0")

    low, high = min(x, y), max(x, y)

    _gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if _gcd < div:
                _gcd = div
        div -= 1

    return _gcd


def gcd_euclidean(x: int, y: int):
    # Adapted from https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
    if x == 0:
        return y
    return gcd_euclidean(y % x, x)


def gcd_optimized(x: int, y: int) -> int:
    """Calculate greatest common divisor of two integers"""

    if type(x) is not int or type(y) is not int:
        raise TypeError("x and y must be integers")
    if x < 0 or y < 0:
        raise ValueError("x and y must be ≥ 0")

    low, high = min(x, y), max(x, y)

    _gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if _gcd < div:
                _gcd = div
        div -= 1
    return _gcd


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


def append(value: Any, the_list: Optional[list] = []):
    """
    Appends a value to a list, and if the list isn't given, return the value on a new list.

    :param value: the value to append to `list`
    :type value: Any

    :param the_list: the list to append to, defaults to an empty list
    :type the_list: list, optional
    """
    the_list.append(value)
    return the_list


def append_fixed(value: Any, the_list: Optional[list] = None):
    """
    Appends a value to a list, and if the list isn't given, return the value on a new list.

    :param value: the value to append to `list`
    :type value: Any

    :param the_list: the list to append to, defaults to an empty list
    :type the_list: list, optional
    """
    if the_list is None:
        the_list = []
    the_list.append(value)
    return the_list
