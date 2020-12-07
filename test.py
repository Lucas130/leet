def get_area(lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2):
    x = y = 0
    list_x1 = [lx1, rx1] if lx1 < rx1 else [rx1, lx1]
    list_x2 = [lx2, rx2] if lx2 < rx2 else [rx2, lx2]
    list_y1 = [ly1, ry1] if ly1 < ry1 else [ry1, ly1]
    list_y2 = [ly2, ry2] if ly2 < ry2 else [ry2, ly2]
    if list_x1[0] in range(list_x2[0], list_x1[1]) or list_x2[0] in range(list_x1[0], list_x1[1]):
        list_x1.extend(list_x2)
        list_x1.sort()
        x = list_x1[2] - list_x1[1]
    if list_y1[0] in range(list_y2[0], list_y2[1]) or list_y2[0] in range(list_y1[0], list_y1[1]):
        list_y1.extend(list_y2)
        list_y1.sort()
        y = list_y1[2] - list_y1[1]
    return x * y
if __name__ == '__main__':
    print(get_area(1,7,10,3,2,6,5,0))
    print(get_area(-3,0,0,-3,2,5,4,3))
    print(get_area(1,5,6,2,4,4,7,1))
