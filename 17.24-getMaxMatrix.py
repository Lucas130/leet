"""
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例：
输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵
"""


class Solution:
    def getMaxMatrix(self, matrix):
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return []
        n, m = len(matrix), len(matrix[0])
        ret = float("-inf")
        ans = [0, 0, 0, 0]
        for i in range(n):
            nums = [[0] * m for _ in range(n - i)]
            nums[0] = matrix[i].copy()
            for j in range(i, n):
                for k in range(m):
                    if j - i > 0:
                        nums[j - i][k] = nums[j - i - 1][k] + matrix[j][k]
                temp, start, end = self.get_max_sub(nums[j - i].copy())
                if temp > ret:
                    ret = temp
                    ans = [i, start, j, end]
        return ans

    def get_max_sub(self, nums):
        ans = nums[0]
        start, end = 0, 0
        first = 0
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]
            else:
                first = i
            if nums[i] > ans:
                start = first
                end = i
                ans = nums[i]
        return ans, start, end

if __name__ == '__main__':
    s = Solution()
    # matrix = [
    #     [-3, 5, -1, 5],
    #     [2, 4, -2, 4],
    #     [-1, 3, -1, 3]
    # ]
    # matrix = [
    #    [-1,0],
    #    [0,-1]
    # ]
    matrix = [
        [9,-8,1,3,-2],
        [-3,7,6,-2,4],
        [6,-4,-4,8,-7]
    ]
    # [0, 0, 2, 3]
    # matrix = [[1, -3], [-4, 9]]

    print(s.getMaxMatrix(matrix))
