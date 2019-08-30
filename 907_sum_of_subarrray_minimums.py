"""
归纳法可以直到每个元素 A[i] 被加入到最终结果的次数为其左邻居中大于它、右邻居中不小于它的元素长度 left 、 right （包括自身）的乘积。
"""
class Solution:
    def sumSubarrayMins(self, A: [int]) -> int:
        stack = []
        sum = 0
        A.insert(0, 0)
        A.append(0)
        for i in range(len(A)):
            while stack and A[i] < A[stack[-1]]:
                out = stack.pop(-1)
                print((out - stack[-1]), (i - out), A[out], (out - stack[-1]) * (i - out) * A[out])
                sum += (out - stack[-1]) * (i - out) * A[out]
            stack.append(i)
        return sum % (pow(10, 9) + 7)


if __name__ == '__main__':
    s = Solution()
    A = [3, 1, 2, 4]
    re=s.sumSubarrayMins(A)
    print(re)