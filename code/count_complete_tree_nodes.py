from collections import deque

from leetcode import TreeNode, new_tree


def count_nodes(root: TreeNode) -> int:
    if root is None:
        return 0

    queue, result = deque((root,)), 0
    while True:
        length = len(queue)
        result += length
        if queue[0].left is None:
            return result

        for _ in range(length):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == "__main__":
    assert count_nodes(new_tree(1, 2, 3, 4, 5, 6)) == 6
    assert count_nodes(new_tree()) == 0
    assert count_nodes(new_tree(1)) == 1
