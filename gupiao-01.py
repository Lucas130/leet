def min_num(l):
    l.sort()
    num = 1
    flag = False
    for i in l:
        if i < num:
            continue
        elif i > num:
            return num
        else:
            flag = True
            num += 1
    return num if flag else -1

def max_huiche(prices):
    ret = [0, 0, 0]
    start, end, num = 0, 1, 0
    for i in range(1, len(prices)):
        if i == start +1 and prices[i] - prices[i - 1] > 0:
            start += 1
            ret[1] = start
            continue
        if prices[start] - prices[i] > num:
            num = prices[start] - prices[i]
            ret[0] = num
            ret[2] = i
            continue
        if prices[i] > prices[start]:
            ret[1] = start
            start = i
    if ret[1] >= ret[2]:
         return []
    return ret


if __name__ == '__main__':
    # l = [2,3,4,1,10,8,5,11,4]
    l=[3,5,1]
    # print(min_num(l))
    print(max_huiche(l))