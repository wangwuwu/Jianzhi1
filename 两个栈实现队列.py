# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
 
    def push(self, node):
        # write code here
        self.stack1.append(node)
 
    def pop(self):
        if not self.stack2:#如果为空则将stack1中的数据倒序放入stack2中，否则直接pop
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()#注意pop（最后一个，和append位置一样） 和pop(0)（第一个）的不同