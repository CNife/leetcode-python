def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
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


if __name__ == "__main__":
    assert can_visit_all_rooms([[1], [2], [3], []]) is True
    assert can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]) is False
    assert can_visit_all_rooms([[]]) is True
