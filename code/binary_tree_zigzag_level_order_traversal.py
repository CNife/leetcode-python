from leetcode import new_tree, TreeNode


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    level = [root]
    result = []
    reverse = False

    while level:
        values = [node.val for node in level]
        if reverse:
            values.reverse()
        reverse = not reverse
        result.append(values)

        tmp = []
        for node in level:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        level = tmp

    return result


if __name__ == "__main__":
    assert zigzag_level_order(new_tree(3, 9, 20, None, None, 15, 7)) == [
        [3],
        [20, 9],
        [15, 7],
    ]
