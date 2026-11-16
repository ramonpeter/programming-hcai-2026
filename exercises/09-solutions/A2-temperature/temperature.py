"""Convert temperatures between Celsius and Fahrenheit."""


def c_to_f(c):
    """Return c degrees Celsius in degrees Fahrenheit."""
    return c * 9 / 5 + 32


def f_to_c(f):
    """Return f degrees Fahrenheit in degrees Celsius."""
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    print(c_to_f(0), c_to_f(100), c_to_f(-40))     # 32.0 212.0 -40.0
    print(f_to_c(32), f_to_c(212), f_to_c(-40))    # 0.0 100.0 -40.0
    print(f_to_c(c_to_f(37)))                      # 37.0
