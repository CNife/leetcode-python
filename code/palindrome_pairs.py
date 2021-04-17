from typing import List

from leetcode import test


def palindrome_pairs_1(words: List[str]) -> List[List[int]]:
    res = []
    word_dict = {word: i for i, word in enumerate(words)}
    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            tmp1 = word[:j]
            tmp2 = word[j:]
            if (
                tmp1[::-1] in word_dict
                and word_dict[tmp1[::-1]] != i
                and tmp2 == tmp2[::-1]
            ):
                res.append([i, word_dict[tmp1[::-1]]])

            if (
                j > 0
                and tmp2[::-1] in word_dict
                and word_dict[tmp2[::-1]] != i
                and tmp1 == tmp1[::-1]
            ):
                res.append([word_dict[tmp2[::-1]], i])
    return res


# noinspection SpellCheckingInspection
test(
    palindrome_pairs_1,
    [
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
    ],
    map_func=lambda l: (l.sort(), l),
)
