from collections import deque
from itertools import zip_longest
from math import isclose
from typing import List

from leetcode import TreeNode, test, new_tree


def average_of_levels(root: TreeNode) -> List[float]:
    if not root:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        level_length = len(queue)
        level_sum = 0
        for _ in range(level_length):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_length)
    return result


test(
    average_of_levels,
    [
        (new_tree(3, 9, 20, None, None, 15, 7), [3, 14.5, 11]),
    ],
    equals_func=lambda lhs, rhs: all(
        isclose(left, right)
        for left, right in zip_longest(lhs, rhs, fillvalue=float("nan"))
    ),
)
