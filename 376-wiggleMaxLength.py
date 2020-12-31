"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
示例 2:
输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
"""
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n
        ret = 1
        start, end = 0, 1
        flag = True
        while end < n:
            if ret == 1:
                if nums[end] > nums[start]:
                    ret += 1
                    flag = False
                    start = end
                elif nums[end] < nums[start]:
                    ret += 1
                    flag = True
                    start = end
            else:
                if flag and nums[end] > nums[start]:
                    ret += 1
                    flag = False
                elif not flag and nums[end] < nums[start]:
                    ret += 1
                    flag = True
                start = end
            end += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(s.wiggleMaxLength(nums))