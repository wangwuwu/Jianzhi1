# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self,pushV, popV):
    # write code here
        stack = []
        l = len(pushV)
        i = 0
        while i < l :
        #global stack
            if pushV[i] != popV[0]:
                stack.append(pushV[i])
                i += 1
            else:
                popV.pop(0)
                i += 1
        while stack:
            if stack.pop() != popV.pop(0):
                return False
        return True