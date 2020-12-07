"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = [0] * 52
        for i in s:
            l[ord(i) - ord("a")] += 1
        ret = 0
        flag = True
        for i in l:
            if i % 2 == 0:
                ret += i
            else:
                ret += i - 1
                if flag:
                    ret += 1
                    flag = False
        return ret

if __name__ == '__main__':
    s = Solution()
    m = "ccc"
    print(s.longestPalindrome(m))