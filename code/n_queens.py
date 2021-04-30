from leetcode import sorted_equals


def solve_n_queens(n: int) -> list[list[str]]:
    solver = NQueensSolver(n)
    solver.backtrack(0)
    return solver.results


class NQueensSolver:
    def __init__(self, n: int):
        self.n: int = n
        self.queens: list[tuple[int, int]] = []
        self.columns: list[bool] = [False] * n
        self.diagonals: list[bool] = [False] * (2 * n - 1)
        self.rev_diagonals: list[bool] = [False] * (2 * n - 1)
        self.results: list[list[str]] = []

    def backtrack(self, r: int) -> None:
        for c in range(self.n):
            if self.could_place(r, c):
                self.place_queen(r, c)
                if r + 1 == self.n:
                    self.add_result()
                else:
                    self.backtrack(r + 1)
                self.remove_queen(r, c)

    def could_place(self, r: int, c: int) -> bool:
        return not (
            self.columns[c]
            or self.diagonals[self.diagonal(r, c)]
            or self.rev_diagonals[self.rev_diagonal(r, c)]
        )

    def place_queen(self, r: int, c: int) -> None:
        self.queens.append((r, c))
        self.columns[c] = True
        self.diagonals[self.diagonal(r, c)] = True
        self.rev_diagonals[self.rev_diagonal(r, c)] = True

    def remove_queen(self, r: int, c: int) -> None:
        self.queens.pop()
        self.columns[c] = False
        self.diagonals[self.diagonal(r, c)] = False
        self.rev_diagonals[self.rev_diagonal(r, c)] = False

    def add_result(self) -> None:
        result = [["."] * self.n for _ in range(self.n)]
        for r, c in self.queens:
            result[r][c] = "Q"
        self.results.append(["".join(row) for row in result])

    # noinspection PyMethodMayBeStatic
    def diagonal(self, r: int, c: int) -> int:
        return r + c

    def rev_diagonal(self, r: int, c: int) -> int:
        if r >= c:
            return r - c
        else:
            return c - r + self.n - 1


if __name__ == "__main__":
    assert sorted_equals(
        solve_n_queens(4),
        [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
    )
