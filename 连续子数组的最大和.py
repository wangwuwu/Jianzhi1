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
    每个向量都会有一个结尾，计算以array各个元素结尾的向量最大值，对于第i+1个，判断第i个向量最大值是否大于0，若是则与array[i]相加，否则第i+1(即以第i+1个为结尾)最大向量和为array[i+1]
    '''
    