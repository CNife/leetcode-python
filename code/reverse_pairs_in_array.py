def reverse_pairs(nums: list[int]) -> int:
    result = 0

    def merge(start: int, end: int) -> None:
        nonlocal nums, result
        length = end - start
        if length < 2:
            return
        elif length == 2 and nums[start] > nums[start + 1]:
            nums[start], nums[start + 1] = nums[start + 1], nums[start]
            result += 1
            return

        mid = start + length // 2
        merge(start, mid)
        merge(mid, end)

        buf = nums[start:end]
        i, j = 0, mid - start
        for k in range(start, end):
            lhs = buf[i] if i < length // 2 else float("inf")
            rhs = buf[j] if j < length else float("inf")
            if lhs <= rhs:
                nums[k] = lhs
                i += 1
            else:
                nums[k] = rhs
                j += 1
                result += length // 2 - i

    merge(0, len(nums))
    return result


if __name__ == "__main__":
    assert reverse_pairs([7, 5, 6, 4]) == 5
