def word_break(s: str, word_dict: list[str]) -> bool:
    n = len(s)
    words = set(word_dict)
    dp = [True] + [False] * n
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and s[i:j] in words:
                dp[j] = True
    return dp[n]


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
