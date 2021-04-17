from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """
    单项链表的节点。
    """
    val: int
    next: Optional["ListNode"] = None

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"


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


def new_cycle_list(nums: list[int], cycle_entry_index: int) -> Optional[
    ListNode]:
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
