"""The median from sheet 08."""


def median(xs):
    """Return the middle value of the numbers in xs, without changing xs.

    For an even number of items, the mean of the two middle ones.
    xs must not be empty.
    """
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
