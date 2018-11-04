# -*- coding:utf-8 -*-
import heapq


class Solution:
    """得到一个输入流的中位数，利用一个最大堆一个最小堆实现
    """

    def __init__(self):
        self.min_heap = list([])
        self.max_heap = list([])

    def Insert(self, num):
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, num)
            return
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            self.balance()

    def balance(self):
        pop_heap, push_heap = (self.min_heap, self.max_heap) if len(
            self.min_heap) > len(self.max_heap) else (self.max_heap, self.min_heap)

        while len(pop_heap) - len(push_heap) > 1:
            heapq.heappush(push_heap, -heapq.heappop(pop_heap))

    def GetMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]


if __name__ == "__main__":
    nums = [[3, 4, 5],
            [5, 2, 3, 4, 1, 6, 7, 0, 8],
            [3, 4, 5, 6, 7, 8, 9],
            ]
    ex = Solution()
    for num in nums[1]:
        ex.Insert(num)
        print(ex.GetMedian(), end=' ')
