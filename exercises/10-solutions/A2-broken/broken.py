"""The three functions from the sheet, as given, each called with an input that shows the bug."""


def total(xs):
    if xs == []:
        return 0
    xs[0] + total(xs[1:])


def halvings(n):
    if n == 1:
        return 0
    return 1 + halvings(n / 2)


def product(xs):
    if xs == []:
        return 0
    return xs[0] * product(xs[1:])


print("total([])     ", total([]))          # 0, looks fine
print("halvings(8)   ", halvings(8))        # 3, looks fine
print("product([2, 3, 4])", product([2, 3, 4]))   # 0, wrong

try:
    total([1, 2])
except TypeError as e:
    print("total([1, 2])  TypeError:", e)

try:
    halvings(6)
except RecursionError as e:
    print("halvings(6)    RecursionError:", e)
