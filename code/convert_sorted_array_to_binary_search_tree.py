from typing import Optional

from leetcode import TreeNode, is_valid_avl


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    middle = len(nums) // 2
    root = TreeNode(nums[middle])
    root.left = sorted_array_to_bst(nums[:middle])
    root.right = sorted_array_to_bst(nums[middle + 1 :])
    return root


if __name__ == "__main__":
    assert is_valid_avl(sorted_array_to_bst([-10, -3, 0, 5, 9]))
