# -*- coding:utf-8 -*-
class Solution:
    def Add(self, a, b):
        # write code here
        '''
        利用二进制求和,两个数异或相当于每一位相加不考虑进位，两个数相与左移一位，得到进位
        '''
        '''
        n1=n2=0
        while num2!=0:
            n1=num1^num2
            n2=(num1 & num2)<<1
            num1=n1
            num2=n2
        return n1
        '''
        while(b): 
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)