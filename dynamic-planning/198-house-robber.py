"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""


class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        temp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            temp.append(max(temp[i - 1], temp[i - 2] + nums[i]))
        return max(temp)


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
