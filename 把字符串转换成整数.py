# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        flag=0
        if s[0]=='+': 
            flag=1
        if s[0]=='-':
            flag=2
        if (flag!=0 and not s[1:].isdigit())or (flag==0 and not s.isdigit()):
            return 0
        sums=0
        temp=s[1:] if flag else s
        for i in temp:
            sums=sums*10+(ord(i)-ord('0'))
        return -sums if flag==2 else sums