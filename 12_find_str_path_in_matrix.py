# -*- coding=utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """寻找字符矩阵中相邻元素是否可以组成给定的path

        Arguments:
            matrix {list} -- 字符矩阵
            rows {int} -- 矩阵总行数
            cols {int} -- 矩阵总列数
            path {str} -- 给定字符串路径

        Returns:
            bool -- 是否存在路径
        """

        if matrix is None or rows < 1 or cols < 1 or path is None:
            return False
        mem = [[False for i in range(cols)] for j in range(rows)]
        cur_path_length = 0
        for row in range(rows):
            for col in range(cols):
                cur_path_length = 0
                res = self.has_path(matrix, row, col, rows,
                                    cols, cur_path_length, path, mem)
                if res:
                    return True
        return False

    def has_path(self, matrix, row, col, rows, cols, cur_path_length, path, mem):
        """矩阵路径搜索函数

        Arguments:
            matrix {list} -- 字符矩阵
            row {int} -- 当前到达矩阵元素的行
            col {int} -- 当前到达矩阵元素的列
            rows {int} -- 矩阵总行数
            cols {int} -- 矩阵总列数
            cur_path_length {int} -- 当前已经确认存在的路径长度
            path {str} -- 给定字符串路径
            mem {list} -- 记录元素是否已经被访问过的矩阵

        Returns:
            bool -- 返回row，col元素的邻居能不能继续匹配path
        """

        if cur_path_length == len(path):
            return True

        inner_res = False

        if row >= 0 and row < rows and col >= 0 and col < cols and \
                matrix[row][col] == path[cur_path_length] and not mem[row][col]:

            cur_path_length += 1
            mem[row][col] = True
            inner_res = self.has_path(matrix, row, col-1, rows, cols, cur_path_length, path, mem) or \
                        self.has_path(matrix, row-1, col, rows, cols, cur_path_length, path, mem) or \
                        self.has_path(matrix, row, col+1, rows, cols, cur_path_length, path, mem) or \
                        self.has_path(matrix, row+1, col, rows, cols, cur_path_length, path, mem)

            if not inner_res:
                cur_path_length -= 1
                mem[row][col] = False

        return inner_res


if __name__ == "__main__":
    matrix = [['a', 'b', 'c', 'd'],
              ['e', 'f', 'g', 'h'],
              ['i', 'j', 'k', 'l'],
              ['m', 'n', 'o', 'p'],
              ]
    ex = Solution()
    print(ex.hasPath(matrix, len(matrix), len(matrix[0]), 'abcghlpop'))
