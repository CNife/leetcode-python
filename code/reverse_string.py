def reverse_string(s: list[str]) -> None:
    l = len(s)
    for i in range(l // 2):
        s[i], s[l - i - 1] = s[l - i - 1], s[i]


if __name__ == "__main__":
    tests = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a", "b"], ["b", "a"]),
    ]
    for s, want in tests:
        reverse_string(s)
        assert s == want
