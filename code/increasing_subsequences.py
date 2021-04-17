from typing import List

from leetcode import test


def find_subsequences(nums: List[int]) -> List[List[int]]:
    results, stack = set(), []

    def backtrack(start: int):
        nonlocal nums, results, stack

        if len(stack) >= 2:
            results.add(tuple(stack))
        for i in range(start, len(nums)):
            if not stack or stack[-1] <= nums[i]:
                stack.append(nums[i])
                backtrack(i + 1)
                stack.pop()

    backtrack(0)
    return [list(res) for res in results]


test(
    find_subsequences,
    [
        (
            [4, 6, 7, 7],
            [
                [4, 6],
                [4, 7],
                [4, 6, 7],
                [4, 6, 7, 7],
                [6, 7],
                [6, 7, 7],
                [7, 7],
                [4, 7, 7],
            ],
        )
    ],
    map_func=lambda l: set(tuple(item) for item in l),
)
