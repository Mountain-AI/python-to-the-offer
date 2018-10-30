# -*- coding:utf-8 -*-
class Solution:
    """matrix类型为二维列表，需要返回列表"""

    def printMatrix(self, matrix):
        res = []
        row_length = len(matrix)
        col_length = len(matrix[0])
        if row_length == 0 or col_length == 0:
            return res
        i = j = 0
        m = row_length - 1
        n = col_length - 1
        while i < m and j < n:
            for _ in range(j, n):
                res.append(matrix[i][_])
            for _ in range(i, m):
                res.append(matrix[_][n])
            for _ in range(n, j, -1):
                res.append(matrix[m][_])
            for _ in range(m, i, -1):
                res.append(matrix[_][j])
            i += 1
            j += 1
            m -= 1
            n -= 1
        if i == m == j == n:
            res.append(matrix[i][j])
        elif i == m:
            for _ in range(j, n+1):
                res.append(matrix[i][_])
        elif j == n:
            for _ in range(i, m+1):
                res.append(matrix[_][n])
        return res
