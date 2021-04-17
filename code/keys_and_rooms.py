from typing import List

from leetcode import test


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    visited = [False] * len(rooms)

    def dfs(i: int) -> None:
        nonlocal visited, rooms
        if visited[i]:
            return
        visited[i] = True
        for key in rooms[i]:
            dfs(key)

    dfs(0)
    return all(v for v in visited)


test(
    can_visit_all_rooms,
    [
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
        ([[]], True),
    ],
)
