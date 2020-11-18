"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
class Solution:
    def reconstructQueue(self, people):
        if not people:
            return []
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        ret = [people.pop(0)]
        while people:
            temp = people.pop(0)

            ret.insert(temp[1], temp)

        return ret


if __name__ == '__main__':
    s = Solution()
    people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    ret = s.reconstructQueue(people)
    print(ret)