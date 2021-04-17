from typing import List, Optional

from leetcode import TreeNode, new_tree, test


def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def helper(in_order: List[int], post_order: List[int]) -> Optional[TreeNode]:
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


test(
    build_tree,
    [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], new_tree(3, 9, 20, None, None, 15, 7)),
    ],
)
