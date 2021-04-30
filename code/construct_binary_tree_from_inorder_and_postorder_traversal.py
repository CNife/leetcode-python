from typing import Optional

from leetcode import TreeNode, new_tree


def build_tree(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    def helper(in_order: list[int], post_order: list[int]) -> Optional[TreeNode]:
        if in_order and post_order:
            root_val = post_order[-1]
            for root_offset, val in enumerate(in_order):
                if val == root_val:
                    break
            else:
                root_offset = 0

            root = TreeNode(root_val)
            root.left = helper(in_order[:root_offset], post_order[:root_offset])
            root.right = helper(in_order[root_offset + 1 :], post_order[root_offset:-1])
            return root

    return helper(inorder, postorder)


if __name__ == "__main__":
    assert (
        build_tree(
            [9, 3, 15, 20, 7],
            [9, 15, 7, 20, 3],
        )
        == new_tree(3, 9, 20, None, None, 15, 7)
    )
