# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        '''
        由分析可知，数组两端符合题意的乘积要小于中间的，可以采用左右夹逼法
        大时右减，小时左加，可以保证乘积最小的先找到
        '''
        start=0
        end=len(array)-1
        while start<end :
            if array[start]+array[end]<tsum:
                start+=1
            if array[start]+array[end]>tsum:
                end-=1
            if array[start]+array[end]==tsum:
                return array[start],array[end]
        return []