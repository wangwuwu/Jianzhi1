# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        '''
        ˼·��������β����ָ��start,end���������к�С��tsumʱ��end++���������кʹ���tsumʱ��start++,����������뵽�����У�start<=(1+len(tsum))/2,end<tsum
        '''
        start=1
        end=2
        tempsum=start+end
        mid=(1+tsum)/2
        res=[]
        while start<mid and end <tsum:
            if tempsum<tsum:
                end+=1
                tempsum+=end
            if tempsum>tsum:
                tempsum-=start
                start+=1
            if tempsum==tsum:
                res.append([x for x in range(start,end+1)])
                end+=1#������һ�����γ���ѭ��
                tempsum+=end
        #����
        res=sorted(res,key=lambda x :x[0])
        return res