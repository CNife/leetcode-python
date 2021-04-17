from typing import List

from leetcode import test


def move_zeroes(nums: List[int]) -> None:
    i = 0
    for j, num in enumerate(nums):
        if num != 0:
            nums[i] = nums[j]
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1


test(move_zeroes, [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])], actual_func=lambda t, _: t[1])
