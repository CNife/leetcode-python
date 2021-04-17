from typing import List

from leetcode import test, sorted_list


def permute_unique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    used, path, result = [False] * len(nums), [], []

    def dfs(n: int) -> None:
        if n == len(nums):
            result.append(list(path))
            return

        prev, is_start = 0, True
        for i in range(len(nums)):
            if (not is_start and prev == nums[i]) or used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            dfs(n + 1)
            used[i] = False
            path.pop()
            is_start = False
            prev = nums[i]

    dfs(0)
    return result


test(
    permute_unique,
    [([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]])],
    map_func=sorted_list,
)
