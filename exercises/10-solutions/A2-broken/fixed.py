def total(xs):
    """Return the sum of the numbers in xs."""
    if xs == []:
        return 0
    return xs[0] + total(xs[1:])


def halvings(n):
    """Return how often n can be halved, rounding down, before it reaches 1."""
    if n <= 1:
        return 0
    return 1 + halvings(n // 2)


def product(xs):
    """Return the product of the numbers in xs."""
    if xs == []:
        return 1
    return xs[0] * product(xs[1:])


if __name__ == "__main__":
    print(total([]), total([1, 2]), total([3, 1, 4]))          # 0 3 8
    print(halvings(8), halvings(6), halvings(1000))            # 3 2 9
    print(product([]), product([2, 3, 4]))                     # 1 24
