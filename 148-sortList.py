"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast, slow = head, head
        pre = None
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                pre = slow
                slow = slow.next
        if pre:
            pre.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        return self.merge(head1, head2)

    def merge(self, head1, head2):
        pre = temp = ListNode(0)
        while head1 or head2:
            if not head1:
                temp.next = head2
                break
            if not head2:
                temp.next = head1
                break
            if head1.val < head2.val:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
                temp.next = None
            else:
                temp.next = head2
                temp = temp.next
                head2 = head2.next
                temp.next = None
        return pre.next

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
    head = s.sortList(head)
    ret = print_tree(head)
    print(ret)


