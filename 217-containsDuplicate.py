"""
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:
输入: [1,2,3,1]
输出: true
"""
import collections


class Solution:
    def containsDuplicate(self, nums) -> bool:
        mapping = {}
        for i in nums:
            if mapping.get(i, 0) == 1:
                return True
            else:
                mapping[i] = 1
        return False

        # mapping = collections.Counter(nums)
        # if max(mapping.values()) > 1:
        #     return True
        # return False