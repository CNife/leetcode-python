from typing import List

from leetcode import test


def word_break(s: str, word_dict: List[str]) -> bool:
    n = len(s)
    words = set(word_dict)
    dp = [True] + [False] * n
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and s[i:j] in words:
                dp[j] = True
    return dp[n]


# noinspection SpellCheckingInspection
test(
    word_break,
    [("leetcode", ["leet", "code"], True), ("applepenapple", ["apple", "pen"], True)],
)
