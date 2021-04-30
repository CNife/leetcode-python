from typing import List


def game(guess: List[int], answer: List[int]) -> int:
    return len([None for g, a in zip(guess, answer) if g == a])


if __name__ == "__main__":
    assert game([1, 2, 3], [1, 2, 3]) == 3
    assert game([2, 2, 3], [3, 2, 1]) == 1
