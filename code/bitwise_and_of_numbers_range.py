from leetcode import test


def range_bitwise_and(m: int, n: int) -> int:
    for i in range(32):
        if m >> i == n >> i:
            return m & (-1 << i)


test(
    range_bitwise_and,
    [
        (5, 7, 4),
        (0, 1, 0),
    ],
)
