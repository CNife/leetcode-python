from leetcode import test


def match(s: str, p: str) -> bool:
    s_len, p_len = len(s), len(p)
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

    dp[0][0] = True
    for j in range(1, p_len + 1):
        dp[0][j] = p[j - 1] == "*" and dp[0][j - 1]

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*" and (dp[i - 1][j] or dp[i][j - 1]):
                dp[i][j] = True

    return dp[s_len][p_len]


# noinspection SpellCheckingInspection
test(
    match,
    [
        ("", "", True),
        ("", "a", False),
        ("", "*", True),
        ("a", "", False),
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("abceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
        ("ho", "ho**", True),
    ],
)
