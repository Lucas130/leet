"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
"""


class Solution:
    def maxProfit(self, prices) -> int:
        cur = float("inf")
        temp = list()
        for i in prices:
            if i < cur:
                cur = i
            else:
                temp.append(i - cur)
        if not prices or not temp:
            return 0
        return max(temp)


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 2, 3, 6, 1, 4, 4]
    # prices = []
    print(Solution().maxProfit(prices))
