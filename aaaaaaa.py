# 寻找前10大的数值
# 一个文件中，存放了数十万条数据，每行一条数据，从中选择出前10大的数值。

def find_num(path, k):
    num = 0
    e_num = 1
    fg_name = ""
    fl_name = ""
    with open(path, "r") as f:
        first = f.readline()
        fg_name = f"greater_than_{first}"
        fl_name = f"lower_than_{first}"
        with open(fg_name, "w") as fg:
            with open(fl_name, "w") as fl:
                while True:
                    item = f.readline()
                    if not item:
                        break
                    elif item > first:
                        fg.write(item)
                        num += 1
                    elif item < first:
                        fl.write(item)
                    else:
                        e_num += 1
                while num < k and e_num > 0:
                    fg.write(first)
                    num += 1
                    e_num -= 1
    return num, fg_name, fl_name


def find_top10(path, k):
    ret = []
    while k > 0:
        num, fg_name, fl_name = find_num(path, k)
        if num <= k:
            with open(fg_name, "r") as f:
                while True:
                    item = f.readline()
                    if not item:
                        break
                    ret.append(item)
                    k -= 1
        else:
            path = fl_name
    return ret


def find2(path, k):
    ret = []
    with open(path, "r") as f:
        while True:
            item = f.readline()
            if not item:
                break
            item = int(item[:-1])
            if not ret:
                ret.append(item)
            else:
                # flag = True
                # for i in range(len(ret)):
                #     if item > ret[i]:
                #         ret.insert(i, item)
                #         flag = False
                #         break
                # if flag:
                #     ret.append(item)
                start, end = 0, len(ret)
                while start < end:
                    mid = (start + end) // 2
                    if item <= ret[mid]:
                        start = mid + 1
                    else:
                        end = mid
                ret.insert(start, item)
                if len(ret) > k:
                    ret.pop()
    return ret


if __name__ == '__main__':
    path = "./1.txt"
    print(find2(path, 10))









