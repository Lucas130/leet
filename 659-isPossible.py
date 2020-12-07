"""
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
"""
import collections


class Solution:
    def isPossible(self, nums):
        mapping = collections.Counter(nums)
        end_map = collections.Counter()
        for i in nums:
            if mapping.get(i, 0) > 0:
                if end_map.get(i - 1, 0) > 0:
                    mapping[i] -= 1
                    end_map[i - 1] -= 1
                    end_map[i] += 1
                else:
                    if mapping.get(i + 1, 0) > 0 and mapping.get(i + 2, 0) > 0:
                        mapping[i] -= 1
                        mapping[i + 1] -= 1
                        mapping[i + 2] -= 1
                        end_map[i + 2] += 1
                    else:
                        return False
        return True

if __name__ == '__main__':
    nums = [1,2,3,3,4,5]
    s = Solution()
    print(s.isPossible(nums))

