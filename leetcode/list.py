from typing import Optional, List


class ListNode:
    """
    单项链表的节点。
    """

    def __init__(self, val: int):
        """
        创建单项链表的节点。

        :param val: 节点的值
        """
        self.val: int = val
        self.next: Optional[ListNode] = None

    def __eq__(self, o: object) -> bool:
        return isinstance(o, ListNode) and self.val == o.val and self.next == o.next

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"

    def __repr__(self):
        return f"ListNode(val={self.val},next={self.next})"

    def __getitem__(self, index: int) -> "ListNode":
        node = self
        for _ in range(index):
            if node:
                node = node.next
            else:
                raise IndexError("index out of range")
        return node


def new_list(*nums: int) -> Optional[ListNode]:
    """
    创建一个值的顺序按照 nums 规定的单项链表。

    :param nums: 链表中的值
    :return: 链表
    """
    if nums:
        head = ListNode(nums[0])
        node = head
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next
        return head
    else:
        return None


def new_cycle_list(nums: List[int], cycle_entry_index: int) -> Optional[ListNode]:
    """
    创建有环的单项链表。

    :param nums: 链表中的值
    :param cycle_entry_index: 开始成环的索引位置
    :return: 链表
    """
    if cycle_entry_index >= len(nums) or cycle_entry_index < 0:
        raise IndexError("cycle entry index out of range")

    head = ListNode(nums[0])
    node, entry_node = head, head
    for i, num in enumerate(nums[1:]):
        node.next = ListNode(num)
        node = node.next
        if i + 1 <= cycle_entry_index:
            entry_node = entry_node.next
    node.next = entry_node
    return head
