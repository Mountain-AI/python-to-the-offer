# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        """打印链表倒数第k个节点

        Args:
            head (ListNode): 链表头结点
            k (int): 指定数字

        Returns:
            ListNode: 倒数第k个节点
        """

        p_ahead = head
        p_behind = head
        while k > 0:
            if p_ahead is None:
                return None
            p_ahead = p_ahead.next

            k -= 1
        while p_ahead is not None:
            p_ahead = p_ahead.next
            p_behind = p_behind.next
        return p_behind
