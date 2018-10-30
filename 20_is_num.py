# -*- coding:utf-8 -*-
import re


class Solution:
    def isNumeric(self, s):
        """
        判断字符串s是不是一个合法的数字形式

        Args:
            s (str): 字符串

        Returns:
            bool: 是否合法
        """

        return True if re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s) else False
