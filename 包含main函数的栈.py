# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr=[]
    def push(self, node):
        self.arr.append(node)
        # write code here
    def pop(self):
        return self.arr.pop()
        # write code here
    def top(self):
        return self.arr[-1]
        # write code here
    def min(self):
        return min(self.arr)
        # write code here