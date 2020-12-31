"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution:
    def groupAnagrams(self, strs):
        mapping = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in mapping:
                mapping[key].append(i)
            else:
                mapping[key] = [i]
        return list(mapping.values())

if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))