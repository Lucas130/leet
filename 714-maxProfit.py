"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""
"""
1.当前股票价格prices[i] + fee < buy, 需要更低的价格prices[i] + fee 去买股票
2.当前股票价格 prices[i] > buy 说明有价值卖出，假设当前手上有一个prices[i]的股票，如果prices[i + 1] > prices[i],
则加上这一天的差价，相当于后一天卖出
3.如果buy位于[prices[i], prices[i] + fee]中，则说明没有买卖价值
"""


class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit


if __name__ == '__main__':
    s = Solution()
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    print(s.maxProfit(prices, fee))

