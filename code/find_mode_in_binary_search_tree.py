from typing import List

from leetcode import TreeNode, test, new_tree


def find_mode(root: TreeNode) -> List[int]:
    result, values, prev_value, count, max_count = [], [], 0, 0, 0

    def update() -> None:
        nonlocal prev_value, count, max_count
        max_count = max(max_count, count)
        values.append((prev_value, count))

    def inorder(node: TreeNode) -> None:
        nonlocal prev_value, count, max_count
        if not node:
            return
        inorder(node.left)
        if node.val == prev_value:
            count += 1
        else:
            update()
            prev_value, count = node.val, 1
        inorder(node.right)

    inorder(root)
    update()
    for value, count in values:
        if count > 0 and count == max_count:
            result.append(value)
    return result


test(find_mode, [(new_tree(1, None, 2, 2), [2]), (new_tree(0), [0])])
