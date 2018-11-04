# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if numbers is None or len(numbers) != 5:
            return []

        numbers.sort()
        length = len(numbers)

        times = numbers.count(0)
        for i in range(length-1):
            if numbers[i] == 0:
                continue
            delta = numbers[i+1] - numbers[i]
            if delta == 0:
                return False
            elif delta - 1 <= times:
                times -= delta - 1
            else:
                return False

        return True


if __name__ == "__main__":
    nums = [1, 3, 2, 6, 4]
    ex = Solution()
    print(ex.IsContinuous(nums))
