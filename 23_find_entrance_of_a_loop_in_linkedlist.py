# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        """找到链表中环的入口节点

        Args:
            pHead (ListNode): 链表头结点

        Returns:
            ListNode: 入口节点（如果没有返回None）
        """

        if pHead is None or pHead.next is None:
            return None
        p1 = p2 = pHead
        while p2.next is not None:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                first_met = p1
                count = 1
                while p1.next != first_met:
                    p1 = p1.next
                    count += 1

                p1 = p2 = pHead
                for i in range(count):
                    p1 = p1.next
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
