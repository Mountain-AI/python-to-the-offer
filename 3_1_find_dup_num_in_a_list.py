# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """借助辅助数据结构，时间复杂度O(n)，空间复杂度O(n)

        Arguments:
            numbers {list} -- 给定数组
            duplication {list} -- 结果数据（牛客系统为了便于检测结果强制要求的，其实没有必要）

        Returns:
            bool -- 存在返回True 否则返回False
        """

        if numbers is None or len(numbers) < 2:
            return False

        temp_set = set()
        for item in numbers:
            if item in temp_set:
                duplication[0] = item
                return True
            temp_set.add(item)

        return False

    def duplicate_2(self, numbers, duplication):
        """不使用辅助数据结构，根据数组本身特点求解 时间复杂度O(n)，空间复杂度O(1)
        """

        if numbers is None or len(numbers) < 2:
            return False

        length = len(numbers)
        for i in range(length):
            try:
                while numbers[i] != i:
                    if numbers[numbers[i]] == numbers[i]:
                        duplication[0] = numbers[i]
                        return True
                    else:
                        self.swap(numbers, i, numbers[i])
            # 顺便检测一下数组中元素是不是只含有0~n的
            except IndexError:
                print("BAD INPUT")
                return False

        return False

    def swap(self, numbers, index1, index2):
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]


if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    res = [0]
    ex = Solution()
    print(ex.duplicate(nums, res))
    print(res)
