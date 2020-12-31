"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")
        if len(l) != len(pattern):
            return False
        mapping = {}
        for index, i in enumerate(pattern):
            if i not in mapping and l[index] not in mapping.values():
                mapping[i] = l[index]
            if l[index] != mapping.get(i, ""):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    pattern = "abba"
    st = "dog cat cat dog"
    print(s.wordPattern(pattern, st))