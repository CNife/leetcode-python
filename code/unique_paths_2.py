from typing import List

from leetcode import test


def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    if not (grid and grid[0]):
        return 0

    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0

    dp = [0] * n
    for j in range(n):
        if grid[0][j] == 0:
            dp[j] = 1
        else:
            break

    for i in range(1, m):
        dp[0] = 1 if grid[i][0] == 0 and dp[0] == 1 else 0
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[j] = 0
            else:
                up = dp[j] if grid[i - 1][j] == 0 else 0
                left = dp[j - 1] if grid[i][j - 1] == 0 else 0
                dp[j] = up + left
    return dp[n - 1]


# def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
#     if not (grid and grid[0]):
#         return 0
#
#     m, n = len(grid), len(grid[0])
#     if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
#         return 0
#
#     dp = [[0] * n for _ in range(m)]
#     dp[0][0] = 1
#     for i in range(1, m):
#         if grid[i][0] == 0:
#             dp[i][0] = 1
#         else:
#             break
#     for j in range(1, n):
#         if grid[0][j] == 0:
#             dp[0][j] = 1
#         else:
#             break
#
#     for i in range(1, m):
#         for j in range(1, n):
#             if grid[i][j] == 1:
#                 continue
#             left = dp[i][j - 1] if grid[i][j - 1] == 0 else 0
#             up = dp[i - 1][j] if grid[i - 1][j] == 0 else 0
#             dp[i][j] = left + up
#     return dp[m - 1][n - 1]


test(unique_paths_with_obstacles, [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2)])
