"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = [0] * 26
        for i in s:
            s_list[ord(i) - ord("a")] += 1
        for j in t:
            s_list[ord(j) - ord("a")] -= 1
        for i in range(26):
            if s_list[i] != 0:
                return False
        return True