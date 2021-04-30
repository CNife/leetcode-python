from leetcode import TreeNode, new_tree


def sum_of_left_leaves(root: TreeNode) -> int:
    def helper(node: TreeNode, is_left: bool) -> int:
        if node:
            if node.left or node.right:
                return helper(node.left, True) + helper(node.right, False)
            elif is_left:
                return node.val
        return 0

    return helper(root, False)


if __name__ == "__main__":
    assert sum_of_left_leaves(new_tree(3, 9, 20, None, None, 15, 7)) == 24
