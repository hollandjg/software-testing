def main(a: int, b: int):
    print(gcd(a, b))


def gcd(a: int, b: int) -> int:
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if a < 0:
        raise ValueError("a must be ≥ 0")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if b < 0:
        raise ValueError("b must be ≥ 0")

    low, high = min(a, b), max(a, b)

    gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if gcd < div:
                gcd = div
        div -= 1

    return gcd
