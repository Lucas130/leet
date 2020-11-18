"""
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum(root)
        return self.ans

    def maxSum(self, root):
        if not root:
            return 0
        left = max(self.maxSum(root.left), 0)
        right = max(self.maxSum(root.right), 0)
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val

