# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        '''
        采用递归形式的回溯法，
        1、当matrix中的元素和path首字符相同时，则开始查找
        2、每次按左右，上下查找，若找到了path的最后一个字符说明全部找到，返回1
        若每次递归，的元素和path对应位置不一样或者是已经访问过的，或者超出范围，则标志位置为0，返回0进行回溯
        '''
        flag=[0]*(rows*cols)
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j]==path[0] and self.judge(matrix,i,j,rows,cols,flag,path,0):
                    return 1
        return 0
    def judge(self,matrix,i,j,rows,cols,flag,path,k):
        index=i*cols+j
        if i<0 or i>=rows or j<0 or j>=cols or flag[index]==1 or path[k]!=matrix[index]:
            return 0
        if k==len(path)-1:
            return 1
        flag[index]=1
        if (self.judge(matrix,i+1,j,rows,cols,flag,path,k+1) or 
        self.judge(matrix,i-1,j,rows,cols,flag,path,k+1) or 
        self.judge(matrix,i,j+1,rows,cols,flag,path,k+1) or 
        self.judge(matrix,i,j-1,rows,cols,flag,path,k+1)):
            return 1
        flag[index]=0
        return 0
        