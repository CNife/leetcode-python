from collections import deque
from typing import Optional

from leetcode import TreeNode, test, new_tree


def serialize(root: TreeNode) -> str:
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node is not None:
            queue.extend([node.left, node.right])
            result.append(str(node.val))
        else:
            result.append("null")
    while result and result[-1] == "null":
        result.pop()
    return ",".join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    nodes = map(
        lambda t: None if t in ("null", "") else TreeNode(int(t)), data.split(",")
    )
    root = next(nodes)
    if root is None:
        return None

    queue = deque([root])
    is_left = True
    node = None
    for next_node in nodes:
        if next_node:
            queue.append(next_node)
        if is_left:
            node = queue.popleft()
            node.left = next_node
        else:
            node.right = next_node
        is_left = not is_left
    return root


test(deserialize, [("1,2,3,null,null,4,5", new_tree(1, 2, 3, None, None, 4, 5))])
test(
    serialize,
    [
        (new_tree(1, 2, 3, None, None, 4, 5), "1,2,3,null,null,4,5"),
    ],
)
