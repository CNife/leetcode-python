from collections import Counter


# from loguru import logger


def least_bricks(wall: list[list[int]]) -> int:
    c = Counter()
    for line in wall:
        line_sum = 0
        for width in line[:-1]:
            line_sum += width
            c[line_sum] += 1
    # logger.info(str(c))

    result = len(wall)
    if len(c) > 0:
        result -= c.most_common(1)[0][1]
    return result


if __name__ == "__main__":
    assert (
        least_bricks(
            [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
        )
        == 2
    )
    assert least_bricks([[1], [1], [1]]) == 3
