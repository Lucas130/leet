"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
"""

class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        ret = [0] * k
        n1, n2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if k - i > n2 or i > n1:
                continue
            l1 = self.get_max(nums1, i)
            l2 = self.get_max(nums2, k - i)
            max_list = self.merge(l1, l2)
            if self.compare(max_list, 0, ret, 0):
                ret = max_list
        return ret

    def get_max(self, nums, k):
        stack = []
        top = -1
        while k > 0:
            top += 1
            for i in range(top, len(nums) - k + 1):
                if nums[i] > nums[top]:
                    top = i
            stack.append(nums[top])
            k -= 1
        return stack

    def merge(self, nums1, nums2):
        stack = []
        n1, n2 = len(nums1), len(nums2)
        s1, s2 = 0, 0
        while s1 < n1 or s2 < n2:
            if s1 >= n1:
                stack.extend(nums2[s2:])
                break
            if s2 >= n2:
                stack.extend(nums1[s1:])
                break
            if self.compare(nums1, s1, nums2, s2):
                stack.append(nums1[s1])
                s1 += 1
            else:
                stack.append(nums2[s2])
                s2 += 1
        return stack

    def compare(self, nums1, i1, nums2, i2):
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 and i2 < n2:
            if nums1[i1] > nums2[i2]:
                return True
            elif nums1[i1] < nums2[i2]:
                return False
            else:
                i1 += 1
                i2 += 1
        if i1 == n1:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    # nums1 = [6, 7]
    # nums2 = [6, 0, 4]
    k = 5
    # nums1 = [1, 2]
    # nums2 = []
    # k = 2
    # nums1 = [2, 5, 6, 4, 4, 0]
    # nums2 = [7, 3, 8, 0, 6, 5, 7, 6, 2]
    # k = 15
    # nums1 = [8, 9]
    # nums2 = [3, 9]
    # k = 3
    nums1 = [2, 8, 0, 4, 5, 1, 4, 8, 9, 9, 0, 8, 2, 9]
    nums2 = [5, 9, 6, 6, 4, 1, 0, 7]
    k = 22
    print(s.maxNumber(nums1, nums2, k))