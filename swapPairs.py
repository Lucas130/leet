"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            temp = head.next
        pre = ListNode(-1)
        pre.next = head
        while True:
            head, net = head, head.next
            head.next = net.next
            net.next = head
            pre.next = net
            pre = head
            head = head.next
            if not head or not head.next:
                break
        return temp