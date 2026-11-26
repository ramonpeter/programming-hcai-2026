def keep(xs):
    if xs == []:
        return []
    if xs[0] % 2 == 0:
        return [xs[0]] + keep(xs[1:])
    return keep(xs[1:])

print(keep([3, 4, 7, 8, 10]))
