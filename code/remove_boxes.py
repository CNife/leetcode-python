from typing import List

from leetcode import test


def remove_boxes(boxes: List[int]) -> int:
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]

    def calc(left: int, right: int, k: int) -> int:
        nonlocal boxes, dp

        if left > right:
            return 0
        if dp[left][right][k] != 0:
            return dp[left][right][k]
        while right > left and boxes[right] == boxes[right - 1]:
            right -= 1
            k += 1
        dp[left][right][k] = calc(left, right - 1, 0) + (k + 1) * (k + 1)
        for i in range(left, right):
            if boxes[i] == boxes[right]:
                n = calc(left, i, k + 1) + calc(i + 1, right - 1, 0)
                dp[left][right][k] = max(dp[left][right][k], n)
        return dp[left][right][k]

    return calc(0, len(boxes) - 1, 0)


test(
    remove_boxes,
    [
        ([1, 3, 2, 2, 2, 3, 4, 3, 1], 23),
    ],
)
