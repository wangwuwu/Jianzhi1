# -*- coding:utf-8 -*-
from  itertools import permutations
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #�Ƚ�s1+s2��s2+s1�Ĵ�С����ǰ�ߴ���s2Ӧ��ǰ
        numbers=map(lambda x:str(x),numbers)
        l=len(numbers)
        if l==0:
            return ""
        res=sorted(numbers,lambda x,y:cmp(x+y,y+x))
        result=''.join(i for i in res)
        return result
        
        
        '''
        #��Ϊ�����Ƚ�
        l=len(numbers)
        if l==0:
            return ""
        arrs=permutations(numbers,l)
        t=float('inf')
        for arr in arrs:
            temp=''.join(str(i) for i in arr)
            if t>int(temp):
                t=int(temp)
        return str(t)
        '''