from typing import List

from leetcode import test


def diving_board(shorter: int, longer: int, k: int) -> List[int]:
    if k == 0:
        return []
    if shorter == longer:
        return [shorter * k]

    diff = longer - shorter
    acc = shorter * k
    result = [acc]
    for _ in range(k):
        acc += diff
        result.append(acc)
    return result


test(
    diving_board,
    [
        (1, 2, 3, [3, 4, 5, 6]),
        (1, 1, 0, []),
        (1, 1, 2, [2]),
    ],
)
