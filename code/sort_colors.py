from typing import List

from leetcode import test


def sort_colors(nums: List[int]) -> None:
    i, m, n = 0, 0, len(nums) - 1
    while i <= n:
        if nums[i] == 0:
            nums[i] = nums[m]
            nums[m] = 0
            m += 1
        elif nums[i] == 2:
            nums[i] = nums[n]
            nums[n] = 2
            i -= 1
            n -= 1
        i += 1


test(
    sort_colors,
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ],
    actual_func=lambda t, _: t[1],
)
