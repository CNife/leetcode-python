"""
1734. 解码异或后的排列，中等
https://leetcode-cn.com/problems/decode-xored-permutation/
"""
import functools
import itertools


def decode(encoded: list[int]) -> list[int]:
    def xor_n(n: int) -> int:
        t = n & 3
        return (t // 2) ^ (n if t % 2 == 0 else 1)

    def xor(a: int, b: int) -> int:
        return a ^ b

    all_xor = xor_n(len(encoded) + 1)
    tail_xor = functools.reduce(xor, (encoded[n] for n in range(1, len(encoded), 2)))
    head = all_xor ^ tail_xor
    return list(itertools.accumulate(encoded, xor, initial=head))


if __name__ == "__main__":
    assert decode([3, 1]) == [1, 2, 3]
    assert decode([6, 5, 4, 6]) == [2, 4, 1, 5, 3]
