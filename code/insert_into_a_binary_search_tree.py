from leetcode import TreeNode, test, new_tree, inorder_traverse


def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    node, prev, is_left = root, None, False
    while node:
        prev = node
        if val < node.val:
            node, is_left = node.left, True
        else:
            node, is_left = node.right, False

    new_node = TreeNode(val)
    if prev is None:
        return new_node

    if is_left:
        prev.left = new_node
    else:
        prev.right = new_node
    return root


test(
    insert_into_bst,
    [(new_tree(4, 2, 7, 1, 3), 5, [1, 2, 3, 4, 5, 7]), (new_tree(), 1, [1])],
    equals_func=lambda actual, expect: inorder_traverse(actual) == expect,
)
