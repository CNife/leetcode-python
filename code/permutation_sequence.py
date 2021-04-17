import math

from leetcode import test


def get_permutation(n: int, k: int) -> str:
    seq = [chr(ord("1") + i) for i in range(n)]
    res = []
    base = math.factorial(n - 1)
    k -= 1

    for m in range(n - 1, 0, -1):
        pos = k // base
        res.append(seq[pos])
        seq.pop(pos)
        k %= base
        base //= m

    res.append(seq[0])
    return "".join(res)


test(
    get_permutation,
    [
        (3, 3, "213"),
        (4, 9, "2314"),
    ],
)
