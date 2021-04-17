from typing import List

from leetcode import TreeNode, test, new_tree, sorted_list


def path_sum(root: TreeNode, target: int) -> List[List[int]]:
    if not root:
        return []

    stack, result, = (
        [],
        [],
    )

    def dfs(node: TreeNode, remaining: int) -> None:
        stack.append(node)
        if node.left or node.right:
            if node.left:
                dfs(node.left, remaining - node.val)
            if node.right:
                dfs(node.right, remaining - node.val)
        else:
            if node.val == remaining:
                path = [n.val for n in stack]
                result.append(path)
        stack.pop()

    dfs(root, target)
    return result


test(
    path_sum,
    [
        (
            new_tree(5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1),
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        )
    ],
    map_func=sorted_list,
)
