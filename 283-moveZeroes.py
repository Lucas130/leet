"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 0
        while end < len(nums):
            if nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end += 1
            else:
                end += 1

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)

