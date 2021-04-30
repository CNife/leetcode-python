from leetcode import sorted_2d_equals


def find_subsequences(nums: list[int]) -> list[list[int]]:
    results, stack = set(), []

    def backtrack(start: int):
        nonlocal nums, results, stack

        if len(stack) >= 2:
            results.add(tuple(stack))
        for i in range(start, len(nums)):
            if not stack or stack[-1] <= nums[i]:
                stack.append(nums[i])
                backtrack(i + 1)
                stack.pop()

    backtrack(0)
    return [list(res) for res in results]


if __name__ == "__main__":
    assert sorted_2d_equals(
        find_subsequences([4, 6, 7, 7]),
        [
            [4, 6],
            [4, 7],
            [4, 6, 7],
            [4, 6, 7, 7],
            [6, 7],
            [6, 7, 7],
            [7, 7],
            [4, 7, 7],
        ],
    )
