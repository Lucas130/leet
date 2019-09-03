"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        for i in range(len(nums)):
            if i == 0:
                continue
            self.nums[i] = self.nums[i] + self.nums[i - 1]

    def sumRange(self, i, j):
        if i > 0:
            return self.nums[j] - self.nums[i - 1]
        return self.nums[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sumRange(2,5))
