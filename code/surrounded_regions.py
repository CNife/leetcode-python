diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def solve(board: list[list[str]]) -> None:
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(x: int, y: int) -> None:
        nonlocal board, m, n, visited

        board[x][y] = "o"
        visited[x][y] = True
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < m
                and 0 <= ny < n
                and board[nx][ny] == "O"
                and not visited[nx][ny]
            ):
                dfs(nx, ny)

    for i in range(m):
        if board[i][0] == "O":
            dfs(i, 0)
        if board[i][n - 1] == "O":
            dfs(i, n - 1)
    for j in range(1, n - 1):
        if board[0][j] == "O":
            dfs(0, j)
        if board[m - 1][j] == "O":
            dfs(m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "o":
                board[i][j] = "O"


if __name__ == "__main__":
    tests = [
        (
            [
                [
                    "X",
                    "X",
                    "X",
                    "X",
                ],
                [
                    "X",
                    "O",
                    "O",
                    "X",
                ],
                [
                    "X",
                    "X",
                    "O",
                    "X",
                ],
                [
                    "X",
                    "O",
                    "X",
                    "X",
                ],
            ],
            [
                [
                    "X",
                    "X",
                    "X",
                    "X",
                ],
                [
                    "X",
                    "X",
                    "X",
                    "X",
                ],
                [
                    "X",
                    "X",
                    "X",
                    "X",
                ],
                [
                    "X",
                    "O",
                    "X",
                    "X",
                ],
            ],
        ),
        ([], []),
    ]
    for board, want in tests:
        solve(board)
        assert board == want
