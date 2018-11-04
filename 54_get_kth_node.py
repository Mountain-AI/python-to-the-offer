# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None or k < 1:
            return None

        cur = pRoot
        res = -1
        while cur:
            most_right = cur.left
            if most_right:
                while most_right.right and most_right.right != cur:
                    most_right = most_right.right

                # 第一次遍历到cur节点
                if most_right.right is None:
                    most_right.right = cur
                    cur = cur.left
                    continue
                # 第二次遍历到cur节点
                if most_right.right == cur:
                    most_right.right = None

            k -= 1
            if k == 0:
                # 为了不破坏原二叉树结构，没有直接返回cur节点
                res = cur
            cur = cur.right
        return None if res == -1 else res


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    ex = Solution()
    print(ex.KthNode(root, 4))  # The answer is TreeNode(5)
