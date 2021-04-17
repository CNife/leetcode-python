from typing import List

from leetcode import test


def predicate_the_winner(nums: List[int]) -> bool:
    dp = [[-1] * 21 for _ in range(21)]

    def range_sum(start: int, end: int) -> int:
        nonlocal nums
        return sum(nums[i] for i in range(start - 1, end))

    def dfs(left: int, right: int) -> int:
        nonlocal nums
        if dp[left][right] == -1:
            if left == right:
                dp[left][right] = nums[left - 1]
            else:
                dp[left][right] = range_sum(left, right) - min(
                    dfs(left + 1, right), dfs(left, right - 1)
                )
        return dp[left][right]

    return dfs(1, len(nums)) * 2 >= range_sum(1, len(nums))


test(
    predicate_the_winner,
    [
        ([1, 5, 2], False),
        ([1, 5, 233, 7], True),
    ],
)
