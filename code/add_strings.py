import itertools

from leetcode import test


def add_strings(left: str, right: str) -> str:
    def char2int(ch: str):
        return ord(ch) - ord("0")

    def int2char(ch: int):
        return chr(ch + ord("0"))

    result = []
    carry = False
    for lc, rc in itertools.zip_longest(
        map(char2int, reversed(left)), map(char2int, reversed(right)), fillvalue=0
    ):
        digit = lc + rc
        if carry:
            digit += 1
        if digit > 9:
            carry = True
            digit -= 10
        else:
            carry = False
        result.append(digit)
    if carry:
        result.append(1)

    return "".join(int2char(digit) for digit in reversed(result))


test(
    add_strings,
    [("0", "0", "0"), ("10", "90", "100"), ("9999", "2", "10001"), ("408", "5", "413")],
)
