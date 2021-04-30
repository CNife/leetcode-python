def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    result = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                valid_len = i - stack[-1]
                result = max(result, valid_len)
            else:
                stack.append(i)
    return result


if __name__ == "__main__":
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
