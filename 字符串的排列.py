# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        l=[]
        if not ss :
            return l
        for i in ss:
            l.append(i)
        res=set([''.join(x) for x in itertools.permutations(l, len(l))])
        res=sorted(res)
        return res
        