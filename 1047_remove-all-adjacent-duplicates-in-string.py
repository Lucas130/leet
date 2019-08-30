class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for e in S:
            if stack and stack[-1] == e:
                stack.pop()
            else:
                stack.append(e)
        return "".join(stack)


if __name__ == '__main__':
    S = "abbcddcaca"
    print(Solution().removeDuplicates(S))
