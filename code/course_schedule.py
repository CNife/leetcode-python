from typing import List

from leetcode import test


def can_finish(node_count: int, edges: List[List[int]]) -> bool:
    graph = [[] for _ in range(node_count)]
    in_degrees = [0] * node_count
    for edge in edges:
        start, end = edge[:2]
        graph[start].append(end)
        in_degrees[end] += 1

    while True:
        for start, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                break
        else:
            return all(in_degree <= 0 for in_degree in in_degrees)

        in_degrees[start] = -1
        for end in graph[start]:
            in_degrees[end] -= 1


test(
    can_finish,
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
    ],
)
