from typing import List, Dict, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: List["Node"] = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

    def __repr__(self) -> str:
        return f"Node({self.val}, {len(self.neighbors)} neighbors)"


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return node

    cloned: Dict[int, Node] = {}

    def clone_node(old: Node) -> Node:
        new = Node(old.val)
        cloned[new.val] = new
        for neighbor in old.neighbors:
            new_neighbor = cloned.get(neighbor.val)
            if new_neighbor is None:
                new_neighbor = clone_node(neighbor)
            new.neighbors.append(new_neighbor)
        return new

    result = clone_node(node)
    # print(cloned)
    return result


src_nodes = [Node(i + 1) for i in range(4)]
src_nodes[0].neighbors.extend([src_nodes[1], src_nodes[3]])
src_nodes[1].neighbors.extend([src_nodes[0], src_nodes[2]])
src_nodes[2].neighbors.extend([src_nodes[1], src_nodes[3]])
src_nodes[3].neighbors.extend([src_nodes[0], src_nodes[2]])

got = clone_graph(src_nodes[0])
# print(src_nodes, got)
