"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list()
        s_set = set()
        count = 0
        for item in s:
            if item not in s_set:
                s_set.add(item)
                s_list.append(item)
            else:
                if not s_list:
                    s_list.append(item)
                    continue
                if s_list[-1] == item:
                    s_list.append(item)
                else:
                    count = len(s_list) if len(s_list) > count else count
                    s_list = [item]
        return count

if __name__ == '__main__':
    s = Solution()
    st = "abcabcbb"
    print(s.lengthOfLongestSubstring(st))