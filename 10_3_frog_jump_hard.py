# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        """有时候我们只是缺少一个发现规律的眼睛
        """

        return 2 ** (number - 1)
