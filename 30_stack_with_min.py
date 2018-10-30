# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack_min = []
        self.min_value = None

    def push(self, node):
        if not self.stack:
            self.min_value = node
        else:
            self.min_value = min(self.min_value, node)
            
        self.stack.append(node)
        self.stack_min.append(self.min_value)

    def pop(self):
        self.stack_min.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.stack_min[-1]
