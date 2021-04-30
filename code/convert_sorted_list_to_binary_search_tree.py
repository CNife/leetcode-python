from typing import Optional

from leetcode import ListNode, TreeNode, new_list, is_valid_avl


def sorted_list_to_bst(head: Optional[ListNode]) -> Optional[TreeNode]:
    length = list_length(head)
    if length <= 0:
        return None

    def build_bst(start: int, end: int) -> Optional[TreeNode]:
        nonlocal head
        if start > end:
            return None
        middle = (start + end) // 2
        left = build_bst(start, middle - 1)
        root = TreeNode(head.val)
        root.left = left
        head = head.next
        root.right = build_bst(middle + 1, end)
        return root

    return build_bst(0, length - 1)


def list_length(list_head: Optional[ListNode]) -> int:
    node, length = list_head, 0
    while node:
        length += 1
        node = node.next
    return length


if __name__ == "__main__":
    assert is_valid_avl(sorted_list_to_bst(new_list(-10, 3, 0, 5, 9)))
    assert is_valid_avl(sorted_list_to_bst(new_list()))
