"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
例如:
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
输出:
2
"""
import collections


class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        mapping = collections.Counter(i + j for i in A for j in B)
        ans = 0
        for k in C:
            for l in D:
                if - k - l in mapping:
                    ans += mapping[- k - l]
        return ans

if __name__ == '__main__':
    s = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(s.fourSumCount(A,B,C,D))