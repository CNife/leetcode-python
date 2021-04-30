from leetcode import sorted_2d_equals


def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def inner(src: list[int], current: list[int]) -> None:
        if src:
            inner(src[1:], list(current))
            current.append(src[0])
            inner(src[1:], current)
        else:
            result.append(current)

    inner(nums, [])
    return result


if __name__ == "__main__":
    assert sorted_2d_equals(
        subsets([1, 2, 3]), [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
    )
