# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.res = []

    def printListFromTailToHead(self, listNode):
        """从尾到头打印链表，将打印结果存入数组

        Args:
            listNode (ListNode): 链表头

        Returns:
            list: 数组结果
        """

        if listNode is not None:
            self.printListFromTailToHead(listNode.next)
            self.res.append(listNode.val)
        return self.res
