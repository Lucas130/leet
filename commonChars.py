"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。
"""
class Solution:
    def commonChars(self, A):
        minfreq = [float("inf")] * 26
        for word in A:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord("a")] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], temp[i])
        ans = []
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans

if __name__ == '__main__':
    A = ["bella","label","roller"]
    s = Solution()
    print(s.commonChars(A))