"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # temp = [1, 2]
        # for i in range(2, n):
        #     temp.append(temp[i - 1] + temp[i - 2])
        # return temp[n - 1]

        a = b = 1
        if n <= 1:
            return b
        for i in range(2, n + 1):
            a, b = b, a+b
        return b

if __name__ == '__main__':
    n = 5
    print(Solution().climbStairs(n))