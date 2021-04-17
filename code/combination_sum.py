from typing import List

from leetcode import test


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)
    candidates.sort()

    result, stack = [], []

    def backtrack(i: int, current: int) -> None:
        nonlocal result, stack
        if current == target:
            result.append(list(stack))
        elif current < target and i < n:
            for j in range(i, n):
                candidate = candidates[j]
                if candidate <= target - current:
                    stack.append(candidate)
                    backtrack(j, current + candidate)
                    stack.pop()
                else:
                    break

    backtrack(0, 0)
    return result


def sll(li):
    for i in li:
        i.sort()
    li.sort()
    return li


test(
    combination_sum,
    [
        ([2, 3, 6, 7], 7, [[7], [2, 2, 3]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ],
    map_func=sll,
)
