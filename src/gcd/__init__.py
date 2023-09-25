from typing import Literal, Any, Optional

import numpy as np


def main(a: int, b: int):
    print(gcd(a, b))


def gcd(a: int, b: int) -> int:
    """Algorithm to calculate greatest common divisor of two integers"""

    if type(a) is not int or type(b) is not int:
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be ≥ 0")

    low, high = min(a, b), max(a, b)

    _gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if _gcd < div:
                _gcd = div
        div -= 1

    return _gcd


def gcd_euclidean(a: int, b: int):
    # Adapted from https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
    if a == 0:
        return b
    return gcd_euclidean(b % a, a)


def gcd_optimized(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers"""

    if type(a) is not int or type(b) is not int:
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be ≥ 0")

    low, high = min(a, b), max(a, b)

    _gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if _gcd < div:
                _gcd = div
        div -= 1
    return _gcd


def gcd_numpy(a: np.int64, b: np.int64) -> int:
    """Algorithm to calculate greatest common divisor of two integers"""
    a, b = np.int64(a), np.int64(b)

    if type(a) is not np.int64 or type(b) is not np.int64:
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be ≥ 0")

    low, high = np.min([a, b]), np.max([a, b])

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
