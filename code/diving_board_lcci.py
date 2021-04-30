def diving_board(shorter: int, longer: int, k: int) -> list[int]:
    if k == 0:
        return []
    if shorter == longer:
        return [shorter * k]

    diff = longer - shorter
    acc = shorter * k
    result = [acc]
    for _ in range(k):
        acc += diff
        result.append(acc)
    return result


if __name__ == "__main__":
    assert diving_board(1, 2, 3) == [3, 4, 5, 6]
    assert diving_board(1, 1, 0) == []
    assert diving_board(1, 1, 2) == [2]
