"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, len(occ))
        return ans

if __name__ == '__main__':
    s = Solution()
    st = "pwwkew"
    print(s.lengthOfLongestSubstring(st))