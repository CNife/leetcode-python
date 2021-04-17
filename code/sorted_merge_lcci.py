from typing import List

from leetcode import test


def merge(a: List[int], m: int, b: List[int], n: int) -> None:
    i, j = m - 1, n - 1
    for k in range(m + n - 1, -1, -1):
        lhs = a[i] if i >= 0 else float("-Infinity")
        rhs = b[j] if j >= 0 else float("-Infinity")
        if lhs > rhs:
            a[k] = lhs
            i -= 1
        else:
            a[k] = rhs
            j -= 1


test(
    merge,
    [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])],
    actual_func=lambda t, _: t[0],
)
