# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """找到旋转数组中的最小数字

        Args:
            rotateArray (list): 数组

        Returns:
            int: 最小数字
        """

        if rotateArray is None or len(rotateArray) <= 0:
            return 0
        low = mid = 0
        high = len(rotateArray) - 1
        while rotateArray[low] >= rotateArray[high]:
            mid = (low + high) // 2
            if rotateArray[low] == rotateArray[high] and rotateArray[low] == rotateArray[mid]:
                return self.sequential_compare(rotateArray, low, high)
            if rotateArray[mid] >= rotateArray[low]:
                low = mid
            if rotateArray[mid] <= rotateArray[high]:
                high = mid
            if high - low == 1:
                return rotateArray[high]
        return rotateArray[mid]

    def sequential_compare(self, rotateArray, low, high):
        if low == high:
            return rotateArray[low]
        for i in range(low, high+1):
            if rotateArray[i] < rotateArray[low]:
                return rotateArray[i]
        return rotateArray[low]
