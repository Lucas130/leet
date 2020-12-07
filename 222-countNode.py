"""
给出一个完全二叉树，求出该树的节点个数。
说明：
完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        cur = root
        while cur.left:
            level += 1
            cur = cur.left

        low = 1 << level
        high = (1 << (level + 1)) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if self.exists(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low

    def exists(self, root, level, mid):
        i = 1 << (level - 1)
        cur = root
        while cur and i > 0:
            if i & mid:
                cur = cur.right
            else:
                cur = cur.left
            i = i >> 1
        return True if cur else False
