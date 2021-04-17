from leetcode import TreeNode, new_tree


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    rv, pv, qv = root.val, p.val, q.val
    if pv > rv and qv > rv:
        return lowest_common_ancestor(root.right, p, q)
    elif pv < rv and qv < rv:
        return lowest_common_ancestor(root.left, p, q)
    else:
        return root


root1 = new_tree(6, 2, 8, 0, 4, 7, 9, None, None, 3, 5)
p1 = root1.left
q1 = root1.right
assert lowest_common_ancestor(root1, p1, q1) is root1

p2 = root1.left
q2 = root1.left.right
assert lowest_common_ancestor(root1, p2, q2) is p2
