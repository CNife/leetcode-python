def is_valid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in ("(", "[", "{"):
            stack.append(ch)
        elif not stack:
            return False
        elif (stack[-1], ch) in (("(", ")"), ("[", "]"), ("{", "}")):
            stack.pop()
        else:
            return False
    return not stack


if __name__ == "__main__":
    assert is_valid("") is True
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[()]}") is True
    assert is_valid("]") is False
