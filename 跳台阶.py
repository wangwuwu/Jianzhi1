'''
һֻ����һ�ο�������1��̨�ף�Ҳ��������2���������������һ��n����̨���ܹ��ж������������Ⱥ����ͬ�㲻ͬ�Ľ������
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        '''���ŵݹ�����쳲���������
        if number==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        n=self.jumpFloor(number-1)+self.jumpFloor(number-2)
        return n
        '''
        one=1
        two=1
        three=0
        if number==0|number==1:
            return 1
        for i in range(2,number+1):
            three=one+two
            one=two
            two=three
        return three
