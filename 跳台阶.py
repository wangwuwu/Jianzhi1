'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        '''看着递归像不像斐波那契数列
        if number==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        n=self.jumpFloor(number-1)+self.jumpFloor(number-2)
        return n
        '''
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
