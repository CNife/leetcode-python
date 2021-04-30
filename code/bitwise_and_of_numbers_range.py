def range_bitwise_and(m: int, n: int) -> int:
    for i in range(32):
        if m >> i == n >> i:
            return m & (-1 << i)


if __name__ == "__main__":
    assert range_bitwise_and(5, 7) == 4
    assert range_bitwise_and(0, 1) == 0
