def count(ch, s):
    """Return how often the character ch appears in s."""
    if s == "":
        return 0
    if s[0] == ch:
        return 1 + count(ch, s[1:])
    return count(ch, s[1:])


def is_palindrome(s):
    """Return True if s reads the same backwards."""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def is_phrase_palindrome(text):
    """Like is_palindrome, ignoring spaces and capitals."""
    return is_palindrome(text.lower().replace(" ", ""))


if __name__ == "__main__":
    print(count("a", "banana"), count("z", "banana"), count("a", ""))     # 3 0 0
    for word in ["level", "noon", "v", "", "abca", "ab"]:
        print(repr(word), is_palindrome(word))
    print(is_phrase_palindrome("Never odd or even"))                       # True
    print(is_phrase_palindrome("Was it a car or a cat I saw"))             # True
