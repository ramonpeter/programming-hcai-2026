import random
import statistics

from median import median
from lazy_median import lazy_median


def check(f, trials=1000):
    """Return how many of trials random lists f gets wrong.

    Wrong means an answer different from statistics.median,
    or a list that was changed.
    """
    failures = 0
    for _ in range(trials):
        xs = [random.randint(0, 20) for _ in range(random.randint(1, 10))]
        before = xs[:]
        if f(xs) != statistics.median(xs) or xs != before:
            failures += 1
    return failures


random.seed(1)
print(check(median), check(lazy_median))     # 0 434
