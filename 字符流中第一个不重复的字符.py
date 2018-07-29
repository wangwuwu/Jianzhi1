# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def __init__(self):
        self.l=[]
    # ∑µªÿ∂‘”¶char
    def FirstAppearingOnce(self):
        # write code here
        dic={}
        for i in range(len(self.l)):
            if self.l[i] not in dic:
                dic[self.l[i]]=[i,1]
            else:
                dic[self.l[i]][1]+=1
        filt=list(filter(lambda x:x[1][1]==1,dic.items()))
        if not len(filt):
            return '#'
        sorte=sorted(filt,key=lambda x :x[1][0])
        return sorte[0][0]
    def Insert(self, char):
        # write code here
        self.l.append(char)