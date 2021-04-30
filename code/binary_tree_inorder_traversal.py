from leetcode import TreeNode, new_tree


def inorder_traversal(root: TreeNode) -> list[int]:
    stack, result = [], []

    def push_node(node: TreeNode) -> None:
        while node:
            stack.append(node)
            node = node.left

    push_node(root)
    while stack:
        p = stack.pop()
        result.append(p.val)
        push_node(p.right)
    return result


if __name__ == "__main__":
    assert inorder_traversal(new_tree(1, None, 2, 3)) == [1, 3, 2]
