class Solution:
    def movingCount(self, threshold, rows, cols):
        """主函数

        Arguments:
            threshold {int} -- 阈值，当前访问的格子横纵坐标坐标各位数字加起来不应超过threshold
            rows {int} -- 矩阵总行数
            cols {int} -- 矩阵总列数

        Returns:
            int -- 可以访问的坐标数
        """

        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0

        visited = [False for i in range(rows * cols)]

        count = self.moving_count(threshold, rows, cols, 0, 0, visited)

        return count

    def moving_count(self, threshold, rows, cols, row, col, visited):
        """递归计算可去做标数

        Arguments:
            row {int} -- 当前横坐标
            col {int} -- 当前纵坐标
            visited {list} -- 记录当前坐标是否已经被计算过
        """

        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True
            count = 1 + self.moving_count(threshold, rows, cols, row, col-1, visited) \
                      + self.moving_count(threshold, rows, cols, row-1, col, visited) \
                      + self.moving_count(threshold, rows, cols, row, col+1, visited) \
                      + self.moving_count(threshold, rows, cols, row+1, col, visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        """判断该坐标是否可以访问

        Returns:
            bool
        """

        if row >= 0 and row < rows and col >= 0 and col < cols and \
                self.get_sum(row) + self.get_sum(col) <= threshold and \
                not visited[row * cols + col]:
            return True
        return False

    def get_sum(self, num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total


if __name__ == "__main__":
    th = 3
    rows = cols = 3
    ex = Solution()
    print(ex.movingCount(th, rows, cols))
