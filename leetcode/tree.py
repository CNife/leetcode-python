from collections import deque
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    """
    二叉树的节点。
    """

    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def new_tree(*nums: Optional[int]) -> Optional[TreeNode]:
    """
    创建二叉树。
    nums 会按照层序遍历的方式添加到树中，None 值会被跳过，并不会参与到下一层的构造中。
    [1, 2, None, None, 3, 4, 5] 构造为 (1 (2 None (3 4 5)) None)。

    :param nums: 节点值的列表，空值用 None 表示
    :return: 二叉树
    """
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = deque()
    queue.append(root)

    i = 1
    while i < len(nums):
        node = queue.popleft()
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if i < len(nums):
            if nums[i] is not None:
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i += 1
    return root


def is_valid_bst(root: TreeNode) -> bool:
    """
    判断 root 是不是合法的二叉搜索树。
    二叉搜索树的定义为
        1. 空树；
        2. 左子树和右子树都是二叉搜索树，同时左孩子的值不大于根的值，右孩子的值不小于根的值。

    :param root: 二叉树
    :return: root 是否是合法的二叉搜索树
    """
    if not root:
        return True
    if root.left and root.left.val > root.val:
        return False
    if root.right and root.right.val < root.val:
        return False
    return is_valid_bst(root.left) and is_valid_bst(root.right)


def height(root: TreeNode) -> int:
    """
    计算 root 的高。
    二叉树的高定义为：
        1. 空树的高为 0；
        2. 非空树的高为左子树与右子树中高度最大者的高加 1。

    :param root: 二叉树
    :return: root 的高
    """
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    root.height = max(left_height, right_height) + 1
    return root.height


def is_valid_avl(root: TreeNode) -> bool:
    """
    判断 root 是否是合法的 AVL 树。
    AVL 树定义为：
        1. AVL 树是二叉搜索树；
        2. AVL 树根节点的左右子树都是 AVL 树，且左右子树的高度差不大于 1。

    :param root: 二叉树
    :return: roo 是否是 AVL 树
    """
    if not root:
        return True
    if not is_valid_bst(root):
        return False
    return abs(height(root.left) - height(root.right)) <= 1


def inorder_traverse(root: TreeNode) -> List[int]:
    """
    中序遍历二叉树。

    :param root: 二叉树
    :return: 中序遍历的结果
    """
    result = []

    def inorder(node: TreeNode) -> None:
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result


def preorder_traverse(root: TreeNode) -> List[int]:
    """
    前序遍历二叉树。

    :param root: 二叉树
    :return: 前序遍历的结果
    """
    result = []

    def preorder(node: TreeNode) -> None:
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return result


def postorder_traverse(root: TreeNode) -> List[int]:
    """
    后序遍历二叉树。

    :param root: 二叉树
    :return: 后序遍历的结果
    """
    result = []

    def postorder(node: TreeNode) -> None:
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

    postorder(root)
    return result


def level_order_traverse(root: TreeNode) -> List[int]:
    """
    层序遍历二叉树。

    :param root: 二叉树
    :return: 层序遍历的结果
    """
    queue, result = deque(), []
    if root:
        queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
