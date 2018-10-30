# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        """青蛙跳台阶，一次可以跳一阶或者两节

        Args:
            number (int): 最后目的阶数

        Returns:
            int: 所有可以跳到目的台阶的方式
        """

        fib1 = 1
        fib2 = 2
        if number == 1:
            return fib1
        if number == 2:
            return fib2
        for i in range(3, number+1):
            fibi = fib1 + fib2
            fib1 = fib2
            fib2 = fibi
        return fibi
