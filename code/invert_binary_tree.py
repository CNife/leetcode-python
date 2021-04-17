from leetcode import TreeNode, test, new_tree


def invert_tree(root: TreeNode) -> TreeNode:
    def invert(node: TreeNode) -> None:
        node.left, node.right = node.right, node.left
        if node.left:
            invert(node.left)
        if node.right:
            invert(node.right)

    if root:
        invert(root)
    return root


test(
    invert_tree,
    [
        (new_tree(4, 2, 7, 1, 3, 6, 9), new_tree(4, 7, 2, 9, 6, 3, 1)),
    ],
)
