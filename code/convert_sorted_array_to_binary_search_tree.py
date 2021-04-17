from typing import List, Optional

from leetcode import TreeNode, test, is_valid_avl


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    middle = len(nums) // 2
    root = TreeNode(nums[middle])
    root.left = sorted_array_to_bst(nums[:middle])
    root.right = sorted_array_to_bst(nums[middle + 1 :])
    return root


test(
    sorted_array_to_bst,
    [
        ([-10, -3, 0, 5, 9], None),
    ],
    equals_func=lambda root, _: is_valid_avl(root),
)
