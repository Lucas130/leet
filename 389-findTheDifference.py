"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapping = [0] * 26
        for i in s:
            mapping[ord(i) - ord("a")] += 1
        for i in t:
            mapping[ord(i) - ord("a")] -= 1
        for i in range(26):
            if mapping[i] == -1:
                return chr(i + ord("a"))
        return ""

if __name__ == '__main__':
    s = Solution()
    st = "abcd"
    t = "abcde"
    print(s.findTheDifference(st, t))