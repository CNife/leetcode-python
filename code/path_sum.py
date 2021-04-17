from leetcode import TreeNode, test, new_tree


def has_path_sum(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return has_path_sum(root.left, target - root.val) or has_path_sum(
        root.right, target - root.val
    )


test(
    has_path_sum,
    [(new_tree(5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1), 22, True)],
)
