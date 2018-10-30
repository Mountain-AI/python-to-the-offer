# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        """合并两个排序链表
        """

        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1

        p1, p2 = pHead1, pHead2
        merge_head = None
        if p1.val < p2.val:
            merge_head = p1
            merge_head.next = self.Merge(p1.next, p2)
        else:
            merge_head = p2
            merge_head.next = self.Merge(p1, p2.next)

        return merge_head
