# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        '''
        #简单版解法
        tempS=s[n:]
        tempS+=s[:n]
        return tempS
    '''
        #第二种，三次翻转
        if len(s)==0:
            return ''
        length=len(s)
        #n%=length
        s=list(s)
        s[:n]=self.Swap(s[0:n])
        s[n:]=self.Swap(s[n:])
        s=self.Swap(s)
        return ''.join(str(i) for i in s)
    def Swap(self,arr):
        length=len(arr)
        for i in range(length/2):
            temp=arr[i]
            arr[i]=arr[length-1-i]
            arr[length-i-1]=temp
        return arr