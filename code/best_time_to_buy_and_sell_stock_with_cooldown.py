def max_profit(prices: list[int]) -> int:
    rest, hold, sold = 0, float("-inf"), 0
    for price in prices:
        old_sold = sold
        sold = hold + price
        hold = max(hold, rest - price)
        rest = max(rest, old_sold)
    return max(rest, sold)


if __name__ == "__main__":
    assert max_profit([1, 2, 3, 0, 2]) == 3
