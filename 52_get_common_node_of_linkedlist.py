# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return None

        loop1 = self.check_loop(pHead1)
        loop2 = self.check_loop(pHead2)
        # 都有环
        if loop1 and loop2:
            p = loop1
            while p.next != loop1:
                if p == loop2:
                    return loop1
                p = p.next
            return None
        # 都无环
        elif (not loop1) and (not loop2):
            p1, p2 = pHead1, pHead2
            while p1 != p2:
                p1 = pHead1 if p1 is None else p1.next
                p2 = pHead2 if p2 is None else p2.next
            return p1
        else:
            return None

    @staticmethod
    def check_loop(pHead):
        if pHead.next is None:
            return False

        buf_dict = {}
        p = pHead
        while p is not None:
            if p in buf_dict:
                return p
            buf_dict[pHead] = 0
            p = p.next
        return False
