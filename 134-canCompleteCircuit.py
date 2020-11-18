"""
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
说明: 
如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
"""
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if not gas:
            return -1
        start, cur, total = 0, 0, 0
        for i in range(len(gas)):
            cur = cur + gas[i] - cost[i]
            total = total + gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i + 1
        if total < 0 or start > len(gas) - 1:
            return -1
        return start
        # dp = [i - j for i, j in zip(gas, cost)]
        # if sum(dp) < 0:
        #     return -1
        # temp = []
        # num = 0
        # ret = 0
        # for index, i in enumerate(dp):
        #     num += i
        #     if num < 0:
        #         temp.append(num)
        #         num = 0
        #         ret = index + 1
        # for i in temp:
        #     num += i
        #     if num < 0:
        #         return -1
        # return ret




if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()
    a = s.canCompleteCircuit(gas, cost)
    print(a)
