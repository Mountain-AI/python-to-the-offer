# -*- coding=utf-8 -*-
import numbers
import time


class Solution():
    """求n个骰子扔在地上，所有骰子正面向上点数和s的各种情况及其出现概率
    """

    def __init__(self, dice=6):
        self.dice_numbers = dice

    def get_sum_recur(self, n):
        """递归求解版本

        Arguments:
            n {int} -- 骰子个数

        Returns:
            list -- 包含元素为（s, probability）, s为和，probability为s出现概率。
        """

        assert isinstance(n, numbers.Integral)
        if n < 1:
            return [(0, 1)]

        res_arr = [0 for i in range((self.dice_numbers - 1) * n + 1)]
        self.recur_process(n, res_arr)

        total = self.dice_numbers ** n
        res_arr = [(i + n, res_arr[i] / total) for i in range(len(res_arr))]

        return res_arr

    def recur_process(self, n, res_arr):
        for i in range(1, self.dice_numbers + 1):
            self.process(n, n, i, res_arr)

    def process(self, n, remain, cur_sum, res_arr):
        if remain == 1:
            res_arr[cur_sum - n] += 1
        else:
            for i in range(1, self.dice_numbers+1):
                self.process(n, remain-1, cur_sum+i, res_arr)

    def get_sum(self, n):
        """非递归求解版本
        """

        assert isinstance(n, numbers.Integral)
        if n < 1:
            return [(0, 1)]

        p1 = [0] * 2
        p1[0] = [0 for i in range(self.dice_numbers*n+2)]
        p1[1] = [0 for i in range(self.dice_numbers*n+2)]
        # flag用来每次循环时，复用上轮循环的结果
        flag = 0
        for i in range(1, self.dice_numbers+1):
            p1[flag][i] = 1

        for i in range(2, n+1):
            for j in range(i):
                # 和不可能小于i
                p1[1-flag][j] = 0
            for j in range(i, self.dice_numbers*i+1):
                p1[1-flag][j] = 0
                k = 1
                while k <= self.dice_numbers and k < j:
                    p1[1-flag][j] += p1[flag][j-k]
                    k += 1
            flag = 1 - flag

        total = self.dice_numbers ** n

        res = []
        for i in range(n, self.dice_numbers*n+1):
            res.append((i, p1[flag][i]/total))

        return res


if __name__ == "__main__":
    n = 10
    print('{}个骰子的情况下：'.format(n))
    ex = Solution()
    start = time.time()
    print("递归求解结果：\n{}".format(ex.get_sum_recur(n)))
    first_period = time.time() - start

    print("非递归求解结果：\n{}".format(ex.get_sum(n)))
    second_period = time.time() - start - first_period

    print("递归用时：{}, 非递归用时：{} \n递归用时是非递归用时的 {} 倍。".format(
        first_period, second_period, first_period/second_period))
