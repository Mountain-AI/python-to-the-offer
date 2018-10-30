# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, s):
        """将s中的空格替换成%20

        Args:
            s (str): 给定字符串

        Returns:
            str: 替换后字符串
        """

        blank_nums = s.count(' ')
        original_length = len(s)
        s = list(s)
        s.extend(['0' for i in range(2*blank_nums)])
        i = original_length - 1
        j = original_length + 2 * blank_nums - 1
        while i >= 0 and i <= j:
            if s[i] == ' ':
                s[j-2:j+1] = '%20'
                j -= 3
                i -= 1
            else:
                s[j] = s[i]
                j -= 1
                i -= 1
        s = ''.join(s)
        
        return s
