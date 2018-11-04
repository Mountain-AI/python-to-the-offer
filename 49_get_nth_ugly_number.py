# -*- coding=utf-8 -*-
import numbers


class Solution:
    def GetUglyNumber_Solution(self, index):
        assert isinstance(index, numbers.Integral)
        if index < 1:
            return None

        ugly = [1]
        while len(ugly) <= index:
            for item in ugly:
                if item * 2 > ugly[-1]:
                    break
            p1 = item * 2
            for item in ugly:
                if item * 3 > ugly[-1]:
                    break
            p2 = item * 3
            for item in ugly:
                if item * 5 > ugly[-1]:
                    break
            p3 = item * 5
            ugly.append(min(p1, p2, p3))

        return ugly[-1]


if __name__ == "__main__":
    n = [2, 3, 4, 5, 6, 7]
    ex = Solution()
    for item in n:
        print(ex.GetUglyNumber_Solution(item))
