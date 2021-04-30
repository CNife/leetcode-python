from collections import defaultdict
from heapq import heappush, heapreplace
from leetcode.test import sorted_equals


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counter = defaultdict(lambda: 0)
    for num in nums:
        counter[num] += 1

    heap: list[tuple[int, int]] = []
    for num, count in counter.items():
        if len(heap) < k:
            heappush(heap, (count, num))
        elif heap[0][0] < count:
            heapreplace(heap, (count, num))
    return [t[1] for t in heap]


if __name__ == "__main__":
    assert sorted_equals(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    assert sorted_equals(top_k_frequent([1], 1), [1])
