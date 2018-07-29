'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        one=1
        two=1
        three=0
        if number==0|number==1:
            return 1
        for i in range(2,number+1):
            three=one+two
            one=two
            two=three
        return three