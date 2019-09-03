"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
最大连续子序列一定是以某个元素结尾的，那么我们就思考以nums中每个元素结尾的连续子序列其最大和是多少。
"""

class Solution:
    def maxSubArray(self, nums):
        # status = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i]+status[i-1] > nums[i]:
        #         status.append(nums[i]+status[i-1])
        #     else:
        #         status.append(nums[i])
        # return max(status)

        max_sum, cur_sum = float('-inf'), 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
