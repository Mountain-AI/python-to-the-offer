# -*- coding=utf-8 -*-


class Solution():
    def InversePairs_recur(self, data):
        """递归归并排序求逆序对

        Args:
            data (list): 列表

        Returns:
            int: 逆序对数目
        """

        if data is None or len(data) < 2:
            return 0

        return self.merge(data, 0, len(data)-1)

    def merge(self, data, left, right):
        if left == right:
            return 0

        middle = left + ((right - left) >> 1)
        left_pairs = self.merge(data, left, middle)
        right_pairs = self.merge(data, middle+1, right)
        merge_pairs = self.process(data, left, right, middle)

        return left_pairs + right_pairs + merge_pairs

    def process(self, data, left, right, middle):
        """归并过程

        Args:
            data (list): 列表
            left (int): 归并左边界
            right (int): 归并右边界
            middle (int): 归并区间分割点
        """

        l, r = left, middle+1
        pairs = 0
        cur = left
        temp_arr = [0 for i in range(len(data))]
        while l <= middle and r <= right:
            # 如果左边数组元素l大于右边数组元素r，则有逆序对middle - l + 1
            if data[l] > data[r]:
                temp_arr[cur] = data[r]
                r += 1
                cur += 1
                pairs += middle - l + 1
            else:
                temp_arr[cur] = data[l]
                l += 1
                cur += 1
        while l <= middle:
            temp_arr[cur] = data[l]
            cur += 1
            l += 1
        while r <= right:
            temp_arr[cur] = data[r]
            r += 1
            cur += 1
        for i in range(left, right+1):
            data[i] = temp_arr[i]

        return pairs

    def InversePairs(self, data):
        """非递归版归并求逆序对

        Args:
            data (list): 列表

        Returns:
            int: 逆序对个数
        """

        if data is None or len(data) < 2:
            return 0

        period = 1
        length = len(data)
        pairs = 0
        while period <= (length//2):
            for i in range(0, length, 2*period):
                left = i
                right = i + 2 * period - 1
                if right > length - 1:
                    right = length - 1
                middle = left + period - 1
                if left <= middle < right:
                    pairs += self.process(data, left, right, middle)
            period *= 2
        pairs += self.process(data, 0, length-1, period-1)
        return pairs


if __name__ == "__main__":
    data_long = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407,
                 416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360, 965,
                 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233,
                 144, 174, 557, 67, 746, 550, 474, 162, 268, 142, 463, 221,
                 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82,
                 935, 983, 583, 523, 697, 478, 147, 795, 380, 973, 958, 115,
                 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630,
                 425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38,
                 811, 267, 575]
    ex = Solution()
    print(ex.InversePairs(list(data_long)))
    print(ex.InversePairs_recur(list(data_long)))
