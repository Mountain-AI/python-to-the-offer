# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        """计算base的exponent次方
        
        Arguments:
            base {int} -- 整数
            exponent {int} -- 指数，可正可负
        
        Returns:
            int -- 结果
        """

        if base == 0:
            return 0
        if base == 1:
            return 1

        abs_exponent = self.abs_exp(base, abs(exponent))
        if exponent > 0:
            return abs_exponent
        else:
            return 1 / abs_exponent

    def abs_exp(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        res = self.abs_exp(base, exponent >> 1)
        res *= res
        if exponent & 1 == 1:
            res *= base
        return res


if __name__ == "__main__":
    base = [2, 3, 0, -2, -3]
    exp = [-2, -3, 0, 2, 3]
    ex = Solution()
    for i in base:
        for j in exp:
            print(ex.Power(i, j))
