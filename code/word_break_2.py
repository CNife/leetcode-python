import functools
from typing import List

from leetcode import test


def word_break(s: str, words: List[str]) -> List[str]:
    words = set(words)

    @functools.lru_cache(None)
    def dfs(start: int) -> List[str]:
        nonlocal s, words
        results = []
        if start == len(s):
            results.append("")
        for end in range(start + 1, len(s) + 1):
            left_part = s[start:end]
            if left_part in words:
                right_parts = dfs(end)
                for right_part in right_parts:
                    result = left_part
                    if len(right_part) > 0:
                        result += " " + right_part
                    results.append(result)
        return results

    return dfs(0)


# noinspection SpellCheckingInspection
test(
    word_break,
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cats and dog", "cat sand dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ],
    map_func=lambda l: set(l),
)
