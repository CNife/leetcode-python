from leetcode import sorted_2d_equals


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    if len(nums) < 4:
        return []

    nums.sort()
    result = set()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left, right = j + 1, len(nums) - 1
            while left < right:
                sum_4 = nums[i] + nums[j] + nums[left] + nums[right]
                if sum_4 == target:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum_4 < target:
                    left += 1
                else:
                    right -= 1
    return [list(item) for item in result]


if __name__ == "__main__":
    assert sorted_2d_equals(
        four_sum(
            [1, 0, -1, 0, -2, 2],
            0,
        ),
        [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]],
    )
