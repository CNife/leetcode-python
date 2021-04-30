def repeated_substring_pattern(s: str) -> bool:
    return len(s) >= 2 and s in (s * 2)[1:-1]


if __name__ == "__main__":
    assert repeated_substring_pattern("abab") == True
    assert repeated_substring_pattern("aba") == False
    assert repeated_substring_pattern("abcabcabcabc") == True
