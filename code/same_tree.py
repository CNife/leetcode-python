from leetcode import TreeNode, test, new_tree


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


test(
    is_same_tree,
    [
        (new_tree(1, 2, 3), new_tree(1, 2, 3), True),
        (new_tree(1, None, 2), new_tree(1, 2), False),
        (new_tree(1, 2, 1), new_tree(1, 1, 2), False),
    ],
)
