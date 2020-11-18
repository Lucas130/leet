"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder1(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            item = stack.pop(0)
            if not item:
                continue
            ret.append(item.val)
            stack.append(item.left)
            stack.append(item.right)
        return ret

    def levelOrder2(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        ret = [[]]
        while stack1 or stack2:
            if not stack1:
                stack1, stack2 = stack2, []
                ret.append([])
            item = stack1.pop(0)
            if not item:
                continue
            ret[-1].append(item.val)
            stack2.append(item.left)
            stack2.append(item.right)
        if ret[-1] == []:
            ret.pop()
        return ret

    def levelOrder3(self, root: TreeNode) -> list[list[int]]:
        # if not root:
        #     return []
        # stack = [root]
        # ret = []
        # while stack:
        #     ret.append([])
        #     for i in range(len(stack)):
        #         item = stack.pop(0)
        #         ret[-1].append(item.val)
        #         if item.left:
        #             stack.append(item.left)
        #         if item.right:
        #             stack.append(item.right)
        # return ret
        from collections import deque
        if not root:
            return []
        stack = deque([root])
        ret = []
        while stack:
            ret.append([])
            for i in range(len(stack)):
                item = stack.popleft()
                ret[-1].append(item.val)
                if item.left:
                    stack.append(item.left)
                if item.right:
                    stack.append(item.right)
        return ret



