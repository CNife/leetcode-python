"""
1482. 制作 m 束花所需的最少天数，中等
https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""


def min_days(bloom_day: list[int], m: int, k: int) -> int:
    def check(time: int) -> bool:
        bunches, current = 0, 0
        for day in bloom_day:
            if day > time:
                current = 0
            else:
                current += 1
            if current >= k:
                bunches += 1
                current = 0
        return bunches >= m

    n = len(bloom_day)

    if m * k > n:
        return -1

    left, right = min(bloom_day), max(bloom_day)
    while left <= right:
        middle = (left + right) // 2
        if check(middle):
            right = middle - 1
        else:
            left = middle + 1
    return left


if __name__ == "__main__":
    assert min_days([1, 10, 3, 10, 2], 3, 1) == 3
    assert min_days([1, 10, 3, 10, 2], 3, 2) == -1
    assert min_days([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
    assert min_days([1000000000, 1000000000], 1, 1) == 1000000000
    assert min_days([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2) == 9
