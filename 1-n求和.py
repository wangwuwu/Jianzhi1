# -*- coding:utf-8 -*-
'''
��1+2+3+...+n��Ҫ����ʹ�ó˳�����for��while��if��else��switch��case�ȹؼ��ּ������ж���䣨A?B:C����
'''
import random
class Solution:
    def Sum_Solution(self, n):
        # write code here
        '''����һֱ�ӵ��ÿ⺯��
        l=list(range(1,n+1))
        return sum(l)
        '''
        #��������ʹ�õݹ�
        #0���κ���and��Ϊ0���κ�����1and��Ϊ�Լ�
        return  (n>0) and (n+self.Sum_Solution(n-1))