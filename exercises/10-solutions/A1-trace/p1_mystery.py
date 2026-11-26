def mystery(n):
    if n == 0:
        return 0
    return n % 10 + mystery(n // 10)

print(mystery(4071))
