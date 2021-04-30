from typing import Optional

from leetcode import TreeNode, new_tree


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    mid = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    if len(inorder) > 1:
        root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
        root.right = build_tree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root


if __name__ == "__main__":
    assert (
        build_tree(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
        )
        == new_tree(3, 9, 20, None, None, 15, 7)
    )
