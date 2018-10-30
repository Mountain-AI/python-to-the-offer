# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray1(self, array):
        """将数组调节为奇数在前偶数在后

        Args:
            array (list): 待调整数组
        """

        if array is None or len(array) < 2:
            return array

        p1 = 0
        p2 = len(array) - 1
        while p1 < p2:
            if self.is_even(array[p1]) and not self.is_even(array[p2]):
                self.swap(array, p1, p2)

            while not self.is_even(array[p1]):
                p1 += 1
            while self.is_even(array[p2]):
                p2 -= 1

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def is_even(self, item):
        return item & 1 == 0

    def reOrderArray(self, array):
        if array is None or len(array) < 2:
            return array

        assi_array = []

        for item in array:
            if not self.is_even(item):
                assi_array.append(item)
        for item in array:
            if self.is_even(item):
                assi_array.append(item)

        return assi_array


if __name__ == "__main__":
    nums = [[1, 2, 3, 4, 5],
            [2, 4, 7, 9, 110],
            [1, 2, 3, 4, 5, 6, 7]]
    ex = Solution()
    for array in nums:
        ex.reOrderArray(array)
        print(array)
