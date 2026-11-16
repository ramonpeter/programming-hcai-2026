def read_scores(path):
    """Return the scores in path as ints, or [] if there is no file."""
    try:
        with open(path, encoding="utf-8") as f:
            return [int(line) for line in f]
    except FileNotFoundError:
        return []


def add_score(path, score):
    """Add score to the file path. Keep the five best, best first."""
    scores = read_scores(path)
    scores.append(score)
    scores.sort(reverse=True)
    with open(path, "w", encoding="utf-8") as f:
        for s in scores[:5]:
            f.write(f"{s}\n")


if __name__ == "__main__":
    for s in [40, 75, 12, 90, 75, 60, 8]:
        add_score("scores.txt", s)
    with open("scores.txt", encoding="utf-8") as f:
        print(f.read(), end="")       # 90 75 75 60 40, one per line
