"""
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ret = None
        while head:
            temp = head
            head = head.next
            temp.next = None
            if not ret:
                ret = temp
                ret.next = None
            elif temp.val < ret.val:
                temp.next = ret
                ret = temp
            else:
                cur = ret
                flag = False
                while cur.next:
                    if temp.val < cur.next.val:
                        item = cur.next
                        cur.next = temp
                        temp.next = item
                        flag = True
                        break
                    cur = cur.next
                if not flag:
                    cur.next = temp
        return ret


def init_tree(l):
    head = ListNode(l[0])
    cur = head
    for i in l[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def print_tree(head):
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret

if __name__ == '__main__':
    l = [-1, 5, 3, 4, 0]
    head = init_tree(l)

    s = Solution()
    head = s.insertionSortList(head)
    ret = print_tree(head)
    print(ret)
    # s = Solution()
