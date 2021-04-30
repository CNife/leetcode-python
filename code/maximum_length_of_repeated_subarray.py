def find_length(a: list[int], b: list[int]) -> int:
    dp = [0] * (len(b) + 1)
    result = 0
    for i in range(1, len(a) + 1):
        for j in range(len(b), 0, -1):
            if a[i - 1] == b[j - 1]:
                dp[j] = dp[j - 1] + 1
            else:
                dp[j] = 0
            result = max(result, dp[j])
    return result


if __name__ == "__main__":
    assert find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
