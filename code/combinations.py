from typing import List

from leetcode import test, sorted_list


def combine(n: int, k: int) -> List[List[int]]:
    result, stack = [], []

    def backtrack(start: int) -> None:
        nonlocal n, k, result, stack
        if len(stack) < k:
            for num in range(start, n + 1):
                stack.append(num)
                backtrack(num + 1)
                stack.pop()
        else:
            result.append(list(stack))

    backtrack(1)
    return result


test(
    combine,
    [
        (4, 2, [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]),
    ],
    map_func=sorted_list,
)
