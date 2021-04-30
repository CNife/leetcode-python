def count_binary_substrings(s: str) -> int:
    result = 0
    for i in range(1, len(s)):
        left, right = i - 1, i
        if s[left] == s[right]:
            continue
        left_byte, right_byte = s[left], s[right]
        while (
            0 <= left < len(s)
            and right < len(s)
            and s[left] == left_byte
            and s[right] == right_byte
        ):
            left -= 1
            right += 1
            result += 1
    return result


if __name__ == "__main__":
    assert count_binary_substrings("00110011") == 6
    assert count_binary_substrings("10101") == 4
