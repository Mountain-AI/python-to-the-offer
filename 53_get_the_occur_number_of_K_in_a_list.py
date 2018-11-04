# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        """计算排序数组中数字出现的次数

        Arguments:
            data {list} -- 数组
            k {int} -- 待寻找数字

        Returns:
            int -- 找到返回个数，找不到返回0
        """

        if k is None or len(data) < 1:
            return 0

        if k < data[0] or k > data[-1]:
            return 0

        first = self.get_occur_location(data, k, True)
        last = self.get_occur_location(data, k, False)
        if first == last and first == -1:
            return 0
        else:
            return last - first + 1

    def get_occur_location(self, data, k, first):
        right = len(data) - 1
        left = 0
        while left <= right:
            middle = left + ((right - left) >> 1)
            if data[middle] == k:
                if first:
                    if middle - 1 > -1 and data[middle-1] == k:
                        right = middle - 1
                    else:
                        return middle
                else:
                    if middle + 1 < len(data) and data[middle+1] == k:
                        left = middle + 1
                    else:
                        return middle
            elif data[middle] > k:
                right = middle - 1
            else:
                left = middle + 1
                
        return -1

    def get_missing_number(self, arr):
        """找到长度为n-1的递增排序数组中不在0~n-1范围内的数字

        Arguments:
            arr {list} -- 长度为n-1的递增排序数组
        """
        if arr is None or len(arr) < 1:
            return None

        return self.binary_find_missing_number(arr)

    def binary_find_missing_number(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + ((right - left) >> 1)
            if arr[middle] == middle:
                left = middle + 1
            elif middle == 0 or (middle - 1 >= 0 and arr[middle-1] == middle-1):
                return middle
            else:
                right = middle - 1

        return -1

    def find_index_equls_value_item(self, arr):
        """找到单调递增且不重复数组中数值和下标相等的元素

        Arguments:
            arr {list} -- 数组 

        Returns:
            int -- 找到返回下标，找不到返回1
        """

        if arr is None or len(arr) < 1:
            return None

        return self.binary_find_equls_item(arr)

    def binary_find_equls_item(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + ((right - left) >> 1)
            if arr[middle] == middle:
                return middle
            elif arr[middle] < middle:
                left = middle + 1
            else:
                right = middle - 1

        return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 3, 3, 3]
    nums2 = [0, 1, 2, 3, 5]
    nums3 = [1, 2, 3, 4]
    nums4 = [-3, -1, 1, 3, 5]
    ex = Solution()
    print(ex.GetNumberOfK(nums, 3))
    print(ex.get_missing_number(nums2))
    print(ex.get_missing_number(nums3))
    print(ex.find_index_equls_value_item(nums4))
