# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        """查找给定节点的下一个节点

        Args:
            pNode (TreeLinkNode): 给定二叉树头

        Returns:
            TreeLinkNode: 给定节点的下一个节点，没有则是None
        """

        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        elif pNode.next and pNode.next.left == pNode:
            return pNode.next
        elif pNode.next and pNode.next.right == pNode:
            p = pNode
            while p.next and p.next.next:
                if p.next.next.left == p.next:
                    return p.next.next
                p = p.next
            return None
        else:
            return None
