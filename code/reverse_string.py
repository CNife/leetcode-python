from typing import List

from leetcode import test


def reverse_string(s: List[str]) -> None:
    l = len(s)
    for i in range(l // 2):
        s[i], s[l - i - 1] = s[l - i - 1], s[i]


test(
    reverse_string,
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a", "b"], ["b", "a"]),
    ],
    actual_func=lambda t, _: t[0],
)
