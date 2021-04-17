import sys
from typing import List

from leetcode import TreeNode, new_tree


def postorder_traversal(root: TreeNode) -> List[int]:
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


def postorder_traversal_recursively(root: TreeNode) -> List[int]:
    result = []

    def recurse(node: TreeNode) -> None:
        if node:
            recurse(node.left)
            recurse(node.right)
            result.append(node.val)

    recurse(root)
    return result


tests = [
    new_tree(1, None, 2, 3),
]
for tree in tests:
    expect = postorder_traversal_recursively(tree)
    actual = postorder_traversal(tree)
    if expect != actual:
        message = f"tree: {tree}\nactual: {actual}\nexpect: {expect}"
        print(message, file=sys.stderr)
        sys.exit(1)
