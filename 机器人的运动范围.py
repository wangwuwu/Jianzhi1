# -*- coding:utf-8 -*-
import math
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag=[0]*(rows*cols)
        i=j=0
        self.look(threshold,rows,cols,i,j,flag)
        return sum(flag)
    def look(self,threshold,rows,cols,i,j,flag):
        if i<0 or i>=rows or j<0 or j>=cols or (self.getSum(i)+self.getSum(j))>threshold or flag[i*cols+j]:
            return 0
        index=i*cols+j
        flag[index]=1
        if(self.look(threshold,rows,cols,i+1,j,flag) or self.look(threshold,rows,cols,i-1,j,flag) or 
          self.look(threshold,rows,cols,i,j-1,flag) or self.look(threshold,rows,cols,i,j+1,flag)):
            return 1
        return 0
    def getSum(self,a):#获得各个位上的数之和
        summ=0
        while a:
            summ+=a%10
            a=int(a/10)
        return summ