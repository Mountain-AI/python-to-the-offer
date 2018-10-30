# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """根据前序序列和中序序列重建二叉树
    """

    def reConstructBinaryTree(self, pre, tin):
        """根据前序序列和中序序列重建二叉树

        Args:
            pre (list): 前序遍历序列
            tin (list): 中序遍历序列

        Returns:
            TreeNode: 重建二叉树头
        """

        if len(pre) != len(tin) or len(pre) == 0 or len(tin) == 0:
            return None
        root = TreeNode(pre[0])
        if pre[0] in tin:
            value = tin.index(pre[0])
        else:
            return None
        left_tin, right_tin = tin[:value], tin[value+1:]
        left_pre, right_pre = pre[1:1+len(left_tin)], pre[1+len(left_tin):]
        root.left = self.reConstructBinaryTree(left_pre, left_tin)
        root.right = self.reConstructBinaryTree(right_pre, right_tin)

        return root


def main():
    pre = [1, 2, 3, 4, 5, 6, 7]
    tin = [3, 2, 4, 1, 6, 5, 7]
    ex = Solution()
    root = ex.reConstructBinaryTree(pre, tin)
    print(root.val, ' ', root.left.val, ' ', root.right.val)


if __name__ == '__main__':
    main()
