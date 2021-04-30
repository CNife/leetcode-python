def update_board(board: list[list[str]], click: list[int]) -> list[list[str]]:
    m, n = len(board), len(board[0])

    def update(x: int, y: int) -> None:
        nonlocal board

        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            bombs, blanks = [], []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == "M":
                            bombs.append((nx, ny))
                        elif board[nx][ny] == "E":
                            blanks.append((nx, ny))

            if bombs:
                board[x][y] = str(len(bombs))
            else:
                board[x][y] = "B"
                for nx, ny in blanks:
                    update(nx, ny)

    update(click[0], click[1])
    return board


if __name__ == "__main__":
    assert update_board(
        [
            ["E", "E", "E", "E", "E"],
            ["E", "E", "M", "E", "E"],
            ["E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E"],
        ],
        [3, 0],
    ) == [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    assert update_board(
        [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "M", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"],
        ],
        [1, 2],
    ) == [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "X", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
