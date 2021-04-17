from typing import List

from leetcode import test, sorted_list


def combinations(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)
    result, stack = set(), []

    def backtrack(i: int, current_sum: int) -> None:
        nonlocal result, stack
        if current_sum == target:
            result.add(tuple(stack))
        elif i < n:
            diff = target - current_sum
            for j, candidate in enumerate(candidates[i:], i):
                if candidate <= diff:
                    stack.append(candidate)
                    backtrack(j + 1, current_sum + candidate)
                    stack.pop()
                else:
                    break

    backtrack(0, 0)
    return [list(t) for t in result]


test(
    combinations,
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ],
    map_func=sorted_list,
)
