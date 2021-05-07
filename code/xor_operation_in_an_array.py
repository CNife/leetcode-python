"""
1486. 数组异或操作，简单
https://leetcode-cn.com/problems/xor-operation-in-an-array/
"""
from functools import reduce


def xor_operation(n: int, start: int) -> int:
    return reduce(lambda acc, num: acc ^ num, range(start, start + n * 2, 2))


if __name__ == "__main__":
    assert xor_operation(5, 0) == 8
    assert xor_operation(4, 3) == 8
    assert xor_operation(1, 7) == 7
    assert xor_operation(10, 5) == 2
