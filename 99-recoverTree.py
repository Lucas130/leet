"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.dfs(root)
        x, y = -1, -1
        for i in range(len(self.ret) - 1):
            if self.ret[i] > self.ret[i + 1]:
                y = i + 1
                if x == -1:
                    x = i
        self.ret[x].val, self.ret[y].val = self.ret[y].val, self.ret[x].val

    def __init__(self):
        self.ret = []

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.ret.append(root)
        self.dfs(root.right)
