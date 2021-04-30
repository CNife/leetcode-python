from leetcode import ListNode, new_list


def remove_duplicate_nodes(head: ListNode) -> ListNode:
    values = set()
    prev, node = None, head
    while node:
        if node.val not in values:
            prev = node
            values.add(node.val)
        else:
            prev.next = node.next
        node = node.next
    return head


if __name__ == "__main__":
    assert remove_duplicate_nodes(new_list(1, 2, 3, 3, 2, 1)) == new_list(1, 2, 3)
    assert remove_duplicate_nodes(new_list(1, 1, 1, 2)) == new_list(1, 2)
