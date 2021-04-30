from leetcode import ListNode, new_list, new_cycle_list


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


if __name__ == "__main__":
    assert has_cycle(new_cycle_list([3, 2, 0, -4], 1)) is True
    assert has_cycle(new_cycle_list([1, 2], 0)) is True
    assert has_cycle(new_list(1)) is False
    assert has_cycle(new_list(1, 2)) is False
