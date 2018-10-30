# -*- coding:utf-8 -*-
import random


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) <= 0:
            return None

        length = len(numbers)
        l, r = 0, length - 1
        middle = length >> 1
        m_left, m_right = self.partition(numbers, l, r)
        while middle not in range(m_left, m_right+1):
            if middle < m_left:
                r = m_left - 1
                m_left, m_right = self.partition(numbers, l, r)
            else:
                l = m_right + 1
                m_left, m_right = self.partition(numbers, l, r)

        return numbers[middle] if numbers.count(numbers[middle]) > length // 2 else 0

    def partition(self, numbers, l, r):
        """快排partition过程

        Arguments:
            numbers {list} -- 数组
            l {int} -- 左边界
            r {int} -- 右边界

        Returns:
            tuple -- 第一个元素为本轮选中元素占据的最左索引，第二个元素为本轮选中元素占据的最右索引
                     如果本轮选中元素在数组中只有一个，那么tuple中两个元素就是相等的。
        """

        self.swap(numbers, random.randint(l, r), r)
        start = l - 1
        end = r
        while l < end:
            if numbers[l] < numbers[r]:
                start += 1
                if start != l:
                    self.swap(numbers, start, l)
                l += 1
            elif numbers[l] == numbers[r]:
                l += 1
            else:
                end -= 1
                self.swap(numbers, l, end)
        self.swap(numbers, end, r)
        return start + 1, end

    def swap(self, numbers, i, j):
        numbers[i], numbers[j] = numbers[j], numbers[i]


if __name__ == "__main__":
    nums = [3, 45, 6, 7, 6]
    ex = Solution()
    print(ex.MoreThanHalfNum_Solution(nums))
