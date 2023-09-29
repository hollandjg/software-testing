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
