from tqdm.auto import tqdm


def main(a: int, b: int):
    print(gcd(a, b))


def gcd(a: int, b: int) -> int:
    assert a >= 0, "a must be positive or zero"
    assert b >= 0, "b must be positive or zero"
    assert type(a) is int, "a must be an integer"
    assert type(b) is int, "b must be an integer"

    low, high = min(a, b), max(a, b)

    gcd = 0

    for div in tqdm(range(low, 1, -1)):
        if (low % div == 0) and (high % div == 0):
            if gcd < div:
                gcd = div

    return gcd
