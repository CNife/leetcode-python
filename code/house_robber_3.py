from leetcode import test, TreeNode, new_tree


def rob(root: TreeNode) -> int:
    def helper(node: TreeNode) -> (int, int):
        if not node:
            return 0, 0
        left_max, left_no_rob = helper(node.left)
        right_max, right_no_rob = helper(node.right)
        return (
            max(left_no_rob + right_no_rob + node.val, left_max + right_max),
            left_max + right_max,
        )

    return helper(root)[0]


test(rob, [(new_tree(3, 4, 5, 1, 3, None, 1), 9)])
