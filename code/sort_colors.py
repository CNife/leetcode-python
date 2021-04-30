def sort_colors(nums: list[int]) -> None:
    i, m, n = 0, 0, len(nums) - 1
    while i <= n:
        if nums[i] == 0:
            nums[i] = nums[m]
            nums[m] = 0
            m += 1
        elif nums[i] == 2:
            nums[i] = nums[n]
            nums[n] = 2
            i -= 1
            n -= 1
        i += 1


if __name__ == "__main__":
    tests = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ]
    for nums, want in tests:
        sort_colors(nums)
        assert nums == want
