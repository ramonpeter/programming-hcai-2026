import random
random.seed(3)
a = random.randint(1, 6)
random.seed(3)
b = random.randint(1, 6)
print(a == b)
