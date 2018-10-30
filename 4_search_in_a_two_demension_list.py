# -*- coding:utf-8 -*-
class Solution:
    def Find(self, target, array):
        """在一个从左到右递增，从上往下递增的数组中查找元素

        Args:
            target (int): 待查找数字
            array (list): 待查找数组

        Returns:
            bool: 是否找到
        """

        row_length = len(array)
        col_length = len(array[0])
        if row_length == 0 or col_length == 0:
            return False
        i, j = 0, col_length - 1
        while True:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                if i < row_length - 1:
                    i += 1
                else:
                    return False
            else:
                if j > 0:
                    j -= 1
                else:
                    return False
