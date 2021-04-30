def judge_circle(moves: str) -> bool:
    x, y = 0, 0
    for move in moves:
        if move == "U":
            y -= 1
        elif move == "D":
            y += 1
        elif move == "L":
            x -= 1
        else:
            x += 1
    return x == 0 and y == 0


if __name__ == "__main__":
    assert judge_circle("UD") is True
    assert judge_circle("LL") is False
