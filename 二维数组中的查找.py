# -*- coding:utf-8 -*-
'''
һ����ά�����У�ÿ��һά����ĳ�����ͬ����ÿһ�ж����մ����ҵ�����˳������ÿһ�ж����մ��ϵ��µ�����˳�����������һ������������������һ����ά�����һ���������ж��������Ƿ��и�������
'''
class Solution:
    # array ��ά�б�
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
