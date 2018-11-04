# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def maxInWindows(self, num, size):
        if num is None or size is None:
            return []
        if size < 1 or size > len(num):
            return []

        res = []
        helper = deque()
        for i in range(size):
            self.expand(num, i, helper)
        res.append(num[helper[0]])

        l = 0
        for i in range(size, len(num)):
            self.expand(num, i, helper)
            l += 1
            self.shrink(num, l, helper)
            res.append(num[helper[0]])

        return res

    def expand(self, num, index, helper):
        if not helper:
            helper.append(index)
        elif num[index] < helper[-1]:
            helper.append(index)
        else:
            while helper and num[index] >= num[helper[-1]]:
                helper.pop()
            helper.append(index)

    def shrink(self, num, l, helper):
        while helper and helper[0] < l:
            helper.popleft()


if __name__ == "__main__":
    ex = Solution()
    num = [2, 3, 4, 2, 6, 2, 5, 1]
    print(ex.maxInWindows(num, 3))
