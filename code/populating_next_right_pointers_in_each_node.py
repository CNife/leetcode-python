from typing import Optional
from unittest import TestCase


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next_node: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next_node = next_node

    def __repr__(self):
        return (
            f"Node(val: {self.val}, "
            f"left: {self.left}, "
            f"right: {self.right}, "
            f"next: {self.next_node})"
        )


def connect(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None

    level = [root]
    while level:
        prev = None
        tmp = []
        for node in level:
            if prev is not None:
                prev.next_node = node
            prev = node
            if node.left and node.right:
                tmp.append(node.left)
                tmp.append(node.right)
        level = tmp
    return root


class Test(TestCase):
    def test_connect(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(7)

        connect(root)

        self.assertIsNone(root.next_node)
        self.assertIs(root.left.next_node, root.right)
        self.assertIsNone(root.right.next_node)
        self.assertIs(root.left.left.next_node, root.left.right)
        self.assertIs(root.left.right.next_node, root.right.left)
        self.assertIs(root.right.left.next_node, root.right.right)
        self.assertIsNone(root.right.right.next_node)
