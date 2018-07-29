# -*- coding:utf-8 -*-
'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
import random
class Solution:
    def Sum_Solution(self, n):
        # write code here
        '''方法一直接调用库函数
        l=list(range(1,n+1))
        return sum(l)
        '''
        #方法二：使用递归
        #0和任何数and都为0，任何数和1and都为自己
        return  (n>0) and (n+self.Sum_Solution(n-1))