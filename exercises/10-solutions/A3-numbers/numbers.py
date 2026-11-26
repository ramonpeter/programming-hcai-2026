def power(x, n):
    """Return x to the power n, for a whole number n >= 0."""
    if n == 0:
        return 1
    return x * power(x, n - 1)


def to_binary(n):
    """Return the binary digits of the whole number n >= 0, as a string."""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


if __name__ == "__main__":
    print(power(2, 10), power(5, 0), power(1.5, 2))       # 1024 1 2.25
    print(to_binary(0), to_binary(6), to_binary(13))      # 0 110 1101
    print(bin(13))                                        # 0b1101

    for n in range(100):
        if "0b" + to_binary(n) != bin(n):
            print("disagree on", n)
    print("to_binary checked against bin for 0 to 99")
