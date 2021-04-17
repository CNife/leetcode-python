from typing import Optional

from leetcode import ListNode, test, new_list


def detect_cycle(head: ListNode) -> Optional[ListNode]:
    def find_cycle():
        fast, slow = head, head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next
            if fast is slow:
                return slow
        return None

    p1, p2 = head, find_cycle()
    if not p2:
        return None
    while p1 is not p2:
        p1, p2 = p1.next, p2.next
    return p1


# noinspection DuplicatedCode
def _test_case(nums, cycle_entry_index):
    head = ListNode(nums[0])
    node, entry_node = head, head
    for i, num in enumerate(nums[1:]):
        node.next = ListNode(num)
        node = node.next
        if i + 1 <= cycle_entry_index:
            entry_node = entry_node.next
    node.next = entry_node
    return head, entry_node


test(
    detect_cycle,
    [
        _test_case([3, 2, 0, -4], 1),
        _test_case([1, 2], 0),
        (new_list(1), None),
    ],
    equals_func=lambda lhs, rhs: lhs.val == rhs.val
    if lhs and rhs
    else lhs is None and rhs is None,
)
