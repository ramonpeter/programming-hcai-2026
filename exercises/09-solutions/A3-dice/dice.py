import random

random.seed(2026)
counts = {}
for _ in range(10_000):
    total = random.randint(1, 6) + random.randint(1, 6)
    counts[total] = counts.get(total, 0) + 1

for total in range(2, 13):
    print(f"{total:>2} {counts[total]:>5} " + "#" * (counts[total] // 100))
