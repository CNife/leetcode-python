def delete_and_earn(nums: list[int]) -> int:
    n = len(nums)
    if n < 1:
        return 0
    if n == 1:
        return nums[0]

    max_num = max(nums)
    all_nums = [0] * (max_num + 1)
    for num in nums:
        all_nums[num] += 1

    dp = [0] * (max_num + 1)
    dp[1] = all_nums[1]
    dp[2] = max(dp[1], all_nums[2] * 2)
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + i * all_nums[i])
    return dp[max_num]


if __name__ == '__main__':
    assert delete_and_earn([3, 4, 2]) == 6
    assert delete_and_earn([2, 2, 3, 3, 3, 4]) == 9
