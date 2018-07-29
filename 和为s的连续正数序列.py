# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        '''
        思路：设置首尾两个指针start,end，当子序列和小于tsum时候，end++，当子序列和大于tsum时候，start++,若等于则加入到队列中，start<=(1+len(tsum))/2,end<tsum
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
                end+=1#少了这一步，形成死循环
                tempsum+=end
        #排序
        res=sorted(res,key=lambda x :x[0])
        return res