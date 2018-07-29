# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)==0:
            return -1
        dic=Counter(s)
        res=filter(lambda x:dic[x]==1,dic)
        l=[]
        for i in res:
            l.append(s.index(i))
        l=sorted(l)
        return l[0]