import bisect


def min_subarray_len(nums: list[int], target: int) -> int:
    prefix_sums = []
    result = float("Infinity")
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        prefix_sums.append(prefix_sum)
        diff = prefix_sum - target
        if diff >= 0:
            j = bisect.bisect_right(prefix_sums, diff)
            result = min(result, i - j + 1)
    return 0 if result == float("Infinity") else result


if __name__ == "__main__":
    assert min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2
    assert min_subarray_len([], 100) == 0
