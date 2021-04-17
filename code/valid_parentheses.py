from leetcode import test


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


test(
    is_valid,
    [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[()]}", True),
        ("]", False),
    ],
)
