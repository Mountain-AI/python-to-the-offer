# -*- coding=utf-8 -*-
class Solution():
    def max_value_of_presents_recur(self, arr):
        if arr is None:
            return None
        if len(arr) == 0 or len(arr[0]) == 0:
            return 0

        row_l = len(arr)
        col_l = len(arr[0])
        return self.process(arr, 0, 0, row_l-1, col_l-1)

    def process(self, arr, i, j, row_l, col_l):
        if i == row_l and j == col_l:
            return arr[i][j]

        if i == row_l:
            res = arr[i][j] + self.process(arr, i, j+1, row_l, col_l)
        elif j == col_l:
            res = arr[i][j] + self.process(arr, i+1, j, row_l, col_l)
        else:
            res = arr[i][j] + max(self.process(arr, i, j+1, row_l, col_l),
                                  self.process(arr, i+1, j, row_l, col_l))
        return res

    # 动态规划版本
    def max_value_of_presents(self, arr):
        if arr is None:
            return None
        if len(arr) == 0 or len(arr[0]) == 0:
            return 0

        row_l = len(arr)
        col_l = len(arr[0])
        res = [[0 for i in range(len(arr[0]))] for i in range(len(arr))]
        res[row_l-1][col_l-1] = arr[row_l-1][col_l-1]

        i = row_l - 1
        for j in range(col_l-2, -1, -1):
            res[i][j] = arr[i][j] + res[i][j+1]

        j = col_l - 1
        for i in range(row_l-2, -1, -1):
            res[i][j] = arr[i][j] + res[i+1][j]

        for i in range(row_l-2, -1, -1):
            for j in range(col_l-2, -1, -1):
                res[i][j] = arr[i][j] + max(res[i+1][j], res[i][j+1])

        return res[0][0]


if __name__ == "__main__":
    arr = [[1, 10, 3, 8],
           [12, 2, 9, 6],
           [5, 7, 4, 11],
           [3, 7, 16, 5],
           ]
    ex = Solution()
    print(ex.max_value_of_presents(arr))
