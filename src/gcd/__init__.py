def main(a: int, b: int):
    print(gcd(a, b))


def gcd(a: int, b: int) -> int:
    assert a >= 0, "a must be positive or zero"
    assert b >= 0, "b must be positive or zero"
    assert type(a) is int, "a must be an integer"
    assert type(b) is int, "b must be an integer"

    low, high = min(a, b), max(a, b)

    gcd = 0

    div = low
    while div > 0:
        if (low % div == 0) and (high % div == 0):
            if gcd < div:
                gcd = div
        div -= 1

    return gcd
