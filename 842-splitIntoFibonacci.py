"""
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
形式上，斐波那契式序列是一个非负整数列表 F，且满足：
0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
F.length >= 3；
对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

示例 1：
输入："123456579"
输出：[123,456,579]
示例 2：
输入: "11235813"
输出: [1,1,2,3,5,8,13]
"""

class Solution:
    def splitIntoFibonacci(self, S: str):
        if len(S) < 3:
            return []
        n = len(S)
        ret = []
        for i in range(1, n // 2 + 1):
            for j in range(1, n - i):
                ret.append(int(S[:i]))
                ret.append(int(S[i:i + j]))
                flag, ret = self.isF(S[i + j:], ret)
                if flag:
                    return ret
                if S[i: i + j] == "0":
                    break
            if S[0] == "0":
                break
        return ret if len(ret) > 2 else []

    def isF(self, S, ans):
        while S:
            temp = ans[-1] + ans[-2]
            if temp > 2 ** 31 - 1:
                return False, []
            if not S.startswith(str(temp)):
                return False, []
            ans.append(temp)
            S = S[len(str(temp)):]
        if len(ans) > 2:
            return True, ans
        return False, []

if __name__ == '__main__':
    s = Solution()
    S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    a = s.splitIntoFibonacci(S)
    print(a)
    for i in range(len(a) - 2):
        if a[i] + a[i + 1] != a[i + 2]:
            print(i)
