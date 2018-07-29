# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        '''递归可以实现，但是时间复杂度太高
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)
        '''
        '''
        使用数组实现，将每一个数存放在一个位置上，每一个值等于前两个值之和，时间复杂度为n,空间复杂度为n
        a=[0]*40
        a[0]=0
        a[1]=1
        if n==0|n==1:
            return n
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]
        '''
        #时间复杂度为n ,空间复杂度为1
        one=0
        two=1
        three=0
        if n==0|n==1:
            return n
        for i in range(2,n+1):
            three=one+two
            one=two
            two=three
        return three