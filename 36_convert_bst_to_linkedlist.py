# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        """将二叉搜索树与双向链表

        Args:
            pRootOfTree (TreeNode): 二叉树根节点

        Returns:
            TreeNode: 双向链表头部
        """

        if pRootOfTree is None:
            return pRootOfTree
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        def mid_order(root, res):
            if root is None:
                return res

            mid_order(root.right, res)
            res.append(root)
            mid_order(root.left, res)

            return res
        pre_res = mid_order(pRootOfTree, [])
        pre_res = pre_res[::-1]
        head = pre_res[0]
        head.left = None
        head.right = pre_res[1]
        if len(pre_res) > 2:
            for i in range(1, len(pre_res)-1):
                temp = pre_res[i]
                temp.left = pre_res[i-1]
                temp.right = pre_res[i+1]

        pre_res[-1].right = None
        pre_res[-1].left = pre_res[-2]
        return head
