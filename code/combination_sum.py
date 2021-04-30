from leetcode import sorted_2d_equals


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    n = len(candidates)
    candidates.sort()

    result, stack = [], []

    def backtrack(i: int, current: int) -> None:
        nonlocal result, stack
        if current == target:
            result.append(list(stack))
        elif current < target and i < n:
            for j in range(i, n):
                candidate = candidates[j]
                if candidate <= target - current:
                    stack.append(candidate)
                    backtrack(j, current + candidate)
                    stack.pop()
                else:
                    break

    backtrack(0, 0)
    return result


if __name__ == "__main__":
    assert sorted_2d_equals(combination_sum([2, 3, 6, 7], 7), [[7], [2, 2, 3]])
    assert sorted_2d_equals(
        combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
