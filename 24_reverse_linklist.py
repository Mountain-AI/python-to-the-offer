# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        """反转链表，返回反转后的头

        Args:
            pHead (ListNode): 链表头

        Returns:
            ListNode: 反转之后链表头
        """

        if pHead is None or pHead.next is None:
            return pHead
        new_head = self.ReverseList(pHead.next)

        pHead.next.next = pHead
        pHead.next = None

        return new_head
