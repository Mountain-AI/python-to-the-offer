# -*- coding=utf-8 -*-
class Solution():
    # 暴力递归版本
    def convert_int_to_str_recur(self, num):
        if num < 0:
            return None

        num = str(num)
        return self.process(num, 0)

    def process(self, num, index):
        if index >= len(num) - 1:
            return 1

        p1 = self.process(num, index+1)
        p2 = self.process(num, index+2) if int(num[index:index+2]) <= 25 else 0

        return p1 + p2

    # 动态规划版本
    def convert_int_to_str(self, num):
        if num < 0:
            return None

        num = str(num)
        res = [0 for i in range(len(num))]
        res[-1], res[-2] = 1, 2 if int(num[-2:]) <= 25 else 1
        for i in range(len(num)-3, -1, -1):
            res[i] = res[i+1]
            if int(num[i:i+2]) <= 25:
                res[i] += res[i+2]
        return res[0]


if __name__ == "__main__":
    num = 12226
    ex = Solution()
    print(ex.convert_int_to_str(num))
