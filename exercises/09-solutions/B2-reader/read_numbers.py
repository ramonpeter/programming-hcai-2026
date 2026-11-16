def read_numbers(path):
    """Return the numbers in the file path, one per line.

    Blank lines are ignored. A line that is not a number is reported
    and skipped. A missing file is reported and gives an empty list.
    """
    numbers = []
    try:
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(f):
                text = line.strip()
                if text == "":
                    continue
                try:
                    numbers.append(float(text))
                except ValueError:
                    print(f"line {i + 1} skipped: {text}")
    except FileNotFoundError:
        print(f"no file called {path}")
    return numbers


if __name__ == "__main__":
    xs = read_numbers("measurements.txt")      # line 5 skipped: twelve
    print(xs)                   # 12.975
    print(read_numbers("missing.txt"))         # no file called missing.txt, then []
