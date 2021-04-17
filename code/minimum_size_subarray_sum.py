import bisect
from typing import List

from leetcode import test


def min_subarray_len(nums: List[int], target: int) -> int:
    prefix_sums = []
    result = float("Infinity")
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        prefix_sums.append(prefix_sum)
        diff = prefix_sum - target
        if diff >= 0:
            j = bisect.bisect_right(prefix_sums, diff)
            result = min(result, i - j + 1)
    return 0 if result == float("Infinity") else result


test(min_subarray_len, [([2, 3, 1, 2, 4, 3], 7, 2), ([], 100, 0)])
