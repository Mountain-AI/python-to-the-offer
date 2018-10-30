class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():
    def print_tree_with_level(self, root):
        if root is None:
            return None
        qu = []
        qu.append(root)
        count = 0
        while qu:
            to_be_print = len(qu)
            while to_be_print > 0:
                temp = qu.pop(0)
                print(temp.val, end=' ')
                if temp.left:
                    qu.append(temp.left)
                if temp.right:
                    qu.append(temp.right)
                to_be_print -= 1
            count += 1
            print('第%d层\n' % count)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    ex = Solution()
    ex.print_tree_with_level(root)


if __name__ == '__main__':
    main()
