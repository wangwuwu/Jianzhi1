# -*- coding:utf-8 -*-
class Solution:
    # matrix����Ϊ��ά�б���Ҫ�����б�
    def printMatrix(self, matrix):
        # write code here
        '''
        ����ʹ��pop����������ָ��Ԫ�ز���ԭ�б���ɾ����
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