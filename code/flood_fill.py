from collections import deque


def flood_fill(
    image: list[list[int]], src_x: int, src_y: int, new_color: int
) -> list[list[int]]:
    m, n = len(image), len(image[0])

    origin_color = image[src_x][src_y]
    if origin_color == new_color:
        return image

    queue: deque[tuple[int, int]] = deque()
    queue.append((src_x, src_y))
    while queue:
        x, y = queue.popleft()
        image[x][y] = new_color
        if x > 0 and image[x - 1][y] == origin_color:
            queue.append((x - 1, y))
        if x < m - 1 and image[x + 1][y] == origin_color:
            queue.append((x + 1, y))
        if y > 0 and image[x][y - 1] == origin_color:
            queue.append((x, y - 1))
        if y < n - 1 and image[x][y + 1] == origin_color:
            queue.append((x, y + 1))
    return image


if __name__ == "__main__":
    assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]
