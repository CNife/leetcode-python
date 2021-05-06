"""
1720. 解码异或后的数组
https://leetcode-cn.com/problems/decode-xored-array/
"""
from itertools import accumulate


def decode(encoded: list[int], first: int) -> list[int]:
    # if a xor b = c, then b = a xor c
    return list(accumulate(encoded, lambda before, num: before ^ num, initial=first))


if __name__ == "__main__":
    assert decode([1, 2, 3], 1) == [1, 0, 2, 1]
    assert decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
