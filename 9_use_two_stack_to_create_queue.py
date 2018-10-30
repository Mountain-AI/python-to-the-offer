# -*- coding:utf-8 -*-
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return False if len(self.data) else True


class Solution:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, node):
        self.stack1.push(node)

    def pop(self):
        if self.stack2.is_empty():
            self.dao()
        return self.stack2.pop()

    def dao(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
