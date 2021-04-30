def contains_nearby_almost_duplicate(nums: [int], k: int, t: int) -> bool:
    if len(nums) < 2 or k <= 0 or t < 0:
        return False

    def bucket_id(n: int) -> int:
        if n >= 0:
            return n // (t + 1)
        else:
            return (n + 1) // (t + 1) - 1

    buckets = {}

    for i, num in enumerate(nums):
        if i > k:
            del buckets[bucket_id(nums[i - k - 1])]

        num_id = bucket_id(num)
        if num_id in buckets:
            return True

        next_bucket_value = buckets.get(num_id + 1)
        if next_bucket_value is not None and next_bucket_value - num <= t:
            return True
        prev_bucket_value = buckets.get(num_id - 1)
        if prev_bucket_value is not None and num - prev_bucket_value <= t:
            return True

        buckets[num_id] = num

    return False


if __name__ == "__main__":
    assert contains_nearby_almost_duplicate([2147483640, 2147483641], 1, 100) is True
    assert contains_nearby_almost_duplicate([1, 2, 3, 1], 3, 0) is True
    assert contains_nearby_almost_duplicate([1, 0, 1, 1], 1, 2) is True
    assert contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
