from typing import List

from leetcode import test


def max_profit(prices: List[int]) -> int:
    rest, hold, sold = 0, float("-inf"), 0
    for price in prices:
        old_sold = sold
        sold = hold + price
        hold = max(hold, rest - price)
        rest = max(rest, old_sold)
    return max(rest, sold)


test(
    max_profit,
    [
        ([1, 2, 3, 0, 2], 3),
    ],
)
