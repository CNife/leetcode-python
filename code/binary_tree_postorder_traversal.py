from leetcode import TreeNode, new_tree


def postorder_traversal(root: TreeNode) -> list[int]:
    stack, result = [], []
    temp = root
    while temp or stack:
        if temp:
            result.append(temp.val)
            stack.append(temp)
            temp = temp.right
        else:
            temp = stack.pop().left

    result.reverse()
    return result


def postorder_traversal_recursively(root: TreeNode) -> list[int]:
    result = []

    def recurse(node: TreeNode) -> None:
        if node:
            recurse(node.left)
            recurse(node.right)
            result.append(node.val)

    recurse(root)
    return result


if __name__ == "__main__":
    trees = [
        new_tree(1, None, 2, 3),
    ]
    for tree in trees:
        assert postorder_traversal(tree) == postorder_traversal_recursively(tree)
