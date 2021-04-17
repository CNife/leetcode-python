from leetcode import ListNode, test, new_list


def reverse_group(head: ListNode, k: int) -> ListNode:
    if not head or k < 2:
        return head

    dummy = ListNode(-1)
    dummy.next = head

    pre, end = dummy, dummy
    while end.next:
        for _ in range(k):
            if end:
                end = end.next
            else:
                break
        if not end:
            return dummy.next

        start, nxt, end.next = pre.next, end.next, None
        pre.next = reverse_list(start)
        start.next, pre, end = nxt, start, start

    return dummy.next


def reverse_list(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev


test(
    reverse_group,
    [
        (new_list(1, 2, 3, 4, 5), 2, new_list(2, 1, 4, 3, 5)),
        (new_list(1, 2, 3, 4, 5), 3, new_list(3, 2, 1, 4, 5)),
    ],
)
