def increasing_triplet(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    small, middle = 2 ** 31 - 1, 2 ** 31 - 1
    for num in nums:
        if num <= small:
            small = num
        elif num <= middle:
            middle = num
        else:
            return True
    return False


if __name__ == "__main__":
    assert increasing_triplet([1, 2, 3, 4, 5]) is True
    assert increasing_triplet([5, 4, 3, 2, 1]) is False
