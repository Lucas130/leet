"""
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        n = len(s)
        for i in range(n):
            if s[i] not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
            if mapping[s[i]] != t[i]:
                return False
        return True

if __name__ == '__main__':
   solution = Solution()
   s = "egg"
   t = "add"
   print(solution.isIsomorphic(s, t))