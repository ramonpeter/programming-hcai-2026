import temperature

for c in range(-10, 41, 10):
    print(f"{c:>4} C  {temperature.c_to_f(c):>5.1f} F")
