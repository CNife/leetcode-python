def move_zeroes(nums: list[int]) -> None:
    i = 0
    for j, num in enumerate(nums):
        if num != 0:
            nums[i] = nums[j]
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1


if __name__ == "__main__":
    tests = [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])]
    for nums, want in tests:
        move_zeroes(nums)
        assert nums == want
