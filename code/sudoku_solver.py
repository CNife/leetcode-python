def solve_sudoku(board: list[list[str]]) -> None:
    if not (board and len(board) == 9 and len(board[0]) == 9):
        return

    row = [[False] * 9 for _ in range(9)]
    col = [[False] * 9 for _ in range(9)]
    box = [[False] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            num = int(board[i][j]) - 1
            k = (i // 3) * 3 + j // 3
            row[i][num] = col[j][num] = box[k][num] = True

    # noinspection PyShadowingNames
    def solve(n: int) -> bool:
        if n == 81:
            return True
        i, j = n // 9, n % 9
        if board[i][j] != ".":
            return solve(n + 1)

        k = (i // 3) * 3 + j // 3
        for num in range(9):
            if row[i][num] or col[j][num] or box[k][num]:
                continue
            board[i][j] = str(num + 1)
            row[i][num] = col[j][num] = box[k][num] = True
            if solve(n + 1):
                return True
            row[i][num] = col[j][num] = box[k][num] = False
        board[i][j] = "."
        return False

    solve(0)


if __name__ == "__main__":
    tests = [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
        ),
    ]
    for board, want in tests:
        solve_sudoku(board)
        assert board == want
