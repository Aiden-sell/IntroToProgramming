def get_count(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the string s."""
    vowels = set('aeiou')
    return sum(1 for ch in s if ch in vowels)


if __name__ == "__main__":
    samples = [
        "abracadabra",
        "hello world",
        "",
        "aeiou aeiou",
    ]
    for s in samples:
        print(repr(s), '->', get_count(s))
