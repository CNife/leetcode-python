def merge(a: list[int], m: int, b: list[int], n: int) -> None:
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


if __name__ == "__main__":
    tests = [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])]
    for a, m, b, n, want in tests:
        merge(a, m, b, n)
        assert a == want
