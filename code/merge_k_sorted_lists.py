from collections import namedtuple
from heapq import heappush, heapreplace, heappop
from typing import Optional

from leetcode import ListNode, new_list


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    tops: list[CmpListNode] = []
    for node in lists:
        if node is not None:
            heappush(tops, CmpListNode(node))

    head = ListNode(-1)
    tail = head
    while tops:
        tail.next = tops[0].node
        tail = tail.next
        if tail.next is not None:
            heapreplace(tops, CmpListNode(tail.next))
        else:
            heappop(tops)

    return head.next


CmpListNode = namedtuple("CmpListNode", ["node"])


def cmp_list_node_lt(lhs, rhs):
    return lhs.node.val < rhs.node.val


CmpListNode.__slots__ = ()
CmpListNode.__lt__ = cmp_list_node_lt

if __name__ == "__main__":
    assert merge_k_lists(
        [new_list(1, 4, 5), new_list(1, 3, 4), new_list(2, 6)]
    ) == new_list(1, 1, 2, 3, 4, 4, 5, 6)
