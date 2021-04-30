def reverse_words(s: str) -> str:
    words = []
    for word in s.split(" "):
        reversed_word = "".join(ch for ch in reversed(word))
        words.append(reversed_word)
    return " ".join(words)


if __name__ == "__main__":
    assert reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
