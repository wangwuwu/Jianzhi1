# -*- coding:utf-8 -*-
import math
'''
������һ��m�к�n�еķ���һ�������˴�����0,0�ĸ��ӿ�ʼ�ƶ���ÿһ��ֻ�������ң��ϣ����ĸ������ƶ�һ�񣬵��ǲ��ܽ�������������������λ֮�ʹ���k�ĸ��ӡ� ���磬��kΪ18ʱ���������ܹ����뷽��35,37������Ϊ3+5+3+7 = 18�����ǣ������ܽ��뷽��35,38������Ϊ3+5+3+8 = 19�����ʸû������ܹ��ﵽ���ٸ����ӣ�
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
    def getSum(self,a):#��ø���λ�ϵ���֮��
        summ=0
        while a:
            summ+=a%10
            a=int(a/10)
        return summ