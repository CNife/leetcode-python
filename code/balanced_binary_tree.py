from leetcode import TreeNode, test, new_tree


def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True
    if not (is_balanced(root.left) and is_balanced(root.right)):
        return False
    left_height = root.left.val if root.left else 0
    right_height = root.right.val if root.right else 0
    root.val = max(left_height, right_height) + 1
    return -1 <= left_height - right_height <= 1


test(
    is_balanced,
    [
        (new_tree(3, 9, 20, None, None, 15, 7), True),
        (new_tree(1, 2, 2, 3, 3, None, None, 4, 4), False),
    ],
)
