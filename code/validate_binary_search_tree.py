from typing import Optional

from leetcode import TreeNode, new_tree


def is_valid_bst(root: TreeNode) -> bool:
    def is_valid_bst_bounded(
        node: TreeNode, lower: Optional[int], higher: Optional[int]
    ) -> bool:
        if not node:
            return True
        if lower is not None and node.val <= lower:
            return False
        if higher is not None and node.val >= higher:
            return False
        left_is_valid = not node.left or is_valid_bst_bounded(
            node.left, lower, node.val
        )
        right_is_valid = not node.right or is_valid_bst_bounded(
            node.right, node.val, higher
        )
        return left_is_valid and right_is_valid

    return is_valid_bst_bounded(root, None, None)


if __name__ == "__main__":
    assert is_valid_bst(new_tree(2, 1, 3)) is True
    assert is_valid_bst(new_tree(5, 1, 4, None, None, 3, 6)) is False
    assert is_valid_bst(new_tree(10, 5, 15, None, None, 6, 20)) is False
    assert is_valid_bst(new_tree(0, None, -1)) is False
