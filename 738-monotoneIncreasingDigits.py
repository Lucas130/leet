"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        ret = []
        while N:
            temp = N % 10
            N = N // 10
            ret.insert(0, temp)
        flag = False
        for i in range(1, len(ret)):
            if flag:
                ret[i] = 9
            elif ret[i] < ret[i - 1]:
                while i > 0 and ret[i] < ret[i - 1]:
                    ret[i] = 9
                    ret[i - 1] -= 1
                    i -= 1
                flag = True
        ans = 0
        for i in ret:
            ans *= 10
            ans += i
        return ans


if __name__ == '__main__':
    s = Solution()
    N = 2034
    print(s.monotoneIncreasingDigits(N))
