# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size==0:
            return ""
        l=[]
        for i in range(len(num)-size+1):
            tt=max(num[i:i+size])
            l.append(tt)
        return l