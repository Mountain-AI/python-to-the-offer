# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return
        stack = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            if temp.left is not None or temp.right is not None:
                temp.left, temp.right = temp.right, temp.left
            if temp.left is not None:
                stack.append(temp.left)
            if temp.right is not None:
                stack.append(temp.right)

    def Mirror_recur(self, root):
        """递归版"""
        if root is None:
            return
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        self.Mirror_recur(root.left)
        self.Mirror_recur(root.right)

    def mirror(self, root1, root2):
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
        return self.mirror(root1.left, root2.right) and self.mirror(root1.right, root2.left)


def main():
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)

    # 镜像树
    root1 = TreeNode(8)
    root1.left = TreeNode(6)
    root1.right = TreeNode(10)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(7)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(11)

    ex = Solution()
    ex.Mirror(root)
    print(ex.mirror(root1, root))


if __name__ == '__main__':
    main()
