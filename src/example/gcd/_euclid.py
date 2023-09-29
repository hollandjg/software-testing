def gcd_euclidean(x: int, y: int):
    # Adapted from https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
    if x == 0:
        return y
    return gcd_euclidean(y % x, x)
