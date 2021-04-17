from typing import List

from leetcode import TreeNode, test, new_tree, sorted_list


def binary_tree_path(root: TreeNode) -> List[str]:
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


test(
    binary_tree_path,
    [
        (new_tree(1, 2, 3, None, 5), ["1->2->5", "1->3"]),
    ],
    map_func=sorted_list,
)
