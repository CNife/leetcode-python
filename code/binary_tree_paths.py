from leetcode import TreeNode, new_tree, sorted_equals


def binary_tree_path(root: TreeNode) -> list[str]:
    if not root:
        return []

    stack, results = [], []

    def helper(node: TreeNode) -> None:
        nonlocal stack, results

        stack.append(node.val)
        if not node.left and not node.right:
            results.append(list(stack))
        else:
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        stack.pop()

    helper(root)
    return ["->".join(str(val) for val in result) for result in results]


if __name__ == "__main__":
    tests = [
        (new_tree(1, 2, 3, None, 5), ["1->2->5", "1->3"]),
    ]
    for root, want in tests:
        assert sorted_equals(binary_tree_path(root), want)
