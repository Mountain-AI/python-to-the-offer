# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, arr):
        if arr is None:
            return None
        if len(arr) < 2:
            return sum(arr)

        res = [arr[0] for x in range(len(arr))]
        for i in range(1, len(arr)):
            if res[i-1] <= 0:
                res[i] = arr[i]
            else:
                res[i] = res[i-1] + arr[i]

        return max(res)


if __name__ == "__main__":
    nums = [1, -2, 3, 10, -4, 7, 2, -5]
    ex = Solution()
    print(ex.FindGreatestSumOfSubArray(nums))
