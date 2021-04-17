from leetcode import TreeNode, test, new_tree


def convert_bst(root: TreeNode) -> TreeNode:
    acc = 0

    def reversed_inorder(node: TreeNode) -> None:
        nonlocal acc
        if node:
            reversed_inorder(node.right)
            acc = node.val = acc + node.val
            reversed_inorder(node.left)

    reversed_inorder(root)
    return root


test(
    convert_bst,
    [
        (new_tree(5, 2, 13), new_tree(18, 20, 13)),
    ],
)
