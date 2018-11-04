# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array is None or len(array) < 2:
            return []

        res = self.get_xor(array)

        flag = self.get_index(res)
        help_arr1, help_arr2 = [], []
        for item in array:
            res = self.get_bit(item, flag)
            if res:
                help_arr1.append(item)
            else:
                help_arr2.append(item)

        return [self.get_xor(help_arr1), self.get_xor(help_arr2)]

    def get_xor(self, arr):
        res = 0
        for item in arr:
            res = res ^ item

        return res

    def get_index(self, res):
        """得到异或结果其中一位为1的位置

        Arguments:
            res {int} -- 原数组异或结果
        """
        period = 0
        while period < 32:
            if res & 1 == 1:
                return period
            res = res >> 1
            period += 1

    def get_bit(self, num, index):
        # 将给定index位置的bit移到最低位
        while index > 0:
            num = num >> 1
            index -= 1

        return num & 1


if __name__ == "__main__":
    ex = Solution()
    nums = [2, 4, 3, 6, 3, 2, 5, 5]
    print(ex.FindNumsAppearOnce(nums))  # The answer is [6, 4].
