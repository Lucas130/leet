"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ret = s[0]
        n = len(s)
        for i in range(0, n - 1):
            start, end = i, i
            while start > 0 and end < n - 1:
                if s[start - 1] != s[end + 1]:
                    break
                start -= 1
                end += 1
            if end - start + 1 > len(ret):
                ret = s[start:end + 1]
            start, end = i, i + 1
            if s[start] == s[end]:
                while start > 0 and end < n - 1:
                    if s[start - 1] != s[end + 1]:
                        break
                    start -= 1
                    end += 1
                if end - start + 1 > len(ret):
                    ret = s[start:end + 1]
        return ret

if __name__ == '__main__':
    s = Solution()
    m = "b"
    print(s.longestPalindrome(m))
