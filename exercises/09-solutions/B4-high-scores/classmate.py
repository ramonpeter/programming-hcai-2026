def add_score(path, score):
    with open(path, "w", encoding="utf-8") as f:
        with open(path, encoding="utf-8") as g:
            scores = [int(line) for line in g]
        scores.append(score)
        scores.sort(reverse=True)
        for s in scores[:5]:
            f.write(f"{s}\n")


for s in [40, 75, 12]:
    add_score("scores.txt", s)
