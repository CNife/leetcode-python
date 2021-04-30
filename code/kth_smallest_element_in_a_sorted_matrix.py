import heapq


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    heap = []
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    for _ in range(1, k):
        heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    assert kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
