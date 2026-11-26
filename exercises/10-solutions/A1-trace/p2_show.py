def show(n):
    if n > 0:
        print(n)
        show(n - 1)
        print(n)

show(2)
