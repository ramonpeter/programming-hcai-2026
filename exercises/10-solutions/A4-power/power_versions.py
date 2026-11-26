"""Three ways to compute x to the power n, and what each costs."""


def power(x, n):
    """Return x to the power n, for a whole number n >= 0."""
    if n == 0:
        return 1
    return x * power(x, n - 1)


calls = []                  # the n of every call to fast_power, in order


def fast_power(x, n):
    """Return x to the power n, for a whole number n >= 0, by halving n."""
    calls.append(n)
    if n == 0:
        return 1
    half = fast_power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half


def power_loop(x, n):
    """Return x to the power n, for a whole number n >= 0."""
    result = 1
    for _ in range(n):
        result *= x
    return result


def fast_power_twice(x, n):
    """fast_power without the variable half: the smaller power is computed twice."""
    calls.append(n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_power_twice(x, n // 2) * fast_power_twice(x, n // 2)
    return x * fast_power_twice(x, n // 2) * fast_power_twice(x, n // 2)


if __name__ == "__main__":
    print(power(2, 900) == 2 ** 900)            # True
    try:
        power(2, 1000)
    except RecursionError as e:
        print("power(2, 1000)  RecursionError:", e)

    calls.clear()
    print(fast_power(2, 1000) == 2 ** 1000)     # True
    print(len(calls), "calls:", calls)          # 11 calls: 1000, 500, ..., 1, 0

    calls.clear()
    fast_power_twice(2, 1000)
    print("without half:", len(calls), "calls")  # 2047

    print(power_loop(2, 1000) == 2 ** 1000)     # True
