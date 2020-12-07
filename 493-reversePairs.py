"""
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
你需要返回给定数组中的重要翻转对的数量。

示例 1:
输入: [1,3,2,3,1]
输出: 2
"""
class Solution:
    def reversePairs(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        mid = len(nums) // 2
        n1 = nums[:mid]
        n2 = nums[mid:]
        ret = self.reversePairs(n1) + self.reversePairs(n2)

        i = 0
        for j in n1:
            while i < len(n2) and j > 2 * n2[i]:
                i += 1
            ret += i

        p1, p2 = 0, 0
        for i in range(len(nums)):
            if p1 < len(n1) and (p2 == len(n2) or n1[p1] < n2[p2]):
                nums[i] = n1[p1]
                p1 += 1
            else:
                nums[i] = n2[p2]
                p2 += 1
        return ret

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,2,3,1]
    nums.sor
    print(s.reversePairs(nums))


