from collections import deque
from typing import List

from leetcode import TreeNode, new_tree, test


def level_order_bottom(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    queue, result = deque([root]), []
    while queue:
        queue_len = len(queue)
        level = []
        for _ in range(queue_len):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    result.reverse()
    return result


test(
    level_order_bottom,
    [
        (new_tree(3, 9, 20, None, None, 15, 7), [[15, 7], [9, 20], [3]]),
    ],
)
