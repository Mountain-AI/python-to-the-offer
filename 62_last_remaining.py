# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution_1(self, n, m):
        """利用辅助数组解法

        Arguments:
            n {int} -- 人数
            m {int} -- 删除第m个元素

        Returns:
            int -- 最后剩余人代号
        """

        if n < 1 or m < 0:
            return -1

        arr = [i for i in range(n)]
        cur = 0
        while len(arr) != 1:
            period = m - 1
            while period:
                cur = self.next_index(arr, cur)
                period -= 1
            arr.pop(cur)
            if cur >= len(arr):
                cur = 0

        return arr[-1]

    def next_index(self, arr, cur):
        return 0 if cur >= len(arr) - 1 else cur + 1

    def LastRemaining_Solution_2(self, n, m):
        """f(n, m) = (f(n - 1, m) + m) % n
        如果不做映射，f(n-1, m)结果相当于f(n, m)淘汰第一个人之后的下一步，但调整了剩余的n-1
        人的代号之后，我们需要确定的映射关系，能把调整之后的代号转换到初始包含n个人的情况下的代号
        这样返回的结果也是和最初数据对应的。
        """

        if n < 1 or m < 1:
            return -1

        last = 0
        for i in range(2, n+1):
            last = (last + m) % i

        return last


if __name__ == "__main__":
    ex = Solution()
    n, m = 5, 3
    print(ex.LastRemaining_Solution_2(n, m))
