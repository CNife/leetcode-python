import random
from dataclasses import dataclass
from typing import Optional


class SkipList:
    def __init__(self):
        self.head: Node = Node(-1, None, None)

    def search(self, target: int) -> bool:
        ptr = self.head
        while ptr:
            while ptr.right and ptr.right.val < target:
                ptr = ptr.right
            if not ptr.right or ptr.right.val > target:
                ptr = ptr.down
            else:
                return True
        return False

    def add(self, num: int) -> None:
        path, ptr = [], self.head
        while ptr:
            while ptr.right and ptr.right.val < num:
                ptr = ptr.right
            path.append(ptr)
            ptr = ptr.down

        insert_up, down = True, None
        while insert_up and path:
            insert = path.pop()
            insert.right = Node(num, insert.right, down)
            down = insert.right
            insert_up = bool(random.randrange(2))

        if insert_up:
            self.head = Node(-1, Node(num, None, down), self.head)

    def erase(self, num: int) -> bool:
        ptr, seen = self.head, False
        while ptr:
            while ptr.right and ptr.right.val < num:
                ptr = ptr.right
            if not ptr.right or ptr.right.val > num:
                ptr = ptr.down
            else:
                seen = True
                ptr.right = ptr.right.right
                ptr = ptr.down
        return seen


@dataclass
class Node:
    val: int
    right: Optional["Node"]
    down: Optional["Node"]


sl = SkipList()
sl.add(1)
sl.add(2)
sl.add(3)
assert sl.search(0) is False
sl.add(4)
assert sl.search(1) is True
assert sl.erase(0) is False
assert sl.erase(1) is True
assert sl.search(1) is False
