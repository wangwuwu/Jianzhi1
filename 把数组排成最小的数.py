# -*- coding:utf-8 -*-
from  itertools import permutations
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #比较s1+s2和s2+s1的大小，若前者大则s2应在前
        numbers=map(lambda x:str(x),numbers)
        l=len(numbers)
        if l==0:
            return ""
        res=sorted(numbers,lambda x,y:cmp(x+y,y+x))
        result=''.join(i for i in res)
        return result
        
        
        '''
        #此为暴力比较
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