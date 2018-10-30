# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        fib0, fib1 = 0, 1
        if n < 2:
            return n
        for i in range(2, n+1):
            fibi = fib0 + fib1
            fib0 = fib1
            fib1 = fibi
        return fibi
