"""
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:
输入: S = "aab"
输出: "aba"
"""
import collections


class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        mapping = collections.Counter(S)
        max_num = max(mapping.values())
        if max_num > (n + 1) // 2:
            return ""
        ret = [""] * n
        first, second = 0, 1
        half = n // 2
        for c, count in mapping.items():
            while count in range(1, half + 1) and second < n:
                ret[second] = c
                second += 2
                count -= 1
            while count > 0:
                ret[first] = c
                first += 2
                count -= 1
        return "".join(ret)

if __name__ == '__main__':
    s = Solution()
    S = "aaabl"
    print(s.reorganizeString(S))
