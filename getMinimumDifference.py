"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.dif = float("inf")
        self.pre = None
        self.traversal(root)
        return self.dif

    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        if self.pre == None:
            self.pre = root.val
        else:
            self.dif = min(self.dif, abs(root.val - self.pre))
            self.pre = root.val
        self.traversal(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    s = Solution()
    print(s.getMinimumDifference(root))
