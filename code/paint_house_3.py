from functools import lru_cache


def min_cost(
    houses: list[int], cost: list[list[int]], m: int, n: int, target: int
) -> int:
    inf = float("inf")

    @lru_cache(None)
    def dfs(idx, color, t):
        if t < 0 or t > m - idx:
            return inf
        if idx == m:
            return 0

        curr = inf
        if houses[idx]:
            if houses[idx] != color:
                curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
            else:
                curr = min(curr, dfs(idx + 1, houses[idx], t))
        else:
            for i in range(1, n + 1):
                if i != color:
                    curr = min(curr, dfs(idx + 1, i, t - 1) + cost[idx][i - 1])
                else:
                    curr = min(curr, dfs(idx + 1, i, t) + cost[idx][i - 1])
        return curr

    result = dfs(0, 0, target)
    if result == inf:
        return -1
    return result


if __name__ == "__main__":
    assert (
        min_cost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3)
        == 9
    )
    assert (
        min_cost([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3)
        == 11
    )
    assert (
        min_cost(
            [0, 0, 0, 0, 0], [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], 5, 2, 5
        )
        == 5
    )
    assert (
        min_cost([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3)
        == -1
    )
