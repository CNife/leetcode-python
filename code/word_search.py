_INDEX_OFFSETS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(x: int, y: int, seq: str) -> bool:
        if not seq:
            return True

        visited[x][y] = True
        found = False
        for dx, dy in _INDEX_OFFSETS:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < m
                and 0 <= ny < n
                and not visited[nx][ny]
                and board[nx][ny] == seq[0]
                and dfs(nx, ny, seq[1:])
            ):
                found = True
                break

        visited[x][y] = False
        return found

    first_char = word[0]
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == first_char and dfs(i, j, word[1:]):
                return True
    return False


if __name__ == "__main__":
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )
    assert (
        exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
        is True
    )
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
        is False
    )
