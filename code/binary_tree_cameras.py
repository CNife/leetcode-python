from leetcode import TreeNode, test, new_tree


def min_camara_cover(root: TreeNode) -> int:
    result = 0

    def lrd(node: TreeNode) -> int:
        nonlocal result
        if not node:
            return 1
        left, right = lrd(node.left), lrd(node.right)
        if left == 0 or right == 0:
            result += 1
            return 2
        if left == 1 and right == 1:
            return 0
        return 1

    if lrd(root) == 0:
        result += 1
    return result


test(
    min_camara_cover,
    [
        (new_tree(0, 0, None, 0, 0), 1),
        (new_tree(0, 0, None, 0, None, 0, None, None, 0), 2),
    ],
)
