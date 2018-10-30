# -*- coding=utf-8 -*-
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():
    """分层之字形打印二叉树
    """

    def Print(self, pRoot):
        if pRoot is None:
            return []

        s1, s2, res = [], [], []
        s1.append(pRoot)
        while s1 or s2:
            if s1:
                cur_level_res = []
                while s1:
                    item = s1.pop()
                    cur_level_res.append(item.val)
                    if item.left:
                        s2.append(item.left)
                    if item.right:
                        s2.append(item.right)
                res.append(cur_level_res)

            if s2:
                cur_level_res = []
                while s2:
                    item = s2.pop()
                    cur_level_res.append(item.val)
                    if item.right:
                        s1.append(item.right)
                    if item.left:
                        s1.append(item.left)
                res.append(cur_level_res)
        
        return res

        
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    ex = Solution()
    print(ex.Print(root))


if __name__ == "__main__":
    main()