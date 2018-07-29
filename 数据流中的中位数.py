# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l=[]
    def Insert(self, num):
        # write code here
        self.l.append(num)
        self.l.sort()
    def GetMedian(self,k):
        # write code here
        lenght=len(self.l)
        if lenght%2==1:
            return self.l[lenght//2]
        return (self.l[lenght//2]+self.l[lenght//2-1])/2.0
'''
class Solution:
    def __init__(self):
        self.arr=[]
    def Insert(self, num):
        self.arr.append(num)
        self.arr.sort()
    def GetMedian(self,fuck):
        length=len(self.arr)
        if length%2==1:
            return self.arr[length//2]
        return(self.arr[length//2]+self.arr[length//2-1])/2.0
    '''