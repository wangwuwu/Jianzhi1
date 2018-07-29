# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        '''
        这里使用pop函数，返回指定元素并从原列表中删除，
        '''
        res = []
        while matrix:
            res+=matrix.pop(0)
            if matrix and matrix[0]:
                res+=[x.pop() for x in matrix]
            if matrix:
                res+=matrix.pop()[::-1]
            if matrix and matrix[0]:
                res+=[x.pop(0) for x in matrix][::-1]
        return res