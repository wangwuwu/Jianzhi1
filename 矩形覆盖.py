'''
���ǿ�����2*1��С���κ��Ż�������ȥ���Ǹ���ľ��Ρ�������n��2*1��С�������ص��ظ���һ��2*n�Ĵ���Σ��ܹ��ж����ַ�����
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
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