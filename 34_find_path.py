# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def FindPath(self, root, expectNumber):
        """找到二叉树中和为某个值的路径

        Args:
            root (TreeNode): 二叉树根节点
            expectNumber (int): 目标和

        Returns:
            list: 二维列表，内部每个列表表示找到的路径
        """

        if root is None:
            return []
        res = []

        def find_main(root, path, cur_sum):
            cur_sum += root.val
            path.append(root)

            is_leaf = True if root.left is None and root.right is None else False
            if cur_sum == expectNumber and is_leaf:
                one_path = []
                for item in path:
                    one_path.append(item.val)
                res.append(one_path)

            if cur_sum < expectNumber:
                if root.left is not None:
                    find_main(root.left, path, cur_sum)
                if root.right is not None:
                    find_main(root.right, path, cur_sum)

            path.pop()

        find_main(root, [], 0)
        return res
