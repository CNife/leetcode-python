from leetcode import ListNode, test, new_list, new_cycle_list


def has_cycle(head: ListNode) -> bool:
    if not head:
        return False

    slow, fast = head, head.next
    while slow and fast:
        if slow is fast:
            return True
        slow, fast = slow.next, fast.next
        if fast:
            fast = fast.next
    return False


test(
    has_cycle,
    [
        (new_cycle_list([3, 2, 0, -4], 1), True),
        (new_cycle_list([1, 2], 0), True),
        (new_list(1), False),
        (new_list(1, 2), False),
    ],
)
