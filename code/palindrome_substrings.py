def count_substrings(s: str) -> int:
    def count_odd() -> int:
        result = len(s)
        for center in range(1, len(s) - 1):
            for i in range(1, min(center + 1, len(s) - center)):
                if s[center - i] == s[center + i]:
                    result += 1
                else:
                    break
        return result

    def count_even() -> int:
        result = 0
        for left in range(len(s) - 1):
            for i in range(min(left + 1, len(s) - left - 1)):
                if s[left - i] == s[left + i + 1]:
                    result += 1
                else:
                    break
        return result

    return count_odd() + count_even()


if __name__ == "__main__":
    assert count_substrings("abc") == 3
    assert count_substrings("aaa") == 6
