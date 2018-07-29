# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        '''
        ���õݹ���ʽ�Ļ��ݷ���
        1����matrix�е�Ԫ�غ�path���ַ���ͬʱ����ʼ����
        2��ÿ�ΰ����ң����²��ң����ҵ���path�����һ���ַ�˵��ȫ���ҵ�������1
        ��ÿ�εݹ飬��Ԫ�غ�path��Ӧλ�ò�һ���������Ѿ����ʹ��ģ����߳�����Χ�����־λ��Ϊ0������0���л���
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
        