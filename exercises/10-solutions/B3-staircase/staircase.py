calls = {"ways": 0, "ways_fast": 0}


def ways(n):
    """Return the number of ways to climb n steps, 1, 2 or 3 at a time."""
    calls["ways"] += 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways(n - 1) + ways(n - 2) + ways(n - 3)


memo = {}


def ways_fast(n):
    """Like ways, remembering every answer in memo."""
    calls["ways_fast"] += 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n not in memo:
        memo[n] = ways_fast(n - 1) + ways_fast(n - 2) + ways_fast(n - 3)
    return memo[n]


if __name__ == "__main__":
    print([ways(n) for n in range(8)])          # [1, 1, 2, 4, 7, 13, 24, 44]

    calls["ways"] = 0
    print(ways(25), calls["ways"], "calls")     # 2555757 9135460 calls

    print(ways_fast(25), calls["ways_fast"], "calls")   # 2555757 76 calls
    print(ways_fast(100))
