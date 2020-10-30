class Solution:
    def smallerNumbersThanCurrent(self, nums):
        if not nums:
            return []
        temp = [0] * 101
        for num in nums:
            temp[num] += 1
        for i in range(1, len(temp)):
            temp[i] = temp[i] + temp[i - 1]
        ret = [0] * len(nums)
        for i, num in enumerate(nums):
            ret[i] = temp[num - 1] if num else 0
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [5,0,10,0,10,6]
    print(s.smallerNumbersThanCurrent(nums))
