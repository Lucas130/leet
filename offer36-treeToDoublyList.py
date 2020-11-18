"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:

    def treeToDoublyList(self, root):
        if not root:
            return root
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head

    def dfs(self, cur):
        if not cur:
            return
        self.dfs(cur.left)
        if self.pre:
            self.pre.right, cur.left = cur, self.pre
        else:
            self.head = cur
        self.pre = cur
        self.dfs(cur.right)
