from typing import List

from leetcode import test, sorted_list


def combinations(k: int, n: int) -> List[List[int]]:
    result, stack = [], []

    def backtrace(ki: int, ni: int, current: int) -> None:
        nonlocal result, stack
        if ni == 0 and ki == 0:
            result.append(list(stack))
        if current > 9 or current > ni or ni > 45:
            return
        stack.append(current)
        backtrace(ki - 1, ni - current, current + 1)
        stack.pop()
        backtrace(ki, ni, current + 1)

    backtrace(k, n, 1)
    return result


test(
    combinations,
    [
        (3, 7, [[1, 2, 4]]),
        (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
    ],
    map_func=sorted_list,
)
