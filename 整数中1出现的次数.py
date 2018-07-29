# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        from collections import Counter
        sum=0
        for i in range(n+1):
            s=str(i)
            s=list(s)
            counter=Counter(s)
            sum+=counter['1']
        return sum