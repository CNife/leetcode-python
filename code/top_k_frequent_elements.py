from collections import defaultdict
from heapq import heappush, heapreplace
from typing import List, Tuple

from leetcode import test, sorted_list


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counter = defaultdict(lambda: 0)
    for num in nums:
        counter[num] += 1

    heap: List[Tuple[int, int]] = []
    for num, count in counter.items():
        if len(heap) < k:
            heappush(heap, (count, num))
        elif heap[0][0] < count:
            heapreplace(heap, (count, num))
    return [t[1] for t in heap]


test(
    top_k_frequent,
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ],
    map_func=sorted_list,
)
