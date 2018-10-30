# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        """前序序列化二叉树

        Args:
            root (TreeNo): 二叉树根节点

        Returns:
            str: 序列化字符串
        """

        if root is None:
            return '#_'
        res = '%d_' % root.val
        res += self.Serialize(root.left)
        res += self.Serialize(root.right)
        return res

    def Deserialize(self, s):
        """根据字符串反序列化由Serialize函数序列化的二叉树

        Args:
            s (str): 序列化的字符串

        Returns:
            TreeNode: 反序列化之后二叉树头结点
        """

        s = s.split('_')[:-1]

        def inside(s):
            head = s.pop(0)
            print(head)
            if head == '#':
                return None
            head = TreeNode(int(head))
            head.left = inside(s)
            head.right = inside(s)

            return head

        return inside(s)
