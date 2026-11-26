def flatten(xs):
    """Return a flat list of the items in the nested list xs, in order."""
    flat = []
    for item in xs:
        if isinstance(item, list):
            flat += flatten(item)
        else:
            flat.append(item)
    return flat


def deep_sum(xs):
    """Return the sum of the numbers in the nested list xs."""
    total = 0
    for item in xs:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
    return total


if __name__ == "__main__":
    nested = [1, [2, [3, 4]], [], 5]
    print(flatten(nested), deep_sum(nested))        # [1, 2, 3, 4, 5] 15
    print(flatten([]), deep_sum([]))                # [] 0
    print(flatten([[[]]]), deep_sum([[[]]]))        # [] 0
