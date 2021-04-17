from typing import List

from leetcode import test

Edge = List[int]


def find_redundant_directed_connection(edges: List[Edge]) -> Edge:
    nodes_count = len(edges)
    uf = UnionFind(nodes_count + 1)
    parent = list(range(nodes_count + 1))
    conflict, cycle = -1, -1

    for i, [node1, node2] in enumerate(edges):
        if parent[node2] != node2:
            conflict = i
        else:
            parent[node2] = node1
            if uf.find(node1) == uf.find(node2):
                cycle = i
            else:
                uf.union(node1, node2)

    if conflict < 0:
        return edges[cycle]
    elif cycle >= 0:
        return [parent[edges[conflict][1]], edges[conflict][1]]
    else:
        return edges[conflict]


class UnionFind:
    def __init__(self, n: int):
        self.ancestor = list(range(n))

    def union(self, lhs: int, rhs: int) -> None:
        self.ancestor[self.find(lhs)] = self.find(rhs)

    def find(self, i: int) -> int:
        if self.ancestor[i] != i:
            self.ancestor[i] = self.find(self.ancestor[i])
        return self.ancestor[i]


test(
    find_redundant_directed_connection,
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
    ],
)
