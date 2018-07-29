# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dic={}
        for i in numbers:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            if dic[i]>len(numbers)/2:
                return i
        return 0