def top_words(path, n):
    """Return the n most common words in path, as (count, word) pairs."""
    counts = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            for word in line.lower().split():
                word = word.strip('.,;:!?"()-')
                if word != "":
                    counts[word] = counts.get(word, 0) + 1
    pairs = [(c, w) for w, c in counts.items()]
    pairs.sort(reverse=True)
    return pairs[:n]


if __name__ == "__main__":
    for count, word in top_words("my_text.txt", 10):
        print(f"{count:>5}  {word}")
