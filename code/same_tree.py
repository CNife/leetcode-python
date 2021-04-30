from leetcode import TreeNode, new_tree


def is_same_tree(lhs: TreeNode, rhs: TreeNode) -> bool:
    if lhs is None:
        return rhs is None
    elif rhs is None:
        return False
    else:
        return (
            lhs.val == rhs.val
            and is_same_tree(lhs.left, rhs.left)
            and is_same_tree(lhs.right, rhs.right)
        )


if __name__ == "__main__":
    assert is_same_tree(new_tree(1, 2, 3), new_tree(1, 2, 3)) is True
    assert is_same_tree(new_tree(1, None, 2), new_tree(1, 2)) is False
    assert is_same_tree(new_tree(1, 2, 1), new_tree(1, 1, 2)) is False
