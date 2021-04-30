from leetcode import sorted_2d_equals


def combinations(k: int, n: int) -> list[list[int]]:
    result, stack = [], []

    def backtrace(ki: int, ni: int, current: int) -> None:
        nonlocal result, stack
        if ni == 0 and ki == 0:
            result.append(list(stack))
        if current > 9 or current > ni or ni > 45:
            return
        stack.append(current)
        backtrace(ki - 1, ni - current, current + 1)
        stack.pop()
        backtrace(ki, ni, current + 1)

    backtrace(k, n, 1)
    return result


if __name__ == "__main__":
    assert sorted_2d_equals(combinations(3, 7), [[1, 2, 4]])
    assert sorted_2d_equals(
        combinations(
            3,
            9,
        ),
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
    )
