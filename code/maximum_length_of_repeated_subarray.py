from typing import List

from leetcode import test


def find_length(a: List[int], b: List[int]) -> int:
    dp = [0] * (len(b) + 1)
    result = 0
    for i in range(1, len(a) + 1):
        for j in range(len(b), 0, -1):
            if a[i - 1] == b[j - 1]:
                dp[j] = dp[j - 1] + 1
            else:
                dp[j] = 0
            result = max(result, dp[j])
    return result


test(find_length, [([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3)])
