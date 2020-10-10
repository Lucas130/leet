class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        num_map = dict()
        for i, v in enumerate(nums):
            if v in num_map.keys():
                return [num_map[v], i]
            num_map[target - v] = i
        return []

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    print(s.twoSum(nums, 9))