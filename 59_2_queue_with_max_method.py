# -*- coding=utf-8 -*-
from collections import deque


class WithMaxQueue():
    """能O(1)时间复杂度返回队列最大值的队列实现：
    实现了pop_front以及push_back方法
    """

    def __init__(self):
        """初始化，self.__l, self.__r两个参数很重要
        params:
        self.__queue:  存储数据的队列
        self.__shadow: 存储数据队列中最大值的队列
        self.__l:      等价于滑动窗口左边界，表示当前队列头部是第几个添加进来的元素
        self.__r:      等价于滑动窗口右边界，表示当前队列尾部是第几个添加进来的元素
        """

        self.__queue = deque()
        self.__shadow = deque()
        self.__l, self.__r = 0, 0

    def push_back(self, item):
        self.__queue.append(item)
        self.expand(item)
        self.__r += 1

    def pop_front(self):
        if self.__queue:
            self.__queue.popleft()
            self.__l += 1
            self.shrink()
        else:
            raise IndexError("pop from emtpy queue")

    def expand(self, item):
        """滑动窗口的扩大过程：即当有新元素时，对最大值队列的调整
        """

        if not self.__shadow:
            self.__shadow.append((self.__r, item))
        else:
            if item < self.__shadow[-1][-1]:
                self.__shadow.append((self.__r, item))
            else:
                while self.__shadow and item >= self.__shadow[-1][-1]:
                    self.__shadow.pop()
                self.__shadow.append((self.__r, item))

    def shrink(self):
        """滑动窗口的缩小过程（窗口左边界右移）即：当弹出元素时，对最大值队列的调整
        """

        while self.__shadow and self.__l > self.__shadow[0][0]:
            self.__shadow.popleft()

    def get_max(self):
        return self.__shadow[0][-1]


if __name__ == "__main__":
    ex = WithMaxQueue()
    num = [2, 3, 4, 2, 6, 2, 5, 1]
    # The anster is 4, 4, 6, 6, 6, 5
    for i in range(3):
        ex.push_back(num[i])
    print(ex.get_max())
    for i in range(3, len(num)):
        ex.push_back(num[i])
        ex.pop_front()
        print(ex.get_max())
