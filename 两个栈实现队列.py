# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
 
    def push(self, node):
        # write code here
        self.stack1.append(node)
 
    def pop(self):
        if not self.stack2:#���Ϊ����stack1�е����ݵ������stack2�У�����ֱ��pop
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()#ע��pop�����һ������appendλ��һ���� ��pop(0)����һ�����Ĳ�ͬ