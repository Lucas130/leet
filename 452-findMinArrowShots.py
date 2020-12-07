"""
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。
"""
class Solution:
    def findMinArrowShots(self, points) -> int:
        # if not points:
        #     return 0
        # points.sort(key=lambda x:x[0])
        # temp = []
        # for i in points:
        #     flag = False
        #     for j in range(len(temp)):
        #         if i[0] in range(temp[j][0], temp[j][1] + 1) or temp[j][0] in range(i[0], i[1] + 1):
        #             temp[j].extend(i)
        #             temp[j] = sorted(temp[j])[1:3]
        #             flag = True
        #     if not flag:
        #         temp.append(i)
        # return len(temp)
        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        nums = 1
        temp = points[0]
        for i in points[1:]:
            if i[0] <= temp[1]:
                temp = [max(temp[0], i[0]), min(temp[1], i[1])]
            else:
                temp = i
                nums += 1

        return nums


if __name__ == '__main__':
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    s = Solution()
    print(s.findMinArrowShots(points))

