"""
993. 二叉树的堂兄弟节点，简单
https://leetcode-cn.com/problems/cousins-in-binary-tree/
"""

from collections import deque

from leetcode import TreeNode, new_tree


def is_cousins(root: TreeNode, x: int, y: int) -> bool:
    def bfs(node: TreeNode, t: int) -> tuple[int, int]:
        queue = deque()
        queue.append((node, None, 0))
        while (size := len(queue)) > 0:
            for _ in range(size):
                current, father, depth = queue.popleft()
                if current.val == t:
                    return father.val if father is not None else 0, depth
                if current.left is not None:
                    queue.append((current.left, current, depth + 1))
                if current.right is not None:
                    queue.append((current.right, current, depth + 1))
        return -1, -1

    x_father, x_depth = bfs(root, x)
    y_father, y_depth = bfs(root, y)
    return x_father != y_father and x_depth == y_depth


if __name__ == "__main__":
    assert is_cousins(new_tree(1, 2, 3, 4), 4, 3) is False
    assert is_cousins(new_tree(1, 2, 3, None, 4, None, 5), 5, 4) is True
    assert is_cousins(new_tree(1, 2, 3, None, 4), 2, 3) is False
