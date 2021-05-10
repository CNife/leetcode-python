"""
872. 叶子相似的树，简单
https://leetcode-cn.com/problems/leaf-similar-trees/
"""

from itertools import zip_longest

from leetcode import TreeNode, new_tree


def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 is None:
        return root2 is None
    if root2 is None:
        return False

    def walk_tree(root: TreeNode):
        left, right = root.left, root.right
        if left is None and right is None:
            yield root.val
        else:
            if left is not None:
                yield from walk_tree(left)
            if right is not None:
                yield from walk_tree(right)

    for v1, v2 in zip_longest(
        walk_tree(root1), walk_tree(root2), fillvalue=float("NaN")
    ):
        if v1 != v2:
            return False
    return True


if __name__ == "__main__":
    assert (
        leaf_similar(
            new_tree(3, 5, 1, 6, 2, 9, 8, None, None, 7, 4),
            new_tree(3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8),
        )
        is True
    )
    assert leaf_similar(new_tree(1), new_tree(1)) is True
    assert leaf_similar(new_tree(1), new_tree(2)) is False
    assert leaf_similar(new_tree(1, 2), new_tree(2, 2)) is True
    assert leaf_similar(new_tree(1, 2, 3), new_tree(1, 3, 2)) is False
