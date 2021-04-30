from leetcode import sorted_2d_equals


def combine(n: int, k: int) -> list[list[int]]:
    result, stack = [], []

    def backtrack(start: int) -> None:
        nonlocal n, k, result, stack
        if len(stack) < k:
            for num in range(start, n + 1):
                stack.append(num)
                backtrack(num + 1)
                stack.pop()
        else:
            result.append(list(stack))

    backtrack(1)
    return result


if __name__ == "__main__":
    assert sorted_2d_equals(
        combine(
            4,
            2,
        ),
        [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]],
    )
