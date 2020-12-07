"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
"""
class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        n = len(nums)
        start, end = 0, n - 1
        ret = [-1, -1]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                left = self.dfs(nums, start, mid, target, 0)
                right = self.dfs(nums, mid, end, target, 1)
                ret = [left, right]
                break
        return ret

    def dfs(self, nums, start, end, target, use):
        while start < end:
            mid = (start + end) // 2 + use
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if use == 0:
                    end = mid
                else:
                    start = mid
        return start

if __name__ == '__main__':
    s = Solution()
    # nums = [5,7,7,8,8,10]
    nums = [8]
    target = 8
    print(s.searchRange(nums, target))
