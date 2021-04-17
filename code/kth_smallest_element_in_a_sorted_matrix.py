import heapq
from typing import List

from leetcode import test


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    heap = []
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    for _ in range(1, k):
        heapq.heappop(heap)
    return heap[0]


test(kth_smallest, [([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13)])
