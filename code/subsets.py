from typing import List

from leetcode import test, sorted_2d_list


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def inner(src: List[int], current: List[int]) -> None:
        if src:
            inner(src[1:], list(current))
            current.append(src[0])
            inner(src[1:], current)
        else:
            result.append(current)

    inner(nums, [])
    return result


test(
    subsets,
    [([1, 2, 3], [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []])],
    map_func=sorted_2d_list,
)
