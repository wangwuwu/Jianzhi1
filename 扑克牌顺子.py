# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        dic={'A':1,'J':11,'Q':12,'K':13}
        #numbers,map(numbers,dic)
        res=[]
        count0=numbers.count(0)
        for i in numbers:
            if i not in dic:
                res.append(i)
            else:
                res.append(dic[i])
        res=sorted(res)
        flag=True
        if count0==0:
            for ii in range(4):
                if (res[ii]+1)!=res[ii+1]:
                    return False
            return True
        else:
            tsum=0
            for j in range(4):
                if res[j]!=0:
                    tsum+=res[j+1]-res[j]-1
            return True if tsum==count0 or count0==4 else False