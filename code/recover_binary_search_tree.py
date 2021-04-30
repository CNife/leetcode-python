from leetcode import TreeNode, new_tree


def recover_tree(root: TreeNode) -> None:
    if not root:
        return

    prev = TreeNode(-(2 ** 31) - 1)
    first_error, second_error = None, None

    def inorder(node: TreeNode) -> None:
        nonlocal prev, first_error, second_error
        if node.left:
            inorder(node.left)
        if prev.val >= node.val and not first_error:
            first_error = prev
        if prev.val >= node.val and first_error:
            second_error = node
        prev = node
        if node.right:
            inorder(node.right)

    inorder(root)
    first_error.val, second_error.val = second_error.val, first_error.val


if __name__ == "__main__":
    tests = [
        (new_tree(1, 3, None, None, 2), new_tree(3, 1, None, None, 2)),
        (new_tree(3, 1, 4, None, None, 2), new_tree(2, 1, 4, None, None, 3)),
        (new_tree(5, 3, 9, -2147483648, 2), new_tree(5, 2, 9, -2147483648, 3)),
    ]
    for root, want in tests:
        recover_tree(root)
        assert root == want
