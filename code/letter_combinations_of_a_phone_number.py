def letter_combinations(digits: str) -> list[str]:
    result = []
    digits = [ord(ch) - ord("0") for ch in digits]

    def combine(s: str, i: int) -> None:
        nonlocal digits, result

        if i < len(digits):
            for next_ch in LETTER_TABLE[digits[i]]:
                combine(s + next_ch, i + 1)
        elif digits:
            result.append(s)

    combine("", 0)
    return result


# noinspection SpellCheckingInspection
LETTER_TABLE = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# noinspection SpellCheckingInspection
if __name__ == "__main__":
    assert letter_combinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert letter_combinations("2184") == []
    assert letter_combinations("284") == [
        "atg",
        "ath",
        "ati",
        "aug",
        "auh",
        "aui",
        "avg",
        "avh",
        "avi",
        "btg",
        "bth",
        "bti",
        "bug",
        "buh",
        "bui",
        "bvg",
        "bvh",
        "bvi",
        "ctg",
        "cth",
        "cti",
        "cug",
        "cuh",
        "cui",
        "cvg",
        "cvh",
        "cvi",
    ]
