"""mystery and gcd again, printing each call indented by its depth, and what it returns."""


def mystery(n, depth=0):
    print("    " * depth + f"mystery({n})")
    if n == 0:
        result = 0
    else:
        result = n % 10 + mystery(n // 10, depth + 1)
    print("    " * depth + f"mystery({n}) returns {result}")
    return result


def gcd(a, b, depth=0):
    print("    " * depth + f"gcd({a}, {b})")
    if b == 0:
        result = a
    else:
        result = gcd(b, a % b, depth + 1)
    print("    " * depth + f"gcd({a}, {b}) returns {result}")
    return result


mystery(4071)
print()
gcd(48, 18)
print()
gcd(18, 48)
