"""
给定 pushed 和 popped 两个序列，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。
"""


class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        i = 0
        # while pushed or stack:
        #     if not stack or stack[-1] != popped[i]:
        #         if pushed:
        #             stack.append(pushed.pop(0))
        #         else:
        #             return False
        #     else:
        #         stack.pop()
        #         i += 1
        #         if i == len(popped):
        #             return True
        # return False if stack else True

        for p in pushed:
            if p != popped[i]:
                stack.append(p)
            else:
                i += 1
                while stack and stack[-1] == popped[i]:
                    i += 1
                    stack.pop()
                if i > len(popped) - 1:
                    break

        return False if stack else True


if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]

    print(Solution().validateStackSequences(pushed, popped))
