# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        '''
        res =len(array) and max(array)
        temp = 0
        for i in array:
            temp = max(i,temp+i)
            res = max(res,temp)
        return res
        '''
        res=[0]*(1+len(array))
        for i in range(len(array)):
            if res[i]>0:
                res[i+1]=res[i]+array[i]
            else:
                res[i+1]=array[i]
        return max(res[1:])
    '''
    ÿ������������һ����β��������array����Ԫ�ؽ�β���������ֵ�����ڵ�i+1�����жϵ�i���������ֵ�Ƿ����0����������array[i]��ӣ������i+1(���Ե�i+1��Ϊ��β)���������Ϊarray[i+1]
    '''
    