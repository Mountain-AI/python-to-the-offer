# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def is_symmetry_tree(self, root1, root2):
        """检测两棵二叉树是不是镜像树

        Args:
            root1 (TreeNode): 二叉树头结点
            root2 (TreeNode): 二叉树头结点

        Returns:
            bool: 是否为镜像树
        """

        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False
        return self.is_symmetry_tree(root1.left, root2.right) and \
            self.is_symmetry_tree(root1.right, root2.left)


def main():
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(5)

    ex = Solution()
    print(ex.is_symmetry_tree(root, root))


if __name__ == '__main__':
    main()
