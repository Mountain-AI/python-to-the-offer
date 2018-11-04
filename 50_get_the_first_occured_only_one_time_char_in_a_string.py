# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s is None:
            return -1
        if len(s) == 0:
            return -1

        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    string = 'abaccdeff'
    ex = Solution()
    print(ex.FirstNotRepeatingChar(string))