# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        """返回克隆的复杂链表的头结点

        Args:
            pHead (RandomListNode): 复杂链表头部

        Returns:
            RanddomListNode: 复制链表头部
        """

        if pHead is None:
            return None

        buf_dict = {}
        copy_head = RandomListNode(pHead.label)
        p, copy_p = pHead, copy_head
        while p.next is not None:
            copy_p.next = RandomListNode(p.next.label)
            p = p.next
            copy_p = copy_p.next
            buf_dict[p] = copy_p

        p, copy_p = pHead, copy_head
        while p is not None:
            if p.random is not None:
                copy_p.random = buf_dict[p.random]
            p = p.next
            copy_p = copy_p.next
        return copy_head
