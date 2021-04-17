import functools
import itertools
import math


def judge_24_points(nums: [int]) -> bool:
    @functools.lru_cache(None)
    def inner(t: (int, ...)) -> bool:
        if len(t) == 1:
            return math.isclose(t[0], 24)
        return any(
            inner(tuple(rest) + (x,))
            for a, b, *rest in itertools.permutations(t)
            for x in {a + b, a - b, a * b, b and a / b}
        )

    return inner(tuple(nums))


if __name__ == "__main__":
    assert judge_24_points([4, 1, 8, 7]) is True
    assert judge_24_points([1, 2, 1, 2]) is False
