from collections import deque
from typing import Optional


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
        self.next = next_node

    def __repr__(self):
        return (
            f"Node(val: {self.val}, "
            f"left: {self.left}, "
            f"right: {self.right}, "
            f"next: {self.next})"
        )


def connect(root: Node) -> Optional[Node]:
    if not root:
        return None

    queue, fake_head = deque(), Node(-1)
    queue.append(root)
    while queue:
        level_count = len(queue)
        node = fake_head
        for _ in range(level_count):
            node.next = queue.popleft()
            node = node.next
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        node.next = None
    return root


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.right = Node(7)

tree = connect(tree)

assert tree.next is None
assert tree.left.next is tree.right
assert tree.right.next is None
assert tree.left.left.next is tree.left.right
assert tree.left.right.next is tree.right.right
assert tree.right.right.next is None
