'''
һֻ����һ�ο�������1��̨�ף�Ҳ��������2��������Ҳ��������n���������������һ��n����̨���ܹ��ж�����������
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        '''
��Ϊn��̨�ף���һ����n����������1������2��������n��
��1����ʣ��n-1������ʣ��������f(n-1)
��2����ʣ��n-2������ʣ��������f(n-2)
����f(n)=f(n-1)+f(n-2)+...+f(1)
��Ϊf(n-1)=f(n-2)+f(n-3)+...+f(1)
����f(n)=2*f(n-1)
        '''
        if number==0:
            return 0
        if number==1:
            return 1
        one=1
        two=1
        for i in range(2,number+1):
            two=2*one
            one=two
        return two