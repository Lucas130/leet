"""
给定一个二叉树，返回它的中序 遍历。
递归算法很简单，你可以通过迭代算法完成吗？
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        stack = []
        ret = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root.val)
            root = root.right
        return ret

