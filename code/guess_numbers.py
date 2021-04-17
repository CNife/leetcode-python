from typing import List

from leetcode import test


def game(guess: List[int], answer: List[int]) -> int:
    return len([None for g, a in zip(guess, answer) if g == a])


test(game, [([1, 2, 3], [1, 2, 3], 3), ([2, 2, 3], [3, 2, 1], 1)])
