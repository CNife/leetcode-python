"""
1269. 停在原地的方案数，困难
https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
"""


def num_ways(steps: int, array_len: int) -> int:
    mod = 1_000_000_007
    max_len = min(steps // 2 + 1, array_len)
    dp = [1] + [0] * max_len
    for i in range(1, steps + 1):
        last = 0
        for j in range(max_len):
            temp = dp[j]
            dp[j] += dp[j + 1]
            if j > 0:
                dp[j] += last
            dp[j] %= mod
            last = temp
    return dp[0]


if __name__ == "__main__":
    assert num_ways(3, 2) == 4
    assert num_ways(2, 4) == 2
    assert num_ways(4, 2) == 8
