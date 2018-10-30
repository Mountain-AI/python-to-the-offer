# -*- coding:utf-8 -*-
import random


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput is None or k is None or k > len(tinput) or k <= 0:
            return []
        if k == len(tinput):
            return tinput

        l, r = 0, len(tinput) - 1
        m_left, m_right = self.partition(tinput, l, r)
        while k not in range(m_left, m_right+1):
            if k < m_left:
                r = m_left - 1
                m_left, m_right = self.partition(tinput, l, r)
            else:
                l = m_right + 1
                m_left, m_right = self.partition(tinput, l, r)

        return tinput[:k]

    def partition(self, arr, l, r):
        self.swap(arr, random.randint(l, r), r)
        start = l - 1
        end = r
        while l < end:
            if arr[l] < arr[r]:
                start += 1
                if l != start:
                    self.swap(arr, l, start)
                l += 1
            elif arr[l] == arr[r]:
                l += 1
            else:
                end -= 1
                self.swap(arr, l, end)
        self.swap(arr, end, r)

        return start+1, end

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    ex = Solution()
    print(ex.GetLeastNumbers_Solution(arr, 10))
