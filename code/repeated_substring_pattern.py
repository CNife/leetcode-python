from leetcode import test


def repeated_substring_pattern(s: str) -> bool:
    return len(s) >= 2 and s in (s * 2)[1:-1]


# noinspection SpellCheckingInspection
test(
    repeated_substring_pattern,
    [
        ("abab", True),
        ("aba", False),
        ("abcabcabcabc", True),
    ],
)
