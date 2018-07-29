# -*- coding:utf-8 -*-
'''
一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag=0
        m=len(array)
        n=len(array[0])
        i=m-1
        j=0
        if  len(array[0])==0 or array[0][0]>target or array[m-1][n-1]<target :
            return 0
        while j<=n-1 and i>=0:
            if array[i][j]==target:
                return 1
            if array[i][j]>target:
                i-=1
            if array[i][j]<target:
                j+=1
        return 0
