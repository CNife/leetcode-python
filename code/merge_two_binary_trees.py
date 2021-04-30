from typing import Optional

from leetcode import TreeNode, new_tree


def merge_trees(lhs: Optional[TreeNode], rhs: Optional[TreeNode]) -> Optional[TreeNode]:
    if lhs and rhs:
        lhs.val += rhs.val
        lhs.left = merge_trees(lhs.left, rhs.left)
        lhs.right = merge_trees(lhs.right, rhs.right)
        return lhs
    elif lhs:
        return lhs
    elif rhs:
        return rhs
    else:
        return None


if __name__ == "__main__":
    assert merge_trees(
        new_tree(1, 3, 2, 5), new_tree(2, 1, 3, None, 4, None, 7)
    ) == new_tree(3, 4, 5, 5, 4, None, 7)
