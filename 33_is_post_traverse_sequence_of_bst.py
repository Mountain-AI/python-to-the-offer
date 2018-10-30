# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        length = len(sequence)
        if length <= 0:
            return False

        root = sequence[-1]
        for i in range(length):
            if sequence[i] > root:
                break
        j = i
        for j in range(i, length-1):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right
