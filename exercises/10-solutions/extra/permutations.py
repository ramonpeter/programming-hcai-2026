def permutations(s):
    """Return a list of all the orderings of the characters of s."""
    if len(s) <= 1:
        return [s]
    result = []
    for i in range(len(s)):
        rest = s[:i] + s[i + 1:]
        for p in permutations(rest):
            result.append(s[i] + p)
    return result


if __name__ == "__main__":
    print(permutations("abc"))              # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(len(permutations("abcd")))        # 24
    print(len(permutations("abcdefgh")))    # 40320, which is 8!
