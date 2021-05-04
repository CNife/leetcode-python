INT32_MIN = -(2 ** 31)
INT32_MAX = 2 ** 31 - 1


def reverse(x: int) -> int:
    result = 0
    if x < 0:
        negative, x = True, -x
    else:
        negative = False

    while x != 0:
        tail = x % 10
        result = result * 10 + tail
        if result > INT32_MAX + 1:
            return 0
        x = x // 10

    if negative:
        result = -result
    if result < INT32_MIN or result > INT32_MAX:
        return 0
    return result


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(0) == 0
