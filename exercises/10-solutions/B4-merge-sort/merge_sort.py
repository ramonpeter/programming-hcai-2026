import random
import time


def merge(a, b):
    """Return one sorted list with the items of sorted lists a and b."""
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result + a[i:] + b[j:]


def merge_sort(xs):
    """Return a new sorted list with the items of xs. xs is not changed."""
    if len(xs) <= 1:
        return xs[:]
    mid = len(xs) // 2
    return merge(merge_sort(xs[:mid]), merge_sort(xs[mid:]))


def check(f, trials=1000):
    """Return how many random lists f sorts differently from sorted, or changes."""
    failures = 0
    for _ in range(trials):
        xs = [random.randint(0, 50) for _ in range(random.randint(0, 20))]
        before = xs[:]
        if f(xs) != sorted(xs) or xs != before:
            failures += 1
    return failures


def depth(n):
    """Return how many times a list of n items is halved before pieces of one are left."""
    if n <= 1:
        return 0
    return 1 + depth((n + 1) // 2)


if __name__ == "__main__":
    print(merge([1, 4, 9], [2, 3, 10, 11]))     # [1, 2, 3, 4, 9, 10, 11]
    print(merge_sort([5, 2, 9, 1, 5, 6]))       # [1, 2, 5, 5, 6, 9]

    random.seed(1)
    print("failures:", check(merge_sort))       # 0

    print("depth for a million items:", depth(1_000_000))     # 20

    big = [random.random() for _ in range(100_000)]
    start = time.time()
    merge_sort(big)
    mine = time.time() - start
    start = time.time()
    sorted(big)
    theirs = time.time() - start
    print(f"100 000 items: merge_sort {mine:.2f} s, sorted {theirs:.3f} s")
