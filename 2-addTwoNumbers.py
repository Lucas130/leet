"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = l1
        l1.val += l2.val
        l1.val, carry = l1.val % 10, l1.val // 10
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            l1.val += l2.val + carry
            carry = 0
            if l1.val > 9:
                l1.val -= 10
                carry = 1
        if not l1.next and not l2.next:
            if carry:
                l1.next = ListNode(carry)
        else:
            if not l1.next and l2.next:
                l1.next = l2.next
                l1.next.val += carry
            if not l2.next and l1.next:
                l1.next.val += carry
            l1 = l1.next
            while l1.val > 9:
                l1.val -= 10
                if not l1.next:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1
                    l1 = l1.next
        return new_node


